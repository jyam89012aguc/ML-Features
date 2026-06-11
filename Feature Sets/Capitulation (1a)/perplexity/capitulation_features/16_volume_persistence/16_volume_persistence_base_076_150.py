"""Generated capitulation features for 16_volume_persistence: sustained elevated volume.
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

def vp_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vp_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vp_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vp_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vp_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vp_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vp_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vp_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vp_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vp_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vp_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vp_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vp_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vp_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vp_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vp_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vp_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vp_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vp_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vp_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vp_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vp_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vp_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vp_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vp_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vp_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vp_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vp_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vp_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vp_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vp_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vp_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vp_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vp_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vp_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vp_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vp_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vp_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vp_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vp_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vp_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vp_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vp_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vp_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vp_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vp_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vp_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vp_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vp_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vp_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vp_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vp_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vp_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vp_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vp_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vp_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vp_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vp_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vp_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_PERSISTENCE_REGISTRY_076_150 = {
    "vp_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_076_capitulation_signal},
    "vp_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_077_capitulation_signal},
    "vp_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_078_capitulation_signal},
    "vp_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_079_capitulation_signal},
    "vp_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_080_capitulation_signal},
    "vp_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_081_capitulation_signal},
    "vp_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_082_capitulation_signal},
    "vp_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_083_capitulation_signal},
    "vp_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_084_capitulation_signal},
    "vp_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_085_capitulation_signal},
    "vp_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_086_capitulation_signal},
    "vp_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_087_capitulation_signal},
    "vp_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_088_capitulation_signal},
    "vp_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_089_capitulation_signal},
    "vp_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_090_capitulation_signal},
    "vp_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_091_capitulation_signal},
    "vp_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_092_capitulation_signal},
    "vp_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_093_capitulation_signal},
    "vp_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_094_capitulation_signal},
    "vp_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_095_capitulation_signal},
    "vp_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_096_capitulation_signal},
    "vp_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_097_capitulation_signal},
    "vp_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_098_capitulation_signal},
    "vp_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_099_capitulation_signal},
    "vp_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_100_capitulation_signal},
    "vp_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_101_capitulation_signal},
    "vp_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_102_capitulation_signal},
    "vp_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_103_capitulation_signal},
    "vp_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_104_capitulation_signal},
    "vp_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_105_capitulation_signal},
    "vp_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_106_capitulation_signal},
    "vp_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_107_capitulation_signal},
    "vp_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_108_capitulation_signal},
    "vp_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_109_capitulation_signal},
    "vp_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_110_capitulation_signal},
    "vp_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_111_capitulation_signal},
    "vp_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_112_capitulation_signal},
    "vp_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_113_capitulation_signal},
    "vp_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_114_capitulation_signal},
    "vp_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_115_capitulation_signal},
    "vp_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_116_capitulation_signal},
    "vp_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_117_capitulation_signal},
    "vp_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_118_capitulation_signal},
    "vp_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_119_capitulation_signal},
    "vp_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_120_capitulation_signal},
    "vp_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_121_capitulation_signal},
    "vp_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_122_capitulation_signal},
    "vp_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_123_capitulation_signal},
    "vp_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_124_capitulation_signal},
    "vp_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_125_capitulation_signal},
    "vp_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_126_capitulation_signal},
    "vp_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_127_capitulation_signal},
    "vp_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_128_capitulation_signal},
    "vp_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_129_capitulation_signal},
    "vp_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_130_capitulation_signal},
    "vp_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_131_capitulation_signal},
    "vp_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_132_capitulation_signal},
    "vp_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_133_capitulation_signal},
    "vp_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_134_capitulation_signal},
    "vp_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_135_capitulation_signal},
    "vp_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_136_capitulation_signal},
    "vp_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_137_capitulation_signal},
    "vp_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_138_capitulation_signal},
    "vp_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_139_capitulation_signal},
    "vp_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_140_capitulation_signal},
    "vp_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_141_capitulation_signal},
    "vp_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_142_capitulation_signal},
    "vp_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_143_capitulation_signal},
    "vp_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_144_capitulation_signal},
    "vp_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_145_capitulation_signal},
    "vp_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_146_capitulation_signal},
    "vp_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_147_capitulation_signal},
    "vp_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_148_capitulation_signal},
    "vp_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_149_capitulation_signal},
    "vp_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_150_capitulation_signal},
}
