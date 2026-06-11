"""Generated capitulation features for 32_momentum_divergence: price new low without momentum new low.
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

def mdv_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def mdv_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def mdv_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def mdv_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def mdv_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def mdv_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def mdv_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def mdv_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def mdv_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def mdv_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def mdv_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def mdv_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def mdv_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def mdv_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def mdv_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def mdv_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mdv_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def mdv_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def mdv_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def mdv_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def mdv_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def mdv_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def mdv_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def mdv_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def mdv_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def mdv_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def mdv_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def mdv_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def mdv_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def mdv_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mdv_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def mdv_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def mdv_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def mdv_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def mdv_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def mdv_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def mdv_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def mdv_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def mdv_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def mdv_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def mdv_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def mdv_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def mdv_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def mdv_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mdv_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def mdv_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def mdv_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def mdv_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def mdv_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def mdv_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def mdv_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def mdv_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def mdv_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def mdv_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def mdv_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def mdv_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def mdv_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def mdv_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mdv_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

MOMENTUM_DIVERGENCE_REGISTRY_076_150 = {
    "mdv_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_076_capitulation_signal},
    "mdv_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_077_capitulation_signal},
    "mdv_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_078_capitulation_signal},
    "mdv_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_079_capitulation_signal},
    "mdv_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_080_capitulation_signal},
    "mdv_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_081_capitulation_signal},
    "mdv_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_082_capitulation_signal},
    "mdv_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_083_capitulation_signal},
    "mdv_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_084_capitulation_signal},
    "mdv_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_085_capitulation_signal},
    "mdv_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_086_capitulation_signal},
    "mdv_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_087_capitulation_signal},
    "mdv_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_088_capitulation_signal},
    "mdv_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_089_capitulation_signal},
    "mdv_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_090_capitulation_signal},
    "mdv_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_091_capitulation_signal},
    "mdv_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_092_capitulation_signal},
    "mdv_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_093_capitulation_signal},
    "mdv_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_094_capitulation_signal},
    "mdv_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_095_capitulation_signal},
    "mdv_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_096_capitulation_signal},
    "mdv_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_097_capitulation_signal},
    "mdv_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_098_capitulation_signal},
    "mdv_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_099_capitulation_signal},
    "mdv_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_100_capitulation_signal},
    "mdv_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_101_capitulation_signal},
    "mdv_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_102_capitulation_signal},
    "mdv_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_103_capitulation_signal},
    "mdv_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_104_capitulation_signal},
    "mdv_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_105_capitulation_signal},
    "mdv_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_106_capitulation_signal},
    "mdv_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_107_capitulation_signal},
    "mdv_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_108_capitulation_signal},
    "mdv_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_109_capitulation_signal},
    "mdv_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_110_capitulation_signal},
    "mdv_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_111_capitulation_signal},
    "mdv_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_112_capitulation_signal},
    "mdv_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_113_capitulation_signal},
    "mdv_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_114_capitulation_signal},
    "mdv_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_115_capitulation_signal},
    "mdv_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_116_capitulation_signal},
    "mdv_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_117_capitulation_signal},
    "mdv_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_118_capitulation_signal},
    "mdv_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_119_capitulation_signal},
    "mdv_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_120_capitulation_signal},
    "mdv_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_121_capitulation_signal},
    "mdv_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_122_capitulation_signal},
    "mdv_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_123_capitulation_signal},
    "mdv_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_124_capitulation_signal},
    "mdv_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_125_capitulation_signal},
    "mdv_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_126_capitulation_signal},
    "mdv_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_127_capitulation_signal},
    "mdv_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_128_capitulation_signal},
    "mdv_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_129_capitulation_signal},
    "mdv_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_130_capitulation_signal},
    "mdv_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_131_capitulation_signal},
    "mdv_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_132_capitulation_signal},
    "mdv_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_133_capitulation_signal},
    "mdv_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_134_capitulation_signal},
    "mdv_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_135_capitulation_signal},
    "mdv_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_136_capitulation_signal},
    "mdv_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_137_capitulation_signal},
    "mdv_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_138_capitulation_signal},
    "mdv_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_139_capitulation_signal},
    "mdv_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_140_capitulation_signal},
    "mdv_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_141_capitulation_signal},
    "mdv_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_142_capitulation_signal},
    "mdv_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_143_capitulation_signal},
    "mdv_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_144_capitulation_signal},
    "mdv_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_145_capitulation_signal},
    "mdv_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_146_capitulation_signal},
    "mdv_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_147_capitulation_signal},
    "mdv_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_148_capitulation_signal},
    "mdv_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_149_capitulation_signal},
    "mdv_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_150_capitulation_signal},
}
