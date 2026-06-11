"""Generated capitulation features for 14_recovery_failure: failed bounces, lower-highs.
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

def rfl_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rfl_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rfl_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rfl_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rfl_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rfl_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rfl_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rfl_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rfl_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rfl_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rfl_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rfl_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rfl_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rfl_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rfl_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rfl_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rfl_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rfl_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rfl_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rfl_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rfl_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rfl_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rfl_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rfl_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rfl_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rfl_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rfl_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rfl_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rfl_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rfl_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rfl_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rfl_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rfl_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rfl_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rfl_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rfl_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rfl_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rfl_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rfl_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rfl_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rfl_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rfl_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rfl_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rfl_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rfl_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rfl_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rfl_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rfl_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rfl_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rfl_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rfl_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rfl_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rfl_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rfl_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rfl_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rfl_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rfl_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rfl_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rfl_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

RECOVERY_FAILURE_REGISTRY_076_150 = {
    "rfl_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_076_capitulation_signal},
    "rfl_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_077_capitulation_signal},
    "rfl_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_078_capitulation_signal},
    "rfl_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_079_capitulation_signal},
    "rfl_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_080_capitulation_signal},
    "rfl_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_081_capitulation_signal},
    "rfl_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_082_capitulation_signal},
    "rfl_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_083_capitulation_signal},
    "rfl_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_084_capitulation_signal},
    "rfl_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_085_capitulation_signal},
    "rfl_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_086_capitulation_signal},
    "rfl_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_087_capitulation_signal},
    "rfl_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_088_capitulation_signal},
    "rfl_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_089_capitulation_signal},
    "rfl_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_090_capitulation_signal},
    "rfl_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_091_capitulation_signal},
    "rfl_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_092_capitulation_signal},
    "rfl_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_093_capitulation_signal},
    "rfl_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_094_capitulation_signal},
    "rfl_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_095_capitulation_signal},
    "rfl_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_096_capitulation_signal},
    "rfl_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_097_capitulation_signal},
    "rfl_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_098_capitulation_signal},
    "rfl_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_099_capitulation_signal},
    "rfl_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_100_capitulation_signal},
    "rfl_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_101_capitulation_signal},
    "rfl_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_102_capitulation_signal},
    "rfl_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_103_capitulation_signal},
    "rfl_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_104_capitulation_signal},
    "rfl_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_105_capitulation_signal},
    "rfl_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_106_capitulation_signal},
    "rfl_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_107_capitulation_signal},
    "rfl_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_108_capitulation_signal},
    "rfl_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_109_capitulation_signal},
    "rfl_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_110_capitulation_signal},
    "rfl_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_111_capitulation_signal},
    "rfl_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_112_capitulation_signal},
    "rfl_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_113_capitulation_signal},
    "rfl_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_114_capitulation_signal},
    "rfl_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_115_capitulation_signal},
    "rfl_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_116_capitulation_signal},
    "rfl_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_117_capitulation_signal},
    "rfl_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_118_capitulation_signal},
    "rfl_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_119_capitulation_signal},
    "rfl_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_120_capitulation_signal},
    "rfl_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_121_capitulation_signal},
    "rfl_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_122_capitulation_signal},
    "rfl_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_123_capitulation_signal},
    "rfl_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_124_capitulation_signal},
    "rfl_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_125_capitulation_signal},
    "rfl_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_126_capitulation_signal},
    "rfl_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_127_capitulation_signal},
    "rfl_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_128_capitulation_signal},
    "rfl_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_129_capitulation_signal},
    "rfl_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_130_capitulation_signal},
    "rfl_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_131_capitulation_signal},
    "rfl_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_132_capitulation_signal},
    "rfl_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_133_capitulation_signal},
    "rfl_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_134_capitulation_signal},
    "rfl_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_135_capitulation_signal},
    "rfl_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_136_capitulation_signal},
    "rfl_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_137_capitulation_signal},
    "rfl_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_138_capitulation_signal},
    "rfl_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_139_capitulation_signal},
    "rfl_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_140_capitulation_signal},
    "rfl_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_141_capitulation_signal},
    "rfl_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_142_capitulation_signal},
    "rfl_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_143_capitulation_signal},
    "rfl_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_144_capitulation_signal},
    "rfl_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_145_capitulation_signal},
    "rfl_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_146_capitulation_signal},
    "rfl_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_147_capitulation_signal},
    "rfl_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_148_capitulation_signal},
    "rfl_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_149_capitulation_signal},
    "rfl_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_150_capitulation_signal},
}
