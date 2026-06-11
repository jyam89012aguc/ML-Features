"""Generated capitulation features for 50_failed_breakdown: undercut-and-reclaim.
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

def fbd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def fbd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def fbd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def fbd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def fbd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def fbd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def fbd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def fbd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def fbd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def fbd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def fbd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def fbd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def fbd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def fbd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def fbd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def fbd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def fbd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def fbd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def fbd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def fbd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def fbd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def fbd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def fbd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def fbd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def fbd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def fbd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def fbd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def fbd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def fbd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def fbd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def fbd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def fbd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def fbd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def fbd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def fbd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def fbd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def fbd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def fbd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def fbd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def fbd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def fbd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def fbd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def fbd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def fbd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def fbd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def fbd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def fbd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def fbd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def fbd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def fbd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def fbd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def fbd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def fbd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def fbd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def fbd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def fbd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def fbd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def fbd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def fbd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

FAILED_BREAKDOWN_REGISTRY_076_150 = {
    "fbd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_076_capitulation_signal},
    "fbd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_077_capitulation_signal},
    "fbd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_078_capitulation_signal},
    "fbd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_079_capitulation_signal},
    "fbd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_080_capitulation_signal},
    "fbd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_081_capitulation_signal},
    "fbd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_082_capitulation_signal},
    "fbd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_083_capitulation_signal},
    "fbd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_084_capitulation_signal},
    "fbd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_085_capitulation_signal},
    "fbd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_086_capitulation_signal},
    "fbd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_087_capitulation_signal},
    "fbd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_088_capitulation_signal},
    "fbd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_089_capitulation_signal},
    "fbd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_090_capitulation_signal},
    "fbd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_091_capitulation_signal},
    "fbd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_092_capitulation_signal},
    "fbd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_093_capitulation_signal},
    "fbd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_094_capitulation_signal},
    "fbd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_095_capitulation_signal},
    "fbd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_096_capitulation_signal},
    "fbd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_097_capitulation_signal},
    "fbd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_098_capitulation_signal},
    "fbd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_099_capitulation_signal},
    "fbd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_100_capitulation_signal},
    "fbd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_101_capitulation_signal},
    "fbd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_102_capitulation_signal},
    "fbd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_103_capitulation_signal},
    "fbd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_104_capitulation_signal},
    "fbd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_105_capitulation_signal},
    "fbd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_106_capitulation_signal},
    "fbd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_107_capitulation_signal},
    "fbd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_108_capitulation_signal},
    "fbd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_109_capitulation_signal},
    "fbd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_110_capitulation_signal},
    "fbd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_111_capitulation_signal},
    "fbd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_112_capitulation_signal},
    "fbd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_113_capitulation_signal},
    "fbd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_114_capitulation_signal},
    "fbd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_115_capitulation_signal},
    "fbd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_116_capitulation_signal},
    "fbd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_117_capitulation_signal},
    "fbd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_118_capitulation_signal},
    "fbd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_119_capitulation_signal},
    "fbd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_120_capitulation_signal},
    "fbd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_121_capitulation_signal},
    "fbd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_122_capitulation_signal},
    "fbd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_123_capitulation_signal},
    "fbd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_124_capitulation_signal},
    "fbd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_125_capitulation_signal},
    "fbd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_126_capitulation_signal},
    "fbd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_127_capitulation_signal},
    "fbd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_128_capitulation_signal},
    "fbd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_129_capitulation_signal},
    "fbd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_130_capitulation_signal},
    "fbd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_131_capitulation_signal},
    "fbd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_132_capitulation_signal},
    "fbd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_133_capitulation_signal},
    "fbd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_134_capitulation_signal},
    "fbd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_135_capitulation_signal},
    "fbd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_136_capitulation_signal},
    "fbd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_137_capitulation_signal},
    "fbd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_138_capitulation_signal},
    "fbd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_139_capitulation_signal},
    "fbd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_140_capitulation_signal},
    "fbd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_141_capitulation_signal},
    "fbd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_142_capitulation_signal},
    "fbd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_143_capitulation_signal},
    "fbd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_144_capitulation_signal},
    "fbd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_145_capitulation_signal},
    "fbd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_146_capitulation_signal},
    "fbd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_147_capitulation_signal},
    "fbd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_148_capitulation_signal},
    "fbd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_149_capitulation_signal},
    "fbd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_150_capitulation_signal},
}
