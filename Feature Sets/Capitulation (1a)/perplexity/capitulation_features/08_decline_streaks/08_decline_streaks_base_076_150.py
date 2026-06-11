"""Generated capitulation features for 08_decline_streaks: consecutive down days/weeks/months.
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

def dstk_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dstk_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dstk_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dstk_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dstk_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dstk_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dstk_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dstk_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dstk_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dstk_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dstk_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dstk_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dstk_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dstk_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dstk_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dstk_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dstk_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dstk_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dstk_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dstk_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dstk_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dstk_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dstk_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dstk_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dstk_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dstk_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dstk_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dstk_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dstk_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dstk_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dstk_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dstk_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dstk_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dstk_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dstk_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dstk_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dstk_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dstk_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dstk_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dstk_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dstk_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dstk_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dstk_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dstk_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dstk_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dstk_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dstk_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dstk_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dstk_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dstk_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dstk_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dstk_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dstk_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dstk_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dstk_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dstk_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dstk_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dstk_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dstk_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DECLINE_STREAKS_REGISTRY_076_150 = {
    "dstk_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_076_capitulation_signal},
    "dstk_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_077_capitulation_signal},
    "dstk_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_078_capitulation_signal},
    "dstk_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_079_capitulation_signal},
    "dstk_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_080_capitulation_signal},
    "dstk_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_081_capitulation_signal},
    "dstk_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_082_capitulation_signal},
    "dstk_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_083_capitulation_signal},
    "dstk_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_084_capitulation_signal},
    "dstk_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_085_capitulation_signal},
    "dstk_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_086_capitulation_signal},
    "dstk_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_087_capitulation_signal},
    "dstk_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_088_capitulation_signal},
    "dstk_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_089_capitulation_signal},
    "dstk_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_090_capitulation_signal},
    "dstk_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_091_capitulation_signal},
    "dstk_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_092_capitulation_signal},
    "dstk_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_093_capitulation_signal},
    "dstk_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_094_capitulation_signal},
    "dstk_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_095_capitulation_signal},
    "dstk_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_096_capitulation_signal},
    "dstk_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_097_capitulation_signal},
    "dstk_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_098_capitulation_signal},
    "dstk_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_099_capitulation_signal},
    "dstk_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_100_capitulation_signal},
    "dstk_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_101_capitulation_signal},
    "dstk_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_102_capitulation_signal},
    "dstk_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_103_capitulation_signal},
    "dstk_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_104_capitulation_signal},
    "dstk_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_105_capitulation_signal},
    "dstk_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_106_capitulation_signal},
    "dstk_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_107_capitulation_signal},
    "dstk_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_108_capitulation_signal},
    "dstk_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_109_capitulation_signal},
    "dstk_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_110_capitulation_signal},
    "dstk_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_111_capitulation_signal},
    "dstk_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_112_capitulation_signal},
    "dstk_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_113_capitulation_signal},
    "dstk_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_114_capitulation_signal},
    "dstk_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_115_capitulation_signal},
    "dstk_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_116_capitulation_signal},
    "dstk_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_117_capitulation_signal},
    "dstk_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_118_capitulation_signal},
    "dstk_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_119_capitulation_signal},
    "dstk_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_120_capitulation_signal},
    "dstk_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_121_capitulation_signal},
    "dstk_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_122_capitulation_signal},
    "dstk_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_123_capitulation_signal},
    "dstk_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_124_capitulation_signal},
    "dstk_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_125_capitulation_signal},
    "dstk_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_126_capitulation_signal},
    "dstk_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_127_capitulation_signal},
    "dstk_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_128_capitulation_signal},
    "dstk_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_129_capitulation_signal},
    "dstk_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_130_capitulation_signal},
    "dstk_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_131_capitulation_signal},
    "dstk_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_132_capitulation_signal},
    "dstk_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_133_capitulation_signal},
    "dstk_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_134_capitulation_signal},
    "dstk_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_135_capitulation_signal},
    "dstk_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_136_capitulation_signal},
    "dstk_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_137_capitulation_signal},
    "dstk_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_138_capitulation_signal},
    "dstk_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_139_capitulation_signal},
    "dstk_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_140_capitulation_signal},
    "dstk_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_141_capitulation_signal},
    "dstk_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_142_capitulation_signal},
    "dstk_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_143_capitulation_signal},
    "dstk_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_144_capitulation_signal},
    "dstk_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_145_capitulation_signal},
    "dstk_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_146_capitulation_signal},
    "dstk_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_147_capitulation_signal},
    "dstk_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_148_capitulation_signal},
    "dstk_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_149_capitulation_signal},
    "dstk_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_150_capitulation_signal},
}
