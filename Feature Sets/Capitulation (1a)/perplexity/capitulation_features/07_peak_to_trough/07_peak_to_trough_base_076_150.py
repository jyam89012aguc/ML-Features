"""Generated capitulation features for 07_peak_to_trough: peak-trough ratios.
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

def ptt_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def ptt_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def ptt_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def ptt_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def ptt_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def ptt_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def ptt_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def ptt_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def ptt_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def ptt_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def ptt_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def ptt_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def ptt_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def ptt_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def ptt_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def ptt_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ptt_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def ptt_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def ptt_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def ptt_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def ptt_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def ptt_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def ptt_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def ptt_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def ptt_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def ptt_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def ptt_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def ptt_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def ptt_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def ptt_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ptt_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def ptt_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def ptt_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def ptt_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def ptt_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def ptt_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def ptt_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def ptt_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def ptt_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def ptt_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def ptt_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def ptt_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def ptt_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def ptt_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ptt_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def ptt_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def ptt_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def ptt_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def ptt_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def ptt_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def ptt_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def ptt_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def ptt_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def ptt_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def ptt_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def ptt_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def ptt_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def ptt_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ptt_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

PEAK_TO_TROUGH_REGISTRY_076_150 = {
    "ptt_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_076_capitulation_signal},
    "ptt_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_077_capitulation_signal},
    "ptt_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_078_capitulation_signal},
    "ptt_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_079_capitulation_signal},
    "ptt_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_080_capitulation_signal},
    "ptt_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_081_capitulation_signal},
    "ptt_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_082_capitulation_signal},
    "ptt_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_083_capitulation_signal},
    "ptt_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_084_capitulation_signal},
    "ptt_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_085_capitulation_signal},
    "ptt_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_086_capitulation_signal},
    "ptt_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_087_capitulation_signal},
    "ptt_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_088_capitulation_signal},
    "ptt_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_089_capitulation_signal},
    "ptt_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_090_capitulation_signal},
    "ptt_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_091_capitulation_signal},
    "ptt_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_092_capitulation_signal},
    "ptt_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_093_capitulation_signal},
    "ptt_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_094_capitulation_signal},
    "ptt_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_095_capitulation_signal},
    "ptt_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_096_capitulation_signal},
    "ptt_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_097_capitulation_signal},
    "ptt_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_098_capitulation_signal},
    "ptt_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_099_capitulation_signal},
    "ptt_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_100_capitulation_signal},
    "ptt_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_101_capitulation_signal},
    "ptt_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_102_capitulation_signal},
    "ptt_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_103_capitulation_signal},
    "ptt_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_104_capitulation_signal},
    "ptt_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_105_capitulation_signal},
    "ptt_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_106_capitulation_signal},
    "ptt_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_107_capitulation_signal},
    "ptt_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_108_capitulation_signal},
    "ptt_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_109_capitulation_signal},
    "ptt_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_110_capitulation_signal},
    "ptt_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_111_capitulation_signal},
    "ptt_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_112_capitulation_signal},
    "ptt_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_113_capitulation_signal},
    "ptt_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_114_capitulation_signal},
    "ptt_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_115_capitulation_signal},
    "ptt_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_116_capitulation_signal},
    "ptt_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_117_capitulation_signal},
    "ptt_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_118_capitulation_signal},
    "ptt_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_119_capitulation_signal},
    "ptt_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_120_capitulation_signal},
    "ptt_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_121_capitulation_signal},
    "ptt_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_122_capitulation_signal},
    "ptt_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_123_capitulation_signal},
    "ptt_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_124_capitulation_signal},
    "ptt_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_125_capitulation_signal},
    "ptt_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_126_capitulation_signal},
    "ptt_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_127_capitulation_signal},
    "ptt_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_128_capitulation_signal},
    "ptt_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_129_capitulation_signal},
    "ptt_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_130_capitulation_signal},
    "ptt_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_131_capitulation_signal},
    "ptt_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_132_capitulation_signal},
    "ptt_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_133_capitulation_signal},
    "ptt_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_134_capitulation_signal},
    "ptt_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_135_capitulation_signal},
    "ptt_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_136_capitulation_signal},
    "ptt_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_137_capitulation_signal},
    "ptt_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_138_capitulation_signal},
    "ptt_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_139_capitulation_signal},
    "ptt_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_140_capitulation_signal},
    "ptt_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_141_capitulation_signal},
    "ptt_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_142_capitulation_signal},
    "ptt_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_143_capitulation_signal},
    "ptt_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_144_capitulation_signal},
    "ptt_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_145_capitulation_signal},
    "ptt_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_146_capitulation_signal},
    "ptt_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_147_capitulation_signal},
    "ptt_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_148_capitulation_signal},
    "ptt_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_149_capitulation_signal},
    "ptt_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_150_capitulation_signal},
}
