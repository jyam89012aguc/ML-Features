"""Generated capitulation features for 11_decline_path_entropy: smooth-vs-jagged structure.
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

def dpe_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dpe_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dpe_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dpe_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dpe_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dpe_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dpe_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dpe_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dpe_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dpe_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dpe_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dpe_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dpe_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dpe_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dpe_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dpe_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dpe_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dpe_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dpe_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dpe_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dpe_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dpe_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dpe_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dpe_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dpe_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dpe_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dpe_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dpe_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dpe_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dpe_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dpe_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dpe_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dpe_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dpe_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dpe_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dpe_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dpe_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dpe_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dpe_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dpe_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dpe_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dpe_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dpe_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dpe_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dpe_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dpe_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dpe_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dpe_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dpe_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dpe_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dpe_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dpe_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dpe_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dpe_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dpe_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dpe_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dpe_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dpe_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dpe_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DECLINE_PATH_ENTROPY_REGISTRY_076_150 = {
    "dpe_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_076_capitulation_signal},
    "dpe_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_077_capitulation_signal},
    "dpe_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_078_capitulation_signal},
    "dpe_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_079_capitulation_signal},
    "dpe_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_080_capitulation_signal},
    "dpe_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_081_capitulation_signal},
    "dpe_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_082_capitulation_signal},
    "dpe_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_083_capitulation_signal},
    "dpe_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_084_capitulation_signal},
    "dpe_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_085_capitulation_signal},
    "dpe_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_086_capitulation_signal},
    "dpe_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_087_capitulation_signal},
    "dpe_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_088_capitulation_signal},
    "dpe_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_089_capitulation_signal},
    "dpe_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_090_capitulation_signal},
    "dpe_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_091_capitulation_signal},
    "dpe_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_092_capitulation_signal},
    "dpe_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_093_capitulation_signal},
    "dpe_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_094_capitulation_signal},
    "dpe_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_095_capitulation_signal},
    "dpe_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_096_capitulation_signal},
    "dpe_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_097_capitulation_signal},
    "dpe_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_098_capitulation_signal},
    "dpe_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_099_capitulation_signal},
    "dpe_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_100_capitulation_signal},
    "dpe_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_101_capitulation_signal},
    "dpe_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_102_capitulation_signal},
    "dpe_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_103_capitulation_signal},
    "dpe_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_104_capitulation_signal},
    "dpe_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_105_capitulation_signal},
    "dpe_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_106_capitulation_signal},
    "dpe_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_107_capitulation_signal},
    "dpe_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_108_capitulation_signal},
    "dpe_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_109_capitulation_signal},
    "dpe_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_110_capitulation_signal},
    "dpe_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_111_capitulation_signal},
    "dpe_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_112_capitulation_signal},
    "dpe_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_113_capitulation_signal},
    "dpe_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_114_capitulation_signal},
    "dpe_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_115_capitulation_signal},
    "dpe_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_116_capitulation_signal},
    "dpe_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_117_capitulation_signal},
    "dpe_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_118_capitulation_signal},
    "dpe_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_119_capitulation_signal},
    "dpe_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_120_capitulation_signal},
    "dpe_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_121_capitulation_signal},
    "dpe_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_122_capitulation_signal},
    "dpe_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_123_capitulation_signal},
    "dpe_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_124_capitulation_signal},
    "dpe_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_125_capitulation_signal},
    "dpe_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_126_capitulation_signal},
    "dpe_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_127_capitulation_signal},
    "dpe_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_128_capitulation_signal},
    "dpe_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_129_capitulation_signal},
    "dpe_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_130_capitulation_signal},
    "dpe_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_131_capitulation_signal},
    "dpe_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_132_capitulation_signal},
    "dpe_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_133_capitulation_signal},
    "dpe_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_134_capitulation_signal},
    "dpe_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_135_capitulation_signal},
    "dpe_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_136_capitulation_signal},
    "dpe_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_137_capitulation_signal},
    "dpe_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_138_capitulation_signal},
    "dpe_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_139_capitulation_signal},
    "dpe_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_140_capitulation_signal},
    "dpe_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_141_capitulation_signal},
    "dpe_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_142_capitulation_signal},
    "dpe_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_143_capitulation_signal},
    "dpe_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_144_capitulation_signal},
    "dpe_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_145_capitulation_signal},
    "dpe_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_146_capitulation_signal},
    "dpe_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_147_capitulation_signal},
    "dpe_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_148_capitulation_signal},
    "dpe_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_149_capitulation_signal},
    "dpe_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_150_capitulation_signal},
}
