"""Generated capitulation features for 42_volatility_of_volatility: instability of volatility.
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

def vov_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vov_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vov_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vov_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vov_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vov_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vov_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vov_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vov_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vov_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vov_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vov_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vov_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vov_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vov_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vov_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vov_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vov_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vov_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vov_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vov_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vov_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vov_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vov_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vov_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vov_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vov_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vov_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vov_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vov_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vov_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vov_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vov_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vov_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vov_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vov_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vov_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vov_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vov_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vov_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vov_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vov_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vov_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vov_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vov_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vov_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vov_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vov_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vov_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vov_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vov_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vov_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vov_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vov_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vov_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vov_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vov_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vov_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vov_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLATILITY_OF_VOLATILITY_REGISTRY_076_150 = {
    "vov_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_076_capitulation_signal},
    "vov_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_077_capitulation_signal},
    "vov_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_078_capitulation_signal},
    "vov_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_079_capitulation_signal},
    "vov_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_080_capitulation_signal},
    "vov_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_081_capitulation_signal},
    "vov_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_082_capitulation_signal},
    "vov_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_083_capitulation_signal},
    "vov_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_084_capitulation_signal},
    "vov_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_085_capitulation_signal},
    "vov_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_086_capitulation_signal},
    "vov_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_087_capitulation_signal},
    "vov_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_088_capitulation_signal},
    "vov_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_089_capitulation_signal},
    "vov_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_090_capitulation_signal},
    "vov_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_091_capitulation_signal},
    "vov_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_092_capitulation_signal},
    "vov_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_093_capitulation_signal},
    "vov_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_094_capitulation_signal},
    "vov_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_095_capitulation_signal},
    "vov_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_096_capitulation_signal},
    "vov_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_097_capitulation_signal},
    "vov_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_098_capitulation_signal},
    "vov_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_099_capitulation_signal},
    "vov_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_100_capitulation_signal},
    "vov_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_101_capitulation_signal},
    "vov_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_102_capitulation_signal},
    "vov_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_103_capitulation_signal},
    "vov_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_104_capitulation_signal},
    "vov_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_105_capitulation_signal},
    "vov_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_106_capitulation_signal},
    "vov_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_107_capitulation_signal},
    "vov_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_108_capitulation_signal},
    "vov_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_109_capitulation_signal},
    "vov_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_110_capitulation_signal},
    "vov_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_111_capitulation_signal},
    "vov_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_112_capitulation_signal},
    "vov_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_113_capitulation_signal},
    "vov_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_114_capitulation_signal},
    "vov_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_115_capitulation_signal},
    "vov_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_116_capitulation_signal},
    "vov_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_117_capitulation_signal},
    "vov_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_118_capitulation_signal},
    "vov_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_119_capitulation_signal},
    "vov_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_120_capitulation_signal},
    "vov_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_121_capitulation_signal},
    "vov_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_122_capitulation_signal},
    "vov_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_123_capitulation_signal},
    "vov_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_124_capitulation_signal},
    "vov_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_125_capitulation_signal},
    "vov_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_126_capitulation_signal},
    "vov_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_127_capitulation_signal},
    "vov_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_128_capitulation_signal},
    "vov_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_129_capitulation_signal},
    "vov_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_130_capitulation_signal},
    "vov_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_131_capitulation_signal},
    "vov_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_132_capitulation_signal},
    "vov_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_133_capitulation_signal},
    "vov_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_134_capitulation_signal},
    "vov_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_135_capitulation_signal},
    "vov_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_136_capitulation_signal},
    "vov_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_137_capitulation_signal},
    "vov_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_138_capitulation_signal},
    "vov_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_139_capitulation_signal},
    "vov_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_140_capitulation_signal},
    "vov_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_141_capitulation_signal},
    "vov_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_142_capitulation_signal},
    "vov_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_143_capitulation_signal},
    "vov_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_144_capitulation_signal},
    "vov_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_145_capitulation_signal},
    "vov_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_146_capitulation_signal},
    "vov_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_147_capitulation_signal},
    "vov_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_148_capitulation_signal},
    "vov_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_149_capitulation_signal},
    "vov_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_150_capitulation_signal},
}
