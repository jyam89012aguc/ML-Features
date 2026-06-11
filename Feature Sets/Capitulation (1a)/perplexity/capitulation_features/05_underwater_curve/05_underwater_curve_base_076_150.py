"""Generated capitulation features for 05_underwater_curve: area/depth of underwater equity curve.
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

def uw_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def uw_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def uw_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def uw_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def uw_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def uw_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def uw_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def uw_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def uw_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def uw_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def uw_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def uw_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def uw_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def uw_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def uw_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def uw_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def uw_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def uw_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def uw_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def uw_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def uw_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def uw_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def uw_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def uw_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def uw_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def uw_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def uw_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def uw_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def uw_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def uw_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def uw_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def uw_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def uw_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def uw_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def uw_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def uw_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def uw_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def uw_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def uw_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def uw_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def uw_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def uw_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def uw_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def uw_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def uw_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def uw_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def uw_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def uw_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def uw_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def uw_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def uw_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def uw_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def uw_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def uw_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def uw_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def uw_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def uw_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def uw_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def uw_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

UNDERWATER_CURVE_REGISTRY_076_150 = {
    "uw_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_076_capitulation_signal},
    "uw_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_077_capitulation_signal},
    "uw_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_078_capitulation_signal},
    "uw_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_079_capitulation_signal},
    "uw_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_080_capitulation_signal},
    "uw_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_081_capitulation_signal},
    "uw_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_082_capitulation_signal},
    "uw_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_083_capitulation_signal},
    "uw_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_084_capitulation_signal},
    "uw_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_085_capitulation_signal},
    "uw_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_086_capitulation_signal},
    "uw_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_087_capitulation_signal},
    "uw_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_088_capitulation_signal},
    "uw_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_089_capitulation_signal},
    "uw_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_090_capitulation_signal},
    "uw_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_091_capitulation_signal},
    "uw_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_092_capitulation_signal},
    "uw_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_093_capitulation_signal},
    "uw_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_094_capitulation_signal},
    "uw_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_095_capitulation_signal},
    "uw_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_096_capitulation_signal},
    "uw_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_097_capitulation_signal},
    "uw_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_098_capitulation_signal},
    "uw_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_099_capitulation_signal},
    "uw_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_100_capitulation_signal},
    "uw_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_101_capitulation_signal},
    "uw_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_102_capitulation_signal},
    "uw_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_103_capitulation_signal},
    "uw_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_104_capitulation_signal},
    "uw_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_105_capitulation_signal},
    "uw_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_106_capitulation_signal},
    "uw_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_107_capitulation_signal},
    "uw_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_108_capitulation_signal},
    "uw_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_109_capitulation_signal},
    "uw_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_110_capitulation_signal},
    "uw_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_111_capitulation_signal},
    "uw_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_112_capitulation_signal},
    "uw_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_113_capitulation_signal},
    "uw_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_114_capitulation_signal},
    "uw_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_115_capitulation_signal},
    "uw_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_116_capitulation_signal},
    "uw_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_117_capitulation_signal},
    "uw_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_118_capitulation_signal},
    "uw_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_119_capitulation_signal},
    "uw_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_120_capitulation_signal},
    "uw_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_121_capitulation_signal},
    "uw_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_122_capitulation_signal},
    "uw_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_123_capitulation_signal},
    "uw_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_124_capitulation_signal},
    "uw_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_125_capitulation_signal},
    "uw_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_126_capitulation_signal},
    "uw_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_127_capitulation_signal},
    "uw_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_128_capitulation_signal},
    "uw_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_129_capitulation_signal},
    "uw_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_130_capitulation_signal},
    "uw_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_131_capitulation_signal},
    "uw_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_132_capitulation_signal},
    "uw_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_133_capitulation_signal},
    "uw_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_134_capitulation_signal},
    "uw_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_135_capitulation_signal},
    "uw_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_136_capitulation_signal},
    "uw_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_137_capitulation_signal},
    "uw_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_138_capitulation_signal},
    "uw_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_139_capitulation_signal},
    "uw_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_140_capitulation_signal},
    "uw_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_141_capitulation_signal},
    "uw_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_142_capitulation_signal},
    "uw_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_143_capitulation_signal},
    "uw_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_144_capitulation_signal},
    "uw_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_145_capitulation_signal},
    "uw_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_146_capitulation_signal},
    "uw_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_147_capitulation_signal},
    "uw_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_148_capitulation_signal},
    "uw_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_149_capitulation_signal},
    "uw_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_150_capitulation_signal},
}
