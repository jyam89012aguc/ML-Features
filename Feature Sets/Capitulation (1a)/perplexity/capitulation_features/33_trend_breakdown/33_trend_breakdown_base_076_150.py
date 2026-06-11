"""Generated capitulation features for 33_trend_breakdown: moving-average trend loss.
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

def tbd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def tbd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def tbd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def tbd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def tbd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def tbd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def tbd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def tbd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def tbd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def tbd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def tbd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def tbd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def tbd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def tbd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def tbd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def tbd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tbd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def tbd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def tbd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def tbd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def tbd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def tbd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def tbd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def tbd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def tbd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def tbd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def tbd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def tbd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def tbd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def tbd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tbd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def tbd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def tbd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def tbd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def tbd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def tbd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def tbd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def tbd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def tbd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def tbd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def tbd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def tbd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def tbd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def tbd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tbd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def tbd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def tbd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def tbd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def tbd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def tbd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def tbd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def tbd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def tbd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def tbd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def tbd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def tbd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def tbd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def tbd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tbd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

TREND_BREAKDOWN_REGISTRY_076_150 = {
    "tbd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_076_capitulation_signal},
    "tbd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_077_capitulation_signal},
    "tbd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_078_capitulation_signal},
    "tbd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_079_capitulation_signal},
    "tbd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_080_capitulation_signal},
    "tbd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_081_capitulation_signal},
    "tbd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_082_capitulation_signal},
    "tbd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_083_capitulation_signal},
    "tbd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_084_capitulation_signal},
    "tbd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_085_capitulation_signal},
    "tbd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_086_capitulation_signal},
    "tbd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_087_capitulation_signal},
    "tbd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_088_capitulation_signal},
    "tbd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_089_capitulation_signal},
    "tbd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_090_capitulation_signal},
    "tbd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_091_capitulation_signal},
    "tbd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_092_capitulation_signal},
    "tbd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_093_capitulation_signal},
    "tbd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_094_capitulation_signal},
    "tbd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_095_capitulation_signal},
    "tbd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_096_capitulation_signal},
    "tbd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_097_capitulation_signal},
    "tbd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_098_capitulation_signal},
    "tbd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_099_capitulation_signal},
    "tbd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_100_capitulation_signal},
    "tbd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_101_capitulation_signal},
    "tbd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_102_capitulation_signal},
    "tbd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_103_capitulation_signal},
    "tbd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_104_capitulation_signal},
    "tbd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_105_capitulation_signal},
    "tbd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_106_capitulation_signal},
    "tbd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_107_capitulation_signal},
    "tbd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_108_capitulation_signal},
    "tbd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_109_capitulation_signal},
    "tbd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_110_capitulation_signal},
    "tbd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_111_capitulation_signal},
    "tbd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_112_capitulation_signal},
    "tbd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_113_capitulation_signal},
    "tbd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_114_capitulation_signal},
    "tbd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_115_capitulation_signal},
    "tbd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_116_capitulation_signal},
    "tbd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_117_capitulation_signal},
    "tbd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_118_capitulation_signal},
    "tbd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_119_capitulation_signal},
    "tbd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_120_capitulation_signal},
    "tbd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_121_capitulation_signal},
    "tbd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_122_capitulation_signal},
    "tbd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_123_capitulation_signal},
    "tbd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_124_capitulation_signal},
    "tbd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_125_capitulation_signal},
    "tbd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_126_capitulation_signal},
    "tbd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_127_capitulation_signal},
    "tbd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_128_capitulation_signal},
    "tbd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_129_capitulation_signal},
    "tbd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_130_capitulation_signal},
    "tbd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_131_capitulation_signal},
    "tbd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_132_capitulation_signal},
    "tbd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_133_capitulation_signal},
    "tbd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_134_capitulation_signal},
    "tbd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_135_capitulation_signal},
    "tbd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_136_capitulation_signal},
    "tbd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_137_capitulation_signal},
    "tbd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_138_capitulation_signal},
    "tbd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_139_capitulation_signal},
    "tbd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_140_capitulation_signal},
    "tbd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_141_capitulation_signal},
    "tbd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_142_capitulation_signal},
    "tbd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_143_capitulation_signal},
    "tbd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_144_capitulation_signal},
    "tbd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_145_capitulation_signal},
    "tbd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_146_capitulation_signal},
    "tbd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_147_capitulation_signal},
    "tbd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_148_capitulation_signal},
    "tbd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_149_capitulation_signal},
    "tbd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_150_capitulation_signal},
}
