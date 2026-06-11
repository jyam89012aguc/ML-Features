"""Generated capitulation features for 47_gap_down_clustering: clustered down gaps.
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

def gdc_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def gdc_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def gdc_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def gdc_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def gdc_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def gdc_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def gdc_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def gdc_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def gdc_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def gdc_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def gdc_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def gdc_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def gdc_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def gdc_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def gdc_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def gdc_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def gdc_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def gdc_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def gdc_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def gdc_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def gdc_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def gdc_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def gdc_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def gdc_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def gdc_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def gdc_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def gdc_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def gdc_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def gdc_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def gdc_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def gdc_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def gdc_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def gdc_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def gdc_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def gdc_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def gdc_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def gdc_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def gdc_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def gdc_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def gdc_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def gdc_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def gdc_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def gdc_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def gdc_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def gdc_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def gdc_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def gdc_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def gdc_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def gdc_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def gdc_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def gdc_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def gdc_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def gdc_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def gdc_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def gdc_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def gdc_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def gdc_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def gdc_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def gdc_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

GAP_DOWN_CLUSTERING_REGISTRY_076_150 = {
    "gdc_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_076_capitulation_signal},
    "gdc_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_077_capitulation_signal},
    "gdc_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_078_capitulation_signal},
    "gdc_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_079_capitulation_signal},
    "gdc_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_080_capitulation_signal},
    "gdc_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_081_capitulation_signal},
    "gdc_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_082_capitulation_signal},
    "gdc_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_083_capitulation_signal},
    "gdc_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_084_capitulation_signal},
    "gdc_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_085_capitulation_signal},
    "gdc_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_086_capitulation_signal},
    "gdc_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_087_capitulation_signal},
    "gdc_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_088_capitulation_signal},
    "gdc_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_089_capitulation_signal},
    "gdc_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_090_capitulation_signal},
    "gdc_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_091_capitulation_signal},
    "gdc_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_092_capitulation_signal},
    "gdc_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_093_capitulation_signal},
    "gdc_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_094_capitulation_signal},
    "gdc_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_095_capitulation_signal},
    "gdc_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_096_capitulation_signal},
    "gdc_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_097_capitulation_signal},
    "gdc_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_098_capitulation_signal},
    "gdc_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_099_capitulation_signal},
    "gdc_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_100_capitulation_signal},
    "gdc_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_101_capitulation_signal},
    "gdc_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_102_capitulation_signal},
    "gdc_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_103_capitulation_signal},
    "gdc_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_104_capitulation_signal},
    "gdc_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_105_capitulation_signal},
    "gdc_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_106_capitulation_signal},
    "gdc_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_107_capitulation_signal},
    "gdc_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_108_capitulation_signal},
    "gdc_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_109_capitulation_signal},
    "gdc_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_110_capitulation_signal},
    "gdc_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_111_capitulation_signal},
    "gdc_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_112_capitulation_signal},
    "gdc_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_113_capitulation_signal},
    "gdc_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_114_capitulation_signal},
    "gdc_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_115_capitulation_signal},
    "gdc_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_116_capitulation_signal},
    "gdc_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_117_capitulation_signal},
    "gdc_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_118_capitulation_signal},
    "gdc_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_119_capitulation_signal},
    "gdc_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_120_capitulation_signal},
    "gdc_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_121_capitulation_signal},
    "gdc_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_122_capitulation_signal},
    "gdc_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_123_capitulation_signal},
    "gdc_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_124_capitulation_signal},
    "gdc_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_125_capitulation_signal},
    "gdc_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_126_capitulation_signal},
    "gdc_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_127_capitulation_signal},
    "gdc_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_128_capitulation_signal},
    "gdc_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_129_capitulation_signal},
    "gdc_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_130_capitulation_signal},
    "gdc_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_131_capitulation_signal},
    "gdc_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_132_capitulation_signal},
    "gdc_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_133_capitulation_signal},
    "gdc_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_134_capitulation_signal},
    "gdc_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_135_capitulation_signal},
    "gdc_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_136_capitulation_signal},
    "gdc_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_137_capitulation_signal},
    "gdc_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_138_capitulation_signal},
    "gdc_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_139_capitulation_signal},
    "gdc_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_140_capitulation_signal},
    "gdc_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_141_capitulation_signal},
    "gdc_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_142_capitulation_signal},
    "gdc_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_143_capitulation_signal},
    "gdc_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_144_capitulation_signal},
    "gdc_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_145_capitulation_signal},
    "gdc_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_146_capitulation_signal},
    "gdc_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_147_capitulation_signal},
    "gdc_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_148_capitulation_signal},
    "gdc_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_149_capitulation_signal},
    "gdc_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_150_capitulation_signal},
}
