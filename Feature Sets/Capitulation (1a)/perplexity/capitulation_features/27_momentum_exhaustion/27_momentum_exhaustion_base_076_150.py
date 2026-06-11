"""Generated capitulation features for 27_momentum_exhaustion: loss of downside momentum.
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

def mex_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def mex_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def mex_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mex_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def mex_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def mex_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def mex_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def mex_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def mex_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def mex_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def mex_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def mex_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mex_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def mex_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def mex_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def mex_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def mex_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def mex_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mex_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mex_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def mex_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def mex_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def mex_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def mex_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def mex_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def mex_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def mex_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def mex_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mex_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def mex_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def mex_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def mex_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def mex_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def mex_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mex_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mex_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def mex_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def mex_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def mex_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def mex_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def mex_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def mex_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def mex_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def mex_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mex_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def mex_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def mex_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def mex_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def mex_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def mex_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mex_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mex_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def mex_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def mex_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def mex_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def mex_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def mex_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def mex_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def mex_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mex_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def mex_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mex_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def mex_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def mex_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def mex_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def mex_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def mex_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mex_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

MOMENTUM_EXHAUSTION_REGISTRY_076_150 = {
    "mex_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_076_capitulation_signal},
    "mex_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_077_capitulation_signal},
    "mex_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_078_capitulation_signal},
    "mex_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_079_capitulation_signal},
    "mex_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_080_capitulation_signal},
    "mex_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_081_capitulation_signal},
    "mex_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_082_capitulation_signal},
    "mex_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_083_capitulation_signal},
    "mex_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_084_capitulation_signal},
    "mex_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_085_capitulation_signal},
    "mex_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_086_capitulation_signal},
    "mex_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_087_capitulation_signal},
    "mex_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_088_capitulation_signal},
    "mex_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_089_capitulation_signal},
    "mex_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_090_capitulation_signal},
    "mex_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_091_capitulation_signal},
    "mex_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_092_capitulation_signal},
    "mex_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_093_capitulation_signal},
    "mex_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_094_capitulation_signal},
    "mex_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_095_capitulation_signal},
    "mex_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_096_capitulation_signal},
    "mex_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_097_capitulation_signal},
    "mex_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_098_capitulation_signal},
    "mex_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_099_capitulation_signal},
    "mex_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_100_capitulation_signal},
    "mex_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_101_capitulation_signal},
    "mex_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_102_capitulation_signal},
    "mex_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_103_capitulation_signal},
    "mex_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_104_capitulation_signal},
    "mex_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_105_capitulation_signal},
    "mex_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_106_capitulation_signal},
    "mex_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_107_capitulation_signal},
    "mex_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_108_capitulation_signal},
    "mex_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_109_capitulation_signal},
    "mex_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_110_capitulation_signal},
    "mex_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_111_capitulation_signal},
    "mex_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_112_capitulation_signal},
    "mex_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_113_capitulation_signal},
    "mex_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_114_capitulation_signal},
    "mex_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_115_capitulation_signal},
    "mex_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_116_capitulation_signal},
    "mex_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_117_capitulation_signal},
    "mex_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_118_capitulation_signal},
    "mex_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_119_capitulation_signal},
    "mex_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_120_capitulation_signal},
    "mex_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_121_capitulation_signal},
    "mex_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_122_capitulation_signal},
    "mex_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_123_capitulation_signal},
    "mex_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_124_capitulation_signal},
    "mex_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_125_capitulation_signal},
    "mex_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_126_capitulation_signal},
    "mex_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_127_capitulation_signal},
    "mex_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_128_capitulation_signal},
    "mex_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_129_capitulation_signal},
    "mex_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_130_capitulation_signal},
    "mex_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_131_capitulation_signal},
    "mex_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_132_capitulation_signal},
    "mex_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_133_capitulation_signal},
    "mex_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_134_capitulation_signal},
    "mex_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_135_capitulation_signal},
    "mex_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_136_capitulation_signal},
    "mex_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_137_capitulation_signal},
    "mex_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_138_capitulation_signal},
    "mex_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_139_capitulation_signal},
    "mex_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_140_capitulation_signal},
    "mex_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_141_capitulation_signal},
    "mex_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_142_capitulation_signal},
    "mex_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_143_capitulation_signal},
    "mex_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_144_capitulation_signal},
    "mex_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_145_capitulation_signal},
    "mex_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_146_capitulation_signal},
    "mex_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_147_capitulation_signal},
    "mex_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_148_capitulation_signal},
    "mex_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_149_capitulation_signal},
    "mex_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mex_150_capitulation_signal},
}
