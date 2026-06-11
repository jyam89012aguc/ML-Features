"""Generated capitulation features for 34_velocity_inflection: sign change in price velocity.
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

def vif_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vif_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vif_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vif_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vif_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vif_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vif_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vif_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vif_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vif_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vif_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vif_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vif_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vif_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vif_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vif_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vif_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vif_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vif_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vif_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vif_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vif_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vif_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vif_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vif_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vif_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vif_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vif_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vif_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vif_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vif_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vif_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vif_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vif_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vif_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vif_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vif_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vif_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vif_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vif_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vif_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vif_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vif_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vif_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vif_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vif_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vif_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vif_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vif_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vif_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vif_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vif_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vif_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vif_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vif_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vif_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vif_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vif_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vif_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VELOCITY_INFLECTION_REGISTRY_076_150 = {
    "vif_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_076_capitulation_signal},
    "vif_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_077_capitulation_signal},
    "vif_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_078_capitulation_signal},
    "vif_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_079_capitulation_signal},
    "vif_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_080_capitulation_signal},
    "vif_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_081_capitulation_signal},
    "vif_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_082_capitulation_signal},
    "vif_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_083_capitulation_signal},
    "vif_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_084_capitulation_signal},
    "vif_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_085_capitulation_signal},
    "vif_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_086_capitulation_signal},
    "vif_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_087_capitulation_signal},
    "vif_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_088_capitulation_signal},
    "vif_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_089_capitulation_signal},
    "vif_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_090_capitulation_signal},
    "vif_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_091_capitulation_signal},
    "vif_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_092_capitulation_signal},
    "vif_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_093_capitulation_signal},
    "vif_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_094_capitulation_signal},
    "vif_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_095_capitulation_signal},
    "vif_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_096_capitulation_signal},
    "vif_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_097_capitulation_signal},
    "vif_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_098_capitulation_signal},
    "vif_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_099_capitulation_signal},
    "vif_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_100_capitulation_signal},
    "vif_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_101_capitulation_signal},
    "vif_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_102_capitulation_signal},
    "vif_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_103_capitulation_signal},
    "vif_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_104_capitulation_signal},
    "vif_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_105_capitulation_signal},
    "vif_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_106_capitulation_signal},
    "vif_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_107_capitulation_signal},
    "vif_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_108_capitulation_signal},
    "vif_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_109_capitulation_signal},
    "vif_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_110_capitulation_signal},
    "vif_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_111_capitulation_signal},
    "vif_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_112_capitulation_signal},
    "vif_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_113_capitulation_signal},
    "vif_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_114_capitulation_signal},
    "vif_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_115_capitulation_signal},
    "vif_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_116_capitulation_signal},
    "vif_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_117_capitulation_signal},
    "vif_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_118_capitulation_signal},
    "vif_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_119_capitulation_signal},
    "vif_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_120_capitulation_signal},
    "vif_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_121_capitulation_signal},
    "vif_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_122_capitulation_signal},
    "vif_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_123_capitulation_signal},
    "vif_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_124_capitulation_signal},
    "vif_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_125_capitulation_signal},
    "vif_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_126_capitulation_signal},
    "vif_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_127_capitulation_signal},
    "vif_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_128_capitulation_signal},
    "vif_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_129_capitulation_signal},
    "vif_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_130_capitulation_signal},
    "vif_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_131_capitulation_signal},
    "vif_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_132_capitulation_signal},
    "vif_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_133_capitulation_signal},
    "vif_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_134_capitulation_signal},
    "vif_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_135_capitulation_signal},
    "vif_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_136_capitulation_signal},
    "vif_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_137_capitulation_signal},
    "vif_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_138_capitulation_signal},
    "vif_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_139_capitulation_signal},
    "vif_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_140_capitulation_signal},
    "vif_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_141_capitulation_signal},
    "vif_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_142_capitulation_signal},
    "vif_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_143_capitulation_signal},
    "vif_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_144_capitulation_signal},
    "vif_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_145_capitulation_signal},
    "vif_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_146_capitulation_signal},
    "vif_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_147_capitulation_signal},
    "vif_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_148_capitulation_signal},
    "vif_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_149_capitulation_signal},
    "vif_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_150_capitulation_signal},
}
