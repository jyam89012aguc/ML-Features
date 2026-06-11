"""Generated capitulation features for 35_capitulation_thrust: final-leg-down thrust.
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

def cth_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def cth_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def cth_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def cth_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def cth_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def cth_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def cth_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def cth_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def cth_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def cth_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def cth_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def cth_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def cth_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def cth_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def cth_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def cth_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def cth_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def cth_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def cth_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def cth_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def cth_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def cth_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def cth_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def cth_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def cth_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def cth_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def cth_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def cth_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def cth_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def cth_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def cth_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def cth_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def cth_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def cth_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def cth_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def cth_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def cth_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def cth_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def cth_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def cth_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def cth_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def cth_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def cth_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def cth_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def cth_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def cth_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def cth_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def cth_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def cth_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def cth_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def cth_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def cth_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def cth_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def cth_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def cth_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def cth_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def cth_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def cth_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def cth_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

CAPITULATION_THRUST_REGISTRY_076_150 = {
    "cth_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_076_capitulation_signal},
    "cth_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_077_capitulation_signal},
    "cth_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_078_capitulation_signal},
    "cth_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_079_capitulation_signal},
    "cth_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_080_capitulation_signal},
    "cth_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_081_capitulation_signal},
    "cth_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_082_capitulation_signal},
    "cth_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_083_capitulation_signal},
    "cth_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_084_capitulation_signal},
    "cth_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_085_capitulation_signal},
    "cth_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_086_capitulation_signal},
    "cth_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_087_capitulation_signal},
    "cth_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_088_capitulation_signal},
    "cth_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_089_capitulation_signal},
    "cth_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_090_capitulation_signal},
    "cth_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_091_capitulation_signal},
    "cth_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_092_capitulation_signal},
    "cth_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_093_capitulation_signal},
    "cth_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_094_capitulation_signal},
    "cth_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_095_capitulation_signal},
    "cth_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_096_capitulation_signal},
    "cth_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_097_capitulation_signal},
    "cth_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_098_capitulation_signal},
    "cth_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_099_capitulation_signal},
    "cth_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_100_capitulation_signal},
    "cth_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_101_capitulation_signal},
    "cth_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_102_capitulation_signal},
    "cth_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_103_capitulation_signal},
    "cth_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_104_capitulation_signal},
    "cth_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_105_capitulation_signal},
    "cth_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_106_capitulation_signal},
    "cth_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_107_capitulation_signal},
    "cth_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_108_capitulation_signal},
    "cth_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_109_capitulation_signal},
    "cth_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_110_capitulation_signal},
    "cth_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_111_capitulation_signal},
    "cth_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_112_capitulation_signal},
    "cth_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_113_capitulation_signal},
    "cth_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_114_capitulation_signal},
    "cth_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_115_capitulation_signal},
    "cth_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_116_capitulation_signal},
    "cth_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_117_capitulation_signal},
    "cth_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_118_capitulation_signal},
    "cth_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_119_capitulation_signal},
    "cth_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_120_capitulation_signal},
    "cth_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_121_capitulation_signal},
    "cth_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_122_capitulation_signal},
    "cth_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_123_capitulation_signal},
    "cth_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_124_capitulation_signal},
    "cth_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_125_capitulation_signal},
    "cth_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_126_capitulation_signal},
    "cth_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_127_capitulation_signal},
    "cth_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_128_capitulation_signal},
    "cth_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_129_capitulation_signal},
    "cth_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_130_capitulation_signal},
    "cth_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_131_capitulation_signal},
    "cth_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_132_capitulation_signal},
    "cth_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_133_capitulation_signal},
    "cth_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_134_capitulation_signal},
    "cth_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_135_capitulation_signal},
    "cth_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_136_capitulation_signal},
    "cth_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_137_capitulation_signal},
    "cth_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_138_capitulation_signal},
    "cth_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_139_capitulation_signal},
    "cth_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_140_capitulation_signal},
    "cth_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_141_capitulation_signal},
    "cth_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_142_capitulation_signal},
    "cth_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_143_capitulation_signal},
    "cth_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_144_capitulation_signal},
    "cth_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_145_capitulation_signal},
    "cth_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_146_capitulation_signal},
    "cth_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_147_capitulation_signal},
    "cth_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_148_capitulation_signal},
    "cth_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_149_capitulation_signal},
    "cth_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_150_capitulation_signal},
}
