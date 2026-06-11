"""Generated capitulation features for 39_intraday_range: high-low spread behavior.
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

def idr_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def idr_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def idr_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def idr_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def idr_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def idr_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def idr_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def idr_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def idr_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def idr_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def idr_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def idr_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def idr_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def idr_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def idr_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def idr_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def idr_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def idr_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def idr_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def idr_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def idr_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def idr_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def idr_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def idr_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def idr_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def idr_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def idr_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def idr_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def idr_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def idr_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def idr_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def idr_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def idr_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def idr_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def idr_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def idr_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def idr_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def idr_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def idr_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def idr_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def idr_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def idr_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def idr_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def idr_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def idr_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def idr_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def idr_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def idr_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def idr_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def idr_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def idr_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def idr_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def idr_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def idr_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def idr_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def idr_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def idr_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def idr_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def idr_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

INTRADAY_RANGE_REGISTRY_076_150 = {
    "idr_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_076_capitulation_signal},
    "idr_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_077_capitulation_signal},
    "idr_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_078_capitulation_signal},
    "idr_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_079_capitulation_signal},
    "idr_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_080_capitulation_signal},
    "idr_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_081_capitulation_signal},
    "idr_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_082_capitulation_signal},
    "idr_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_083_capitulation_signal},
    "idr_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_084_capitulation_signal},
    "idr_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_085_capitulation_signal},
    "idr_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_086_capitulation_signal},
    "idr_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_087_capitulation_signal},
    "idr_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_088_capitulation_signal},
    "idr_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_089_capitulation_signal},
    "idr_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_090_capitulation_signal},
    "idr_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_091_capitulation_signal},
    "idr_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_092_capitulation_signal},
    "idr_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_093_capitulation_signal},
    "idr_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_094_capitulation_signal},
    "idr_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_095_capitulation_signal},
    "idr_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_096_capitulation_signal},
    "idr_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_097_capitulation_signal},
    "idr_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_098_capitulation_signal},
    "idr_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_099_capitulation_signal},
    "idr_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_100_capitulation_signal},
    "idr_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_101_capitulation_signal},
    "idr_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_102_capitulation_signal},
    "idr_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_103_capitulation_signal},
    "idr_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_104_capitulation_signal},
    "idr_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_105_capitulation_signal},
    "idr_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_106_capitulation_signal},
    "idr_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_107_capitulation_signal},
    "idr_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_108_capitulation_signal},
    "idr_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_109_capitulation_signal},
    "idr_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_110_capitulation_signal},
    "idr_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_111_capitulation_signal},
    "idr_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_112_capitulation_signal},
    "idr_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_113_capitulation_signal},
    "idr_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_114_capitulation_signal},
    "idr_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_115_capitulation_signal},
    "idr_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_116_capitulation_signal},
    "idr_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_117_capitulation_signal},
    "idr_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_118_capitulation_signal},
    "idr_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_119_capitulation_signal},
    "idr_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_120_capitulation_signal},
    "idr_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_121_capitulation_signal},
    "idr_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_122_capitulation_signal},
    "idr_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_123_capitulation_signal},
    "idr_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_124_capitulation_signal},
    "idr_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_125_capitulation_signal},
    "idr_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_126_capitulation_signal},
    "idr_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_127_capitulation_signal},
    "idr_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_128_capitulation_signal},
    "idr_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_129_capitulation_signal},
    "idr_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_130_capitulation_signal},
    "idr_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_131_capitulation_signal},
    "idr_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_132_capitulation_signal},
    "idr_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_133_capitulation_signal},
    "idr_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_134_capitulation_signal},
    "idr_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_135_capitulation_signal},
    "idr_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_136_capitulation_signal},
    "idr_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_137_capitulation_signal},
    "idr_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_138_capitulation_signal},
    "idr_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_139_capitulation_signal},
    "idr_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_140_capitulation_signal},
    "idr_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_141_capitulation_signal},
    "idr_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_142_capitulation_signal},
    "idr_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_143_capitulation_signal},
    "idr_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_144_capitulation_signal},
    "idr_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_145_capitulation_signal},
    "idr_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_146_capitulation_signal},
    "idr_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_147_capitulation_signal},
    "idr_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_148_capitulation_signal},
    "idr_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_149_capitulation_signal},
    "idr_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_150_capitulation_signal},
}
