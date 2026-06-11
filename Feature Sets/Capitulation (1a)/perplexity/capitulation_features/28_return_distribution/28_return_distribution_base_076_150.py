"""Generated capitulation features for 28_return_distribution: return distribution tails.
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

def rds_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rds_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rds_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rds_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rds_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rds_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rds_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rds_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rds_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rds_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rds_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rds_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rds_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rds_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rds_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rds_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rds_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rds_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rds_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rds_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rds_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rds_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rds_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rds_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rds_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rds_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rds_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rds_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rds_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rds_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rds_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rds_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rds_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rds_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rds_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rds_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rds_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rds_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rds_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rds_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rds_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rds_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rds_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rds_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rds_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rds_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rds_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rds_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rds_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rds_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rds_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rds_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rds_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rds_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rds_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rds_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rds_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rds_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rds_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rds_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rds_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rds_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rds_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rds_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rds_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rds_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rds_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rds_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

RETURN_DISTRIBUTION_REGISTRY_076_150 = {
    "rds_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_076_capitulation_signal},
    "rds_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_077_capitulation_signal},
    "rds_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_078_capitulation_signal},
    "rds_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_079_capitulation_signal},
    "rds_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_080_capitulation_signal},
    "rds_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_081_capitulation_signal},
    "rds_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_082_capitulation_signal},
    "rds_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_083_capitulation_signal},
    "rds_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_084_capitulation_signal},
    "rds_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_085_capitulation_signal},
    "rds_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_086_capitulation_signal},
    "rds_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_087_capitulation_signal},
    "rds_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_088_capitulation_signal},
    "rds_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_089_capitulation_signal},
    "rds_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_090_capitulation_signal},
    "rds_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_091_capitulation_signal},
    "rds_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_092_capitulation_signal},
    "rds_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_093_capitulation_signal},
    "rds_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_094_capitulation_signal},
    "rds_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_095_capitulation_signal},
    "rds_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_096_capitulation_signal},
    "rds_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_097_capitulation_signal},
    "rds_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_098_capitulation_signal},
    "rds_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_099_capitulation_signal},
    "rds_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_100_capitulation_signal},
    "rds_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_101_capitulation_signal},
    "rds_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_102_capitulation_signal},
    "rds_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_103_capitulation_signal},
    "rds_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_104_capitulation_signal},
    "rds_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_105_capitulation_signal},
    "rds_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_106_capitulation_signal},
    "rds_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_107_capitulation_signal},
    "rds_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_108_capitulation_signal},
    "rds_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_109_capitulation_signal},
    "rds_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_110_capitulation_signal},
    "rds_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_111_capitulation_signal},
    "rds_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_112_capitulation_signal},
    "rds_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_113_capitulation_signal},
    "rds_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_114_capitulation_signal},
    "rds_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_115_capitulation_signal},
    "rds_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_116_capitulation_signal},
    "rds_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_117_capitulation_signal},
    "rds_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_118_capitulation_signal},
    "rds_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_119_capitulation_signal},
    "rds_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_120_capitulation_signal},
    "rds_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_121_capitulation_signal},
    "rds_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_122_capitulation_signal},
    "rds_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_123_capitulation_signal},
    "rds_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_124_capitulation_signal},
    "rds_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_125_capitulation_signal},
    "rds_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_126_capitulation_signal},
    "rds_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_127_capitulation_signal},
    "rds_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_128_capitulation_signal},
    "rds_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_129_capitulation_signal},
    "rds_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_130_capitulation_signal},
    "rds_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_131_capitulation_signal},
    "rds_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_132_capitulation_signal},
    "rds_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_133_capitulation_signal},
    "rds_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_134_capitulation_signal},
    "rds_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_135_capitulation_signal},
    "rds_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_136_capitulation_signal},
    "rds_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_137_capitulation_signal},
    "rds_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_138_capitulation_signal},
    "rds_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_139_capitulation_signal},
    "rds_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_140_capitulation_signal},
    "rds_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_141_capitulation_signal},
    "rds_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_142_capitulation_signal},
    "rds_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_143_capitulation_signal},
    "rds_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_144_capitulation_signal},
    "rds_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_145_capitulation_signal},
    "rds_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_146_capitulation_signal},
    "rds_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_147_capitulation_signal},
    "rds_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_148_capitulation_signal},
    "rds_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_149_capitulation_signal},
    "rds_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rds_150_capitulation_signal},
}
