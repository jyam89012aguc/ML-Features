"""Generated capitulation features for 26_rsi_extremes: oversold readings.
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

def rsi_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rsi_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rsi_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rsi_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rsi_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rsi_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rsi_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rsi_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rsi_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rsi_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rsi_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rsi_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rsi_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rsi_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rsi_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rsi_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rsi_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rsi_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rsi_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rsi_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rsi_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rsi_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rsi_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rsi_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rsi_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rsi_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rsi_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rsi_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rsi_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rsi_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rsi_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rsi_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rsi_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rsi_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rsi_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rsi_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rsi_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rsi_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rsi_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rsi_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rsi_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rsi_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rsi_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rsi_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rsi_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rsi_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rsi_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rsi_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rsi_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rsi_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rsi_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rsi_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rsi_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rsi_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rsi_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rsi_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rsi_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rsi_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rsi_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

RSI_EXTREMES_REGISTRY_076_150 = {
    "rsi_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_076_capitulation_signal},
    "rsi_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_077_capitulation_signal},
    "rsi_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_078_capitulation_signal},
    "rsi_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_079_capitulation_signal},
    "rsi_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_080_capitulation_signal},
    "rsi_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_081_capitulation_signal},
    "rsi_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_082_capitulation_signal},
    "rsi_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_083_capitulation_signal},
    "rsi_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_084_capitulation_signal},
    "rsi_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_085_capitulation_signal},
    "rsi_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_086_capitulation_signal},
    "rsi_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_087_capitulation_signal},
    "rsi_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_088_capitulation_signal},
    "rsi_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_089_capitulation_signal},
    "rsi_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_090_capitulation_signal},
    "rsi_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_091_capitulation_signal},
    "rsi_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_092_capitulation_signal},
    "rsi_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_093_capitulation_signal},
    "rsi_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_094_capitulation_signal},
    "rsi_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_095_capitulation_signal},
    "rsi_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_096_capitulation_signal},
    "rsi_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_097_capitulation_signal},
    "rsi_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_098_capitulation_signal},
    "rsi_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_099_capitulation_signal},
    "rsi_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_100_capitulation_signal},
    "rsi_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_101_capitulation_signal},
    "rsi_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_102_capitulation_signal},
    "rsi_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_103_capitulation_signal},
    "rsi_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_104_capitulation_signal},
    "rsi_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_105_capitulation_signal},
    "rsi_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_106_capitulation_signal},
    "rsi_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_107_capitulation_signal},
    "rsi_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_108_capitulation_signal},
    "rsi_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_109_capitulation_signal},
    "rsi_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_110_capitulation_signal},
    "rsi_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_111_capitulation_signal},
    "rsi_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_112_capitulation_signal},
    "rsi_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_113_capitulation_signal},
    "rsi_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_114_capitulation_signal},
    "rsi_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_115_capitulation_signal},
    "rsi_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_116_capitulation_signal},
    "rsi_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_117_capitulation_signal},
    "rsi_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_118_capitulation_signal},
    "rsi_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_119_capitulation_signal},
    "rsi_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_120_capitulation_signal},
    "rsi_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_121_capitulation_signal},
    "rsi_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_122_capitulation_signal},
    "rsi_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_123_capitulation_signal},
    "rsi_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_124_capitulation_signal},
    "rsi_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_125_capitulation_signal},
    "rsi_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_126_capitulation_signal},
    "rsi_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_127_capitulation_signal},
    "rsi_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_128_capitulation_signal},
    "rsi_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_129_capitulation_signal},
    "rsi_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_130_capitulation_signal},
    "rsi_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_131_capitulation_signal},
    "rsi_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_132_capitulation_signal},
    "rsi_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_133_capitulation_signal},
    "rsi_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_134_capitulation_signal},
    "rsi_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_135_capitulation_signal},
    "rsi_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_136_capitulation_signal},
    "rsi_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_137_capitulation_signal},
    "rsi_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_138_capitulation_signal},
    "rsi_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_139_capitulation_signal},
    "rsi_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_140_capitulation_signal},
    "rsi_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_141_capitulation_signal},
    "rsi_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_142_capitulation_signal},
    "rsi_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_143_capitulation_signal},
    "rsi_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_144_capitulation_signal},
    "rsi_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_145_capitulation_signal},
    "rsi_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_146_capitulation_signal},
    "rsi_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_147_capitulation_signal},
    "rsi_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_148_capitulation_signal},
    "rsi_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_149_capitulation_signal},
    "rsi_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_150_capitulation_signal},
}
