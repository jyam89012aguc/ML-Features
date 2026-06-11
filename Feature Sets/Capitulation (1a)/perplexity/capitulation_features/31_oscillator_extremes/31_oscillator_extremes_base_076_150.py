"""Generated capitulation features for 31_oscillator_extremes: stochastic extremes.
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

def osc_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def osc_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def osc_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def osc_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def osc_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def osc_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def osc_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def osc_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def osc_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def osc_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def osc_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def osc_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def osc_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def osc_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def osc_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def osc_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def osc_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def osc_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def osc_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def osc_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def osc_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def osc_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def osc_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def osc_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def osc_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def osc_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def osc_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def osc_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def osc_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def osc_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def osc_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def osc_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def osc_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def osc_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def osc_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def osc_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def osc_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def osc_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def osc_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def osc_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def osc_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def osc_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def osc_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def osc_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def osc_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def osc_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def osc_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def osc_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def osc_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def osc_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def osc_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def osc_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def osc_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def osc_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def osc_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def osc_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def osc_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def osc_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def osc_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

OSCILLATOR_EXTREMES_REGISTRY_076_150 = {
    "osc_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_076_capitulation_signal},
    "osc_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_077_capitulation_signal},
    "osc_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_078_capitulation_signal},
    "osc_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_079_capitulation_signal},
    "osc_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_080_capitulation_signal},
    "osc_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_081_capitulation_signal},
    "osc_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_082_capitulation_signal},
    "osc_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_083_capitulation_signal},
    "osc_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_084_capitulation_signal},
    "osc_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_085_capitulation_signal},
    "osc_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_086_capitulation_signal},
    "osc_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_087_capitulation_signal},
    "osc_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_088_capitulation_signal},
    "osc_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_089_capitulation_signal},
    "osc_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_090_capitulation_signal},
    "osc_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_091_capitulation_signal},
    "osc_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_092_capitulation_signal},
    "osc_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_093_capitulation_signal},
    "osc_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_094_capitulation_signal},
    "osc_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_095_capitulation_signal},
    "osc_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_096_capitulation_signal},
    "osc_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_097_capitulation_signal},
    "osc_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_098_capitulation_signal},
    "osc_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_099_capitulation_signal},
    "osc_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_100_capitulation_signal},
    "osc_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_101_capitulation_signal},
    "osc_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_102_capitulation_signal},
    "osc_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_103_capitulation_signal},
    "osc_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_104_capitulation_signal},
    "osc_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_105_capitulation_signal},
    "osc_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_106_capitulation_signal},
    "osc_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_107_capitulation_signal},
    "osc_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_108_capitulation_signal},
    "osc_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_109_capitulation_signal},
    "osc_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_110_capitulation_signal},
    "osc_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_111_capitulation_signal},
    "osc_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_112_capitulation_signal},
    "osc_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_113_capitulation_signal},
    "osc_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_114_capitulation_signal},
    "osc_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_115_capitulation_signal},
    "osc_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_116_capitulation_signal},
    "osc_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_117_capitulation_signal},
    "osc_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_118_capitulation_signal},
    "osc_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_119_capitulation_signal},
    "osc_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_120_capitulation_signal},
    "osc_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_121_capitulation_signal},
    "osc_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_122_capitulation_signal},
    "osc_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_123_capitulation_signal},
    "osc_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_124_capitulation_signal},
    "osc_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_125_capitulation_signal},
    "osc_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_126_capitulation_signal},
    "osc_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_127_capitulation_signal},
    "osc_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_128_capitulation_signal},
    "osc_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_129_capitulation_signal},
    "osc_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_130_capitulation_signal},
    "osc_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_131_capitulation_signal},
    "osc_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_132_capitulation_signal},
    "osc_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_133_capitulation_signal},
    "osc_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_134_capitulation_signal},
    "osc_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_135_capitulation_signal},
    "osc_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_136_capitulation_signal},
    "osc_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_137_capitulation_signal},
    "osc_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_138_capitulation_signal},
    "osc_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_139_capitulation_signal},
    "osc_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_140_capitulation_signal},
    "osc_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_141_capitulation_signal},
    "osc_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_142_capitulation_signal},
    "osc_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_143_capitulation_signal},
    "osc_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_144_capitulation_signal},
    "osc_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_145_capitulation_signal},
    "osc_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_146_capitulation_signal},
    "osc_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_147_capitulation_signal},
    "osc_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_148_capitulation_signal},
    "osc_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_149_capitulation_signal},
    "osc_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_150_capitulation_signal},
}
