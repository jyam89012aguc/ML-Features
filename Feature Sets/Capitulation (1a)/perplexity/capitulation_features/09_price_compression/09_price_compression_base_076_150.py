"""Generated capitulation features for 09_price_compression: price range narrowing near the low.
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

def pcmp_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def pcmp_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def pcmp_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def pcmp_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def pcmp_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def pcmp_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def pcmp_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def pcmp_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def pcmp_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def pcmp_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def pcmp_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def pcmp_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def pcmp_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def pcmp_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def pcmp_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def pcmp_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def pcmp_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def pcmp_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def pcmp_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def pcmp_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def pcmp_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def pcmp_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def pcmp_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def pcmp_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def pcmp_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def pcmp_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def pcmp_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def pcmp_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def pcmp_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def pcmp_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def pcmp_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def pcmp_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def pcmp_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def pcmp_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def pcmp_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def pcmp_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def pcmp_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def pcmp_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def pcmp_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def pcmp_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def pcmp_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def pcmp_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def pcmp_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def pcmp_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def pcmp_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def pcmp_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def pcmp_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def pcmp_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def pcmp_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def pcmp_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def pcmp_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def pcmp_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def pcmp_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def pcmp_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def pcmp_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def pcmp_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def pcmp_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def pcmp_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def pcmp_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

PRICE_COMPRESSION_REGISTRY_076_150 = {
    "pcmp_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_076_capitulation_signal},
    "pcmp_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_077_capitulation_signal},
    "pcmp_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_078_capitulation_signal},
    "pcmp_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_079_capitulation_signal},
    "pcmp_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_080_capitulation_signal},
    "pcmp_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_081_capitulation_signal},
    "pcmp_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_082_capitulation_signal},
    "pcmp_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_083_capitulation_signal},
    "pcmp_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_084_capitulation_signal},
    "pcmp_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_085_capitulation_signal},
    "pcmp_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_086_capitulation_signal},
    "pcmp_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_087_capitulation_signal},
    "pcmp_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_088_capitulation_signal},
    "pcmp_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_089_capitulation_signal},
    "pcmp_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_090_capitulation_signal},
    "pcmp_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_091_capitulation_signal},
    "pcmp_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_092_capitulation_signal},
    "pcmp_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_093_capitulation_signal},
    "pcmp_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_094_capitulation_signal},
    "pcmp_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_095_capitulation_signal},
    "pcmp_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_096_capitulation_signal},
    "pcmp_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_097_capitulation_signal},
    "pcmp_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_098_capitulation_signal},
    "pcmp_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_099_capitulation_signal},
    "pcmp_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_100_capitulation_signal},
    "pcmp_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_101_capitulation_signal},
    "pcmp_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_102_capitulation_signal},
    "pcmp_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_103_capitulation_signal},
    "pcmp_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_104_capitulation_signal},
    "pcmp_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_105_capitulation_signal},
    "pcmp_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_106_capitulation_signal},
    "pcmp_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_107_capitulation_signal},
    "pcmp_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_108_capitulation_signal},
    "pcmp_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_109_capitulation_signal},
    "pcmp_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_110_capitulation_signal},
    "pcmp_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_111_capitulation_signal},
    "pcmp_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_112_capitulation_signal},
    "pcmp_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_113_capitulation_signal},
    "pcmp_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_114_capitulation_signal},
    "pcmp_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_115_capitulation_signal},
    "pcmp_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_116_capitulation_signal},
    "pcmp_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_117_capitulation_signal},
    "pcmp_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_118_capitulation_signal},
    "pcmp_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_119_capitulation_signal},
    "pcmp_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_120_capitulation_signal},
    "pcmp_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_121_capitulation_signal},
    "pcmp_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_122_capitulation_signal},
    "pcmp_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_123_capitulation_signal},
    "pcmp_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_124_capitulation_signal},
    "pcmp_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_125_capitulation_signal},
    "pcmp_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_126_capitulation_signal},
    "pcmp_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_127_capitulation_signal},
    "pcmp_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_128_capitulation_signal},
    "pcmp_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_129_capitulation_signal},
    "pcmp_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_130_capitulation_signal},
    "pcmp_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_131_capitulation_signal},
    "pcmp_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_132_capitulation_signal},
    "pcmp_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_133_capitulation_signal},
    "pcmp_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_134_capitulation_signal},
    "pcmp_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_135_capitulation_signal},
    "pcmp_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_136_capitulation_signal},
    "pcmp_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_137_capitulation_signal},
    "pcmp_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_138_capitulation_signal},
    "pcmp_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_139_capitulation_signal},
    "pcmp_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_140_capitulation_signal},
    "pcmp_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_141_capitulation_signal},
    "pcmp_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_142_capitulation_signal},
    "pcmp_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_143_capitulation_signal},
    "pcmp_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_144_capitulation_signal},
    "pcmp_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_145_capitulation_signal},
    "pcmp_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_146_capitulation_signal},
    "pcmp_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_147_capitulation_signal},
    "pcmp_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_148_capitulation_signal},
    "pcmp_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_149_capitulation_signal},
    "pcmp_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_150_capitulation_signal},
}
