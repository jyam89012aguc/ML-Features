"""Generated capitulation features for 01_drawdown_depth: decline magnitude vs trailing highs.
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

def dd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DRAWDOWN_DEPTH_REGISTRY_076_150 = {
    "dd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_076_capitulation_signal},
    "dd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_077_capitulation_signal},
    "dd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_078_capitulation_signal},
    "dd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_079_capitulation_signal},
    "dd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_080_capitulation_signal},
    "dd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_081_capitulation_signal},
    "dd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_082_capitulation_signal},
    "dd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_083_capitulation_signal},
    "dd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_084_capitulation_signal},
    "dd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_085_capitulation_signal},
    "dd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_086_capitulation_signal},
    "dd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_087_capitulation_signal},
    "dd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_088_capitulation_signal},
    "dd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_089_capitulation_signal},
    "dd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_090_capitulation_signal},
    "dd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_091_capitulation_signal},
    "dd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_092_capitulation_signal},
    "dd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_093_capitulation_signal},
    "dd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_094_capitulation_signal},
    "dd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_095_capitulation_signal},
    "dd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_096_capitulation_signal},
    "dd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_097_capitulation_signal},
    "dd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_098_capitulation_signal},
    "dd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_099_capitulation_signal},
    "dd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_100_capitulation_signal},
    "dd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_101_capitulation_signal},
    "dd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_102_capitulation_signal},
    "dd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_103_capitulation_signal},
    "dd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_104_capitulation_signal},
    "dd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_105_capitulation_signal},
    "dd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_106_capitulation_signal},
    "dd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_107_capitulation_signal},
    "dd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_108_capitulation_signal},
    "dd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_109_capitulation_signal},
    "dd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_110_capitulation_signal},
    "dd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_111_capitulation_signal},
    "dd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_112_capitulation_signal},
    "dd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_113_capitulation_signal},
    "dd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_114_capitulation_signal},
    "dd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_115_capitulation_signal},
    "dd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_116_capitulation_signal},
    "dd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_117_capitulation_signal},
    "dd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_118_capitulation_signal},
    "dd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_119_capitulation_signal},
    "dd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_120_capitulation_signal},
    "dd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_121_capitulation_signal},
    "dd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_122_capitulation_signal},
    "dd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_123_capitulation_signal},
    "dd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_124_capitulation_signal},
    "dd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_125_capitulation_signal},
    "dd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_126_capitulation_signal},
    "dd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_127_capitulation_signal},
    "dd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_128_capitulation_signal},
    "dd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_129_capitulation_signal},
    "dd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_130_capitulation_signal},
    "dd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_131_capitulation_signal},
    "dd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_132_capitulation_signal},
    "dd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_133_capitulation_signal},
    "dd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_134_capitulation_signal},
    "dd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_135_capitulation_signal},
    "dd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_136_capitulation_signal},
    "dd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_137_capitulation_signal},
    "dd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_138_capitulation_signal},
    "dd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_139_capitulation_signal},
    "dd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_140_capitulation_signal},
    "dd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_141_capitulation_signal},
    "dd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_142_capitulation_signal},
    "dd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_143_capitulation_signal},
    "dd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_144_capitulation_signal},
    "dd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_145_capitulation_signal},
    "dd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_146_capitulation_signal},
    "dd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_147_capitulation_signal},
    "dd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_148_capitulation_signal},
    "dd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_149_capitulation_signal},
    "dd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_150_capitulation_signal},
}
