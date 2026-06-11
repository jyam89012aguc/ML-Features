"""Generated capitulation features for 21_volume_concentration: share of volume in worst days.
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

def vcc_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vcc_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vcc_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vcc_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vcc_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vcc_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vcc_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vcc_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vcc_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vcc_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vcc_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vcc_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vcc_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vcc_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vcc_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vcc_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vcc_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vcc_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vcc_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vcc_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vcc_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vcc_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vcc_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vcc_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vcc_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vcc_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vcc_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vcc_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vcc_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vcc_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vcc_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vcc_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vcc_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vcc_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vcc_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vcc_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vcc_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vcc_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vcc_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vcc_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vcc_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vcc_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vcc_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vcc_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vcc_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vcc_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vcc_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vcc_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vcc_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vcc_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vcc_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_CONCENTRATION_REGISTRY_076_150 = {
    "vcc_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_076_capitulation_signal},
    "vcc_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_077_capitulation_signal},
    "vcc_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_078_capitulation_signal},
    "vcc_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_079_capitulation_signal},
    "vcc_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_080_capitulation_signal},
    "vcc_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_081_capitulation_signal},
    "vcc_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_082_capitulation_signal},
    "vcc_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_083_capitulation_signal},
    "vcc_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_084_capitulation_signal},
    "vcc_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_085_capitulation_signal},
    "vcc_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_086_capitulation_signal},
    "vcc_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_087_capitulation_signal},
    "vcc_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_088_capitulation_signal},
    "vcc_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_089_capitulation_signal},
    "vcc_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_090_capitulation_signal},
    "vcc_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_091_capitulation_signal},
    "vcc_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_092_capitulation_signal},
    "vcc_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_093_capitulation_signal},
    "vcc_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_094_capitulation_signal},
    "vcc_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_095_capitulation_signal},
    "vcc_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_096_capitulation_signal},
    "vcc_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_097_capitulation_signal},
    "vcc_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_098_capitulation_signal},
    "vcc_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_099_capitulation_signal},
    "vcc_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_100_capitulation_signal},
    "vcc_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_101_capitulation_signal},
    "vcc_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_102_capitulation_signal},
    "vcc_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_103_capitulation_signal},
    "vcc_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_104_capitulation_signal},
    "vcc_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_105_capitulation_signal},
    "vcc_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_106_capitulation_signal},
    "vcc_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_107_capitulation_signal},
    "vcc_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_108_capitulation_signal},
    "vcc_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_109_capitulation_signal},
    "vcc_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_110_capitulation_signal},
    "vcc_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_111_capitulation_signal},
    "vcc_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_112_capitulation_signal},
    "vcc_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_113_capitulation_signal},
    "vcc_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_114_capitulation_signal},
    "vcc_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_115_capitulation_signal},
    "vcc_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_116_capitulation_signal},
    "vcc_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_117_capitulation_signal},
    "vcc_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_118_capitulation_signal},
    "vcc_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_119_capitulation_signal},
    "vcc_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_120_capitulation_signal},
    "vcc_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_121_capitulation_signal},
    "vcc_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_122_capitulation_signal},
    "vcc_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_123_capitulation_signal},
    "vcc_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_124_capitulation_signal},
    "vcc_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_125_capitulation_signal},
    "vcc_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_126_capitulation_signal},
    "vcc_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_127_capitulation_signal},
    "vcc_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_128_capitulation_signal},
    "vcc_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_129_capitulation_signal},
    "vcc_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_130_capitulation_signal},
    "vcc_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_131_capitulation_signal},
    "vcc_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_132_capitulation_signal},
    "vcc_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_133_capitulation_signal},
    "vcc_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_134_capitulation_signal},
    "vcc_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_135_capitulation_signal},
    "vcc_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_136_capitulation_signal},
    "vcc_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_137_capitulation_signal},
    "vcc_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_138_capitulation_signal},
    "vcc_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_139_capitulation_signal},
    "vcc_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_140_capitulation_signal},
    "vcc_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_141_capitulation_signal},
    "vcc_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_142_capitulation_signal},
    "vcc_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_143_capitulation_signal},
    "vcc_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_144_capitulation_signal},
    "vcc_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_145_capitulation_signal},
    "vcc_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_146_capitulation_signal},
    "vcc_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_147_capitulation_signal},
    "vcc_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_148_capitulation_signal},
    "vcc_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_149_capitulation_signal},
    "vcc_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_150_capitulation_signal},
}
