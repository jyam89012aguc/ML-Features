"""Generated capitulation features for 56_zero_volume_days: no-trade days.
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

def zvd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def zvd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def zvd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def zvd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def zvd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def zvd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def zvd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def zvd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def zvd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def zvd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def zvd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def zvd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def zvd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def zvd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def zvd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def zvd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def zvd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def zvd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def zvd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def zvd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def zvd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def zvd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def zvd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def zvd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def zvd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def zvd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def zvd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def zvd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def zvd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def zvd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def zvd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def zvd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def zvd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def zvd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def zvd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def zvd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def zvd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def zvd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def zvd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def zvd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def zvd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def zvd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def zvd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def zvd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def zvd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def zvd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def zvd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def zvd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def zvd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def zvd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def zvd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def zvd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def zvd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def zvd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def zvd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def zvd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def zvd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def zvd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def zvd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

ZERO_VOLUME_DAYS_REGISTRY_076_150 = {
    "zvd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_076_capitulation_signal},
    "zvd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_077_capitulation_signal},
    "zvd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_078_capitulation_signal},
    "zvd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_079_capitulation_signal},
    "zvd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_080_capitulation_signal},
    "zvd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_081_capitulation_signal},
    "zvd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_082_capitulation_signal},
    "zvd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_083_capitulation_signal},
    "zvd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_084_capitulation_signal},
    "zvd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_085_capitulation_signal},
    "zvd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_086_capitulation_signal},
    "zvd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_087_capitulation_signal},
    "zvd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_088_capitulation_signal},
    "zvd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_089_capitulation_signal},
    "zvd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_090_capitulation_signal},
    "zvd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_091_capitulation_signal},
    "zvd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_092_capitulation_signal},
    "zvd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_093_capitulation_signal},
    "zvd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_094_capitulation_signal},
    "zvd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_095_capitulation_signal},
    "zvd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_096_capitulation_signal},
    "zvd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_097_capitulation_signal},
    "zvd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_098_capitulation_signal},
    "zvd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_099_capitulation_signal},
    "zvd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_100_capitulation_signal},
    "zvd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_101_capitulation_signal},
    "zvd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_102_capitulation_signal},
    "zvd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_103_capitulation_signal},
    "zvd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_104_capitulation_signal},
    "zvd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_105_capitulation_signal},
    "zvd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_106_capitulation_signal},
    "zvd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_107_capitulation_signal},
    "zvd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_108_capitulation_signal},
    "zvd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_109_capitulation_signal},
    "zvd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_110_capitulation_signal},
    "zvd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_111_capitulation_signal},
    "zvd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_112_capitulation_signal},
    "zvd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_113_capitulation_signal},
    "zvd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_114_capitulation_signal},
    "zvd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_115_capitulation_signal},
    "zvd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_116_capitulation_signal},
    "zvd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_117_capitulation_signal},
    "zvd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_118_capitulation_signal},
    "zvd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_119_capitulation_signal},
    "zvd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_120_capitulation_signal},
    "zvd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_121_capitulation_signal},
    "zvd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_122_capitulation_signal},
    "zvd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_123_capitulation_signal},
    "zvd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_124_capitulation_signal},
    "zvd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_125_capitulation_signal},
    "zvd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_126_capitulation_signal},
    "zvd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_127_capitulation_signal},
    "zvd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_128_capitulation_signal},
    "zvd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_129_capitulation_signal},
    "zvd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_130_capitulation_signal},
    "zvd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_131_capitulation_signal},
    "zvd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_132_capitulation_signal},
    "zvd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_133_capitulation_signal},
    "zvd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_134_capitulation_signal},
    "zvd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_135_capitulation_signal},
    "zvd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_136_capitulation_signal},
    "zvd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_137_capitulation_signal},
    "zvd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_138_capitulation_signal},
    "zvd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_139_capitulation_signal},
    "zvd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_140_capitulation_signal},
    "zvd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_141_capitulation_signal},
    "zvd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_142_capitulation_signal},
    "zvd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_143_capitulation_signal},
    "zvd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_144_capitulation_signal},
    "zvd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_145_capitulation_signal},
    "zvd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_146_capitulation_signal},
    "zvd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_147_capitulation_signal},
    "zvd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_148_capitulation_signal},
    "zvd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_149_capitulation_signal},
    "zvd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_150_capitulation_signal},
}
