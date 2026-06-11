"""Generated capitulation features for 48_open_close_dynamics: open-close behavior.
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

def ocd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def ocd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def ocd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def ocd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def ocd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def ocd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def ocd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def ocd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def ocd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def ocd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def ocd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def ocd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def ocd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def ocd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def ocd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def ocd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ocd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def ocd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def ocd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def ocd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def ocd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def ocd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def ocd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def ocd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def ocd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def ocd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def ocd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def ocd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def ocd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def ocd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ocd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def ocd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def ocd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def ocd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def ocd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def ocd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def ocd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def ocd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def ocd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def ocd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def ocd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def ocd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def ocd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def ocd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ocd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def ocd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def ocd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def ocd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def ocd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def ocd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def ocd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def ocd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def ocd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def ocd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def ocd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def ocd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def ocd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def ocd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ocd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

OPEN_CLOSE_DYNAMICS_REGISTRY_076_150 = {
    "ocd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_076_capitulation_signal},
    "ocd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_077_capitulation_signal},
    "ocd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_078_capitulation_signal},
    "ocd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_079_capitulation_signal},
    "ocd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_080_capitulation_signal},
    "ocd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_081_capitulation_signal},
    "ocd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_082_capitulation_signal},
    "ocd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_083_capitulation_signal},
    "ocd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_084_capitulation_signal},
    "ocd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_085_capitulation_signal},
    "ocd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_086_capitulation_signal},
    "ocd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_087_capitulation_signal},
    "ocd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_088_capitulation_signal},
    "ocd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_089_capitulation_signal},
    "ocd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_090_capitulation_signal},
    "ocd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_091_capitulation_signal},
    "ocd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_092_capitulation_signal},
    "ocd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_093_capitulation_signal},
    "ocd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_094_capitulation_signal},
    "ocd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_095_capitulation_signal},
    "ocd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_096_capitulation_signal},
    "ocd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_097_capitulation_signal},
    "ocd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_098_capitulation_signal},
    "ocd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_099_capitulation_signal},
    "ocd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_100_capitulation_signal},
    "ocd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_101_capitulation_signal},
    "ocd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_102_capitulation_signal},
    "ocd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_103_capitulation_signal},
    "ocd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_104_capitulation_signal},
    "ocd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_105_capitulation_signal},
    "ocd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_106_capitulation_signal},
    "ocd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_107_capitulation_signal},
    "ocd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_108_capitulation_signal},
    "ocd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_109_capitulation_signal},
    "ocd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_110_capitulation_signal},
    "ocd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_111_capitulation_signal},
    "ocd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_112_capitulation_signal},
    "ocd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_113_capitulation_signal},
    "ocd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_114_capitulation_signal},
    "ocd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_115_capitulation_signal},
    "ocd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_116_capitulation_signal},
    "ocd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_117_capitulation_signal},
    "ocd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_118_capitulation_signal},
    "ocd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_119_capitulation_signal},
    "ocd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_120_capitulation_signal},
    "ocd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_121_capitulation_signal},
    "ocd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_122_capitulation_signal},
    "ocd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_123_capitulation_signal},
    "ocd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_124_capitulation_signal},
    "ocd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_125_capitulation_signal},
    "ocd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_126_capitulation_signal},
    "ocd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_127_capitulation_signal},
    "ocd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_128_capitulation_signal},
    "ocd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_129_capitulation_signal},
    "ocd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_130_capitulation_signal},
    "ocd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_131_capitulation_signal},
    "ocd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_132_capitulation_signal},
    "ocd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_133_capitulation_signal},
    "ocd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_134_capitulation_signal},
    "ocd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_135_capitulation_signal},
    "ocd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_136_capitulation_signal},
    "ocd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_137_capitulation_signal},
    "ocd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_138_capitulation_signal},
    "ocd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_139_capitulation_signal},
    "ocd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_140_capitulation_signal},
    "ocd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_141_capitulation_signal},
    "ocd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_142_capitulation_signal},
    "ocd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_143_capitulation_signal},
    "ocd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_144_capitulation_signal},
    "ocd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_145_capitulation_signal},
    "ocd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_146_capitulation_signal},
    "ocd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_147_capitulation_signal},
    "ocd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_148_capitulation_signal},
    "ocd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_149_capitulation_signal},
    "ocd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_150_capitulation_signal},
}
