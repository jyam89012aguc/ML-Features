"""Generated capitulation features for 40_close_location: close within daily range.
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

def clv_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def clv_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def clv_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def clv_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def clv_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def clv_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def clv_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def clv_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def clv_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def clv_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def clv_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def clv_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def clv_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def clv_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def clv_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def clv_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def clv_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def clv_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def clv_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def clv_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def clv_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def clv_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def clv_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def clv_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def clv_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def clv_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def clv_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def clv_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def clv_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def clv_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def clv_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def clv_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def clv_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def clv_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def clv_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def clv_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def clv_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def clv_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def clv_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def clv_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def clv_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def clv_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def clv_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def clv_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def clv_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def clv_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def clv_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def clv_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def clv_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def clv_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def clv_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def clv_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def clv_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def clv_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def clv_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def clv_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def clv_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def clv_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def clv_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

CLOSE_LOCATION_REGISTRY_076_150 = {
    "clv_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_076_capitulation_signal},
    "clv_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_077_capitulation_signal},
    "clv_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_078_capitulation_signal},
    "clv_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_079_capitulation_signal},
    "clv_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_080_capitulation_signal},
    "clv_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_081_capitulation_signal},
    "clv_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_082_capitulation_signal},
    "clv_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_083_capitulation_signal},
    "clv_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_084_capitulation_signal},
    "clv_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_085_capitulation_signal},
    "clv_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_086_capitulation_signal},
    "clv_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_087_capitulation_signal},
    "clv_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_088_capitulation_signal},
    "clv_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_089_capitulation_signal},
    "clv_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_090_capitulation_signal},
    "clv_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_091_capitulation_signal},
    "clv_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_092_capitulation_signal},
    "clv_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_093_capitulation_signal},
    "clv_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_094_capitulation_signal},
    "clv_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_095_capitulation_signal},
    "clv_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_096_capitulation_signal},
    "clv_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_097_capitulation_signal},
    "clv_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_098_capitulation_signal},
    "clv_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_099_capitulation_signal},
    "clv_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_100_capitulation_signal},
    "clv_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_101_capitulation_signal},
    "clv_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_102_capitulation_signal},
    "clv_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_103_capitulation_signal},
    "clv_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_104_capitulation_signal},
    "clv_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_105_capitulation_signal},
    "clv_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_106_capitulation_signal},
    "clv_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_107_capitulation_signal},
    "clv_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_108_capitulation_signal},
    "clv_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_109_capitulation_signal},
    "clv_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_110_capitulation_signal},
    "clv_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_111_capitulation_signal},
    "clv_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_112_capitulation_signal},
    "clv_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_113_capitulation_signal},
    "clv_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_114_capitulation_signal},
    "clv_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_115_capitulation_signal},
    "clv_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_116_capitulation_signal},
    "clv_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_117_capitulation_signal},
    "clv_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_118_capitulation_signal},
    "clv_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_119_capitulation_signal},
    "clv_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_120_capitulation_signal},
    "clv_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_121_capitulation_signal},
    "clv_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_122_capitulation_signal},
    "clv_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_123_capitulation_signal},
    "clv_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_124_capitulation_signal},
    "clv_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_125_capitulation_signal},
    "clv_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_126_capitulation_signal},
    "clv_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_127_capitulation_signal},
    "clv_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_128_capitulation_signal},
    "clv_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_129_capitulation_signal},
    "clv_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_130_capitulation_signal},
    "clv_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_131_capitulation_signal},
    "clv_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_132_capitulation_signal},
    "clv_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_133_capitulation_signal},
    "clv_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_134_capitulation_signal},
    "clv_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_135_capitulation_signal},
    "clv_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_136_capitulation_signal},
    "clv_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_137_capitulation_signal},
    "clv_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_138_capitulation_signal},
    "clv_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_139_capitulation_signal},
    "clv_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_140_capitulation_signal},
    "clv_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_141_capitulation_signal},
    "clv_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_142_capitulation_signal},
    "clv_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_143_capitulation_signal},
    "clv_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_144_capitulation_signal},
    "clv_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_145_capitulation_signal},
    "clv_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_146_capitulation_signal},
    "clv_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_147_capitulation_signal},
    "clv_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_148_capitulation_signal},
    "clv_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_149_capitulation_signal},
    "clv_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_150_capitulation_signal},
}
