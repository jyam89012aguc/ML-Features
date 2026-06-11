"""Generated capitulation features for 41_range_compression: range collapse after expansion.
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

def rcp_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rcp_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rcp_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rcp_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rcp_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rcp_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rcp_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rcp_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rcp_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rcp_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rcp_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rcp_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rcp_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rcp_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rcp_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rcp_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rcp_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rcp_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rcp_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rcp_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rcp_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rcp_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rcp_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rcp_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rcp_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rcp_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rcp_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rcp_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rcp_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rcp_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rcp_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rcp_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rcp_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rcp_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rcp_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rcp_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rcp_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rcp_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rcp_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rcp_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rcp_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rcp_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rcp_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rcp_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rcp_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rcp_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rcp_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rcp_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rcp_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rcp_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rcp_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rcp_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rcp_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rcp_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rcp_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rcp_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rcp_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rcp_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rcp_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

RANGE_COMPRESSION_REGISTRY_076_150 = {
    "rcp_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_076_capitulation_signal},
    "rcp_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_077_capitulation_signal},
    "rcp_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_078_capitulation_signal},
    "rcp_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_079_capitulation_signal},
    "rcp_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_080_capitulation_signal},
    "rcp_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_081_capitulation_signal},
    "rcp_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_082_capitulation_signal},
    "rcp_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_083_capitulation_signal},
    "rcp_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_084_capitulation_signal},
    "rcp_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_085_capitulation_signal},
    "rcp_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_086_capitulation_signal},
    "rcp_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_087_capitulation_signal},
    "rcp_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_088_capitulation_signal},
    "rcp_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_089_capitulation_signal},
    "rcp_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_090_capitulation_signal},
    "rcp_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_091_capitulation_signal},
    "rcp_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_092_capitulation_signal},
    "rcp_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_093_capitulation_signal},
    "rcp_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_094_capitulation_signal},
    "rcp_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_095_capitulation_signal},
    "rcp_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_096_capitulation_signal},
    "rcp_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_097_capitulation_signal},
    "rcp_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_098_capitulation_signal},
    "rcp_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_099_capitulation_signal},
    "rcp_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_100_capitulation_signal},
    "rcp_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_101_capitulation_signal},
    "rcp_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_102_capitulation_signal},
    "rcp_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_103_capitulation_signal},
    "rcp_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_104_capitulation_signal},
    "rcp_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_105_capitulation_signal},
    "rcp_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_106_capitulation_signal},
    "rcp_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_107_capitulation_signal},
    "rcp_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_108_capitulation_signal},
    "rcp_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_109_capitulation_signal},
    "rcp_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_110_capitulation_signal},
    "rcp_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_111_capitulation_signal},
    "rcp_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_112_capitulation_signal},
    "rcp_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_113_capitulation_signal},
    "rcp_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_114_capitulation_signal},
    "rcp_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_115_capitulation_signal},
    "rcp_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_116_capitulation_signal},
    "rcp_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_117_capitulation_signal},
    "rcp_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_118_capitulation_signal},
    "rcp_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_119_capitulation_signal},
    "rcp_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_120_capitulation_signal},
    "rcp_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_121_capitulation_signal},
    "rcp_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_122_capitulation_signal},
    "rcp_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_123_capitulation_signal},
    "rcp_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_124_capitulation_signal},
    "rcp_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_125_capitulation_signal},
    "rcp_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_126_capitulation_signal},
    "rcp_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_127_capitulation_signal},
    "rcp_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_128_capitulation_signal},
    "rcp_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_129_capitulation_signal},
    "rcp_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_130_capitulation_signal},
    "rcp_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_131_capitulation_signal},
    "rcp_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_132_capitulation_signal},
    "rcp_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_133_capitulation_signal},
    "rcp_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_134_capitulation_signal},
    "rcp_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_135_capitulation_signal},
    "rcp_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_136_capitulation_signal},
    "rcp_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_137_capitulation_signal},
    "rcp_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_138_capitulation_signal},
    "rcp_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_139_capitulation_signal},
    "rcp_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_140_capitulation_signal},
    "rcp_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_141_capitulation_signal},
    "rcp_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_142_capitulation_signal},
    "rcp_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_143_capitulation_signal},
    "rcp_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_144_capitulation_signal},
    "rcp_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_145_capitulation_signal},
    "rcp_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_146_capitulation_signal},
    "rcp_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_147_capitulation_signal},
    "rcp_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_148_capitulation_signal},
    "rcp_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_149_capitulation_signal},
    "rcp_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_150_capitulation_signal},
}
