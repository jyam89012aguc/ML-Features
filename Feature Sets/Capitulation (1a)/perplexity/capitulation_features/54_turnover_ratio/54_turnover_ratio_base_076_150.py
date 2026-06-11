"""Generated capitulation features for 54_turnover_ratio: volume/share extremes.
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

def tnv_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def tnv_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def tnv_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def tnv_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def tnv_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def tnv_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def tnv_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def tnv_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def tnv_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def tnv_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def tnv_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def tnv_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def tnv_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def tnv_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def tnv_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def tnv_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tnv_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def tnv_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def tnv_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def tnv_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def tnv_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def tnv_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def tnv_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def tnv_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def tnv_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def tnv_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def tnv_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def tnv_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def tnv_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def tnv_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tnv_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def tnv_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def tnv_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def tnv_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def tnv_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def tnv_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def tnv_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def tnv_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def tnv_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def tnv_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def tnv_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def tnv_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def tnv_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def tnv_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tnv_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def tnv_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def tnv_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def tnv_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def tnv_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def tnv_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def tnv_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def tnv_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def tnv_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def tnv_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def tnv_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def tnv_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def tnv_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def tnv_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tnv_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

TURNOVER_RATIO_REGISTRY_076_150 = {
    "tnv_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_076_capitulation_signal},
    "tnv_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_077_capitulation_signal},
    "tnv_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_078_capitulation_signal},
    "tnv_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_079_capitulation_signal},
    "tnv_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_080_capitulation_signal},
    "tnv_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_081_capitulation_signal},
    "tnv_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_082_capitulation_signal},
    "tnv_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_083_capitulation_signal},
    "tnv_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_084_capitulation_signal},
    "tnv_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_085_capitulation_signal},
    "tnv_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_086_capitulation_signal},
    "tnv_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_087_capitulation_signal},
    "tnv_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_088_capitulation_signal},
    "tnv_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_089_capitulation_signal},
    "tnv_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_090_capitulation_signal},
    "tnv_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_091_capitulation_signal},
    "tnv_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_092_capitulation_signal},
    "tnv_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_093_capitulation_signal},
    "tnv_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_094_capitulation_signal},
    "tnv_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_095_capitulation_signal},
    "tnv_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_096_capitulation_signal},
    "tnv_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_097_capitulation_signal},
    "tnv_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_098_capitulation_signal},
    "tnv_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_099_capitulation_signal},
    "tnv_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_100_capitulation_signal},
    "tnv_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_101_capitulation_signal},
    "tnv_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_102_capitulation_signal},
    "tnv_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_103_capitulation_signal},
    "tnv_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_104_capitulation_signal},
    "tnv_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_105_capitulation_signal},
    "tnv_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_106_capitulation_signal},
    "tnv_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_107_capitulation_signal},
    "tnv_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_108_capitulation_signal},
    "tnv_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_109_capitulation_signal},
    "tnv_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_110_capitulation_signal},
    "tnv_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_111_capitulation_signal},
    "tnv_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_112_capitulation_signal},
    "tnv_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_113_capitulation_signal},
    "tnv_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_114_capitulation_signal},
    "tnv_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_115_capitulation_signal},
    "tnv_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_116_capitulation_signal},
    "tnv_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_117_capitulation_signal},
    "tnv_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_118_capitulation_signal},
    "tnv_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_119_capitulation_signal},
    "tnv_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_120_capitulation_signal},
    "tnv_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_121_capitulation_signal},
    "tnv_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_122_capitulation_signal},
    "tnv_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_123_capitulation_signal},
    "tnv_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_124_capitulation_signal},
    "tnv_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_125_capitulation_signal},
    "tnv_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_126_capitulation_signal},
    "tnv_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_127_capitulation_signal},
    "tnv_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_128_capitulation_signal},
    "tnv_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_129_capitulation_signal},
    "tnv_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_130_capitulation_signal},
    "tnv_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_131_capitulation_signal},
    "tnv_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_132_capitulation_signal},
    "tnv_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_133_capitulation_signal},
    "tnv_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_134_capitulation_signal},
    "tnv_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_135_capitulation_signal},
    "tnv_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_136_capitulation_signal},
    "tnv_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_137_capitulation_signal},
    "tnv_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_138_capitulation_signal},
    "tnv_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_139_capitulation_signal},
    "tnv_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_140_capitulation_signal},
    "tnv_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_141_capitulation_signal},
    "tnv_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_142_capitulation_signal},
    "tnv_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_143_capitulation_signal},
    "tnv_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_144_capitulation_signal},
    "tnv_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_145_capitulation_signal},
    "tnv_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_146_capitulation_signal},
    "tnv_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_147_capitulation_signal},
    "tnv_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_148_capitulation_signal},
    "tnv_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_149_capitulation_signal},
    "tnv_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_150_capitulation_signal},
}
