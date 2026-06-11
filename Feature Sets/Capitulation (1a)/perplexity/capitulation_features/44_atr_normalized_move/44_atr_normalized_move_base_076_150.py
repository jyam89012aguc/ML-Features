"""Generated capitulation features for 44_atr_normalized_move: moves measured in ATR units.
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

def atr_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def atr_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def atr_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def atr_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def atr_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def atr_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def atr_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def atr_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def atr_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def atr_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def atr_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def atr_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def atr_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def atr_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def atr_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def atr_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def atr_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def atr_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def atr_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def atr_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def atr_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def atr_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def atr_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def atr_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def atr_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def atr_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def atr_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def atr_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def atr_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def atr_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def atr_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def atr_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def atr_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def atr_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def atr_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def atr_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def atr_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def atr_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def atr_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def atr_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def atr_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def atr_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def atr_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def atr_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def atr_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def atr_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def atr_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def atr_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def atr_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def atr_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def atr_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def atr_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def atr_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def atr_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def atr_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def atr_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def atr_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def atr_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def atr_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

ATR_NORMALIZED_MOVE_REGISTRY_076_150 = {
    "atr_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_076_capitulation_signal},
    "atr_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_077_capitulation_signal},
    "atr_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_078_capitulation_signal},
    "atr_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_079_capitulation_signal},
    "atr_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_080_capitulation_signal},
    "atr_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_081_capitulation_signal},
    "atr_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_082_capitulation_signal},
    "atr_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_083_capitulation_signal},
    "atr_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_084_capitulation_signal},
    "atr_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_085_capitulation_signal},
    "atr_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_086_capitulation_signal},
    "atr_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_087_capitulation_signal},
    "atr_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_088_capitulation_signal},
    "atr_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_089_capitulation_signal},
    "atr_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_090_capitulation_signal},
    "atr_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_091_capitulation_signal},
    "atr_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_092_capitulation_signal},
    "atr_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_093_capitulation_signal},
    "atr_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_094_capitulation_signal},
    "atr_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_095_capitulation_signal},
    "atr_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_096_capitulation_signal},
    "atr_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_097_capitulation_signal},
    "atr_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_098_capitulation_signal},
    "atr_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_099_capitulation_signal},
    "atr_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_100_capitulation_signal},
    "atr_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_101_capitulation_signal},
    "atr_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_102_capitulation_signal},
    "atr_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_103_capitulation_signal},
    "atr_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_104_capitulation_signal},
    "atr_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_105_capitulation_signal},
    "atr_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_106_capitulation_signal},
    "atr_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_107_capitulation_signal},
    "atr_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_108_capitulation_signal},
    "atr_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_109_capitulation_signal},
    "atr_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_110_capitulation_signal},
    "atr_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_111_capitulation_signal},
    "atr_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_112_capitulation_signal},
    "atr_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_113_capitulation_signal},
    "atr_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_114_capitulation_signal},
    "atr_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_115_capitulation_signal},
    "atr_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_116_capitulation_signal},
    "atr_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_117_capitulation_signal},
    "atr_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_118_capitulation_signal},
    "atr_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_119_capitulation_signal},
    "atr_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_120_capitulation_signal},
    "atr_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_121_capitulation_signal},
    "atr_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_122_capitulation_signal},
    "atr_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_123_capitulation_signal},
    "atr_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_124_capitulation_signal},
    "atr_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_125_capitulation_signal},
    "atr_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_126_capitulation_signal},
    "atr_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_127_capitulation_signal},
    "atr_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_128_capitulation_signal},
    "atr_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_129_capitulation_signal},
    "atr_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_130_capitulation_signal},
    "atr_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_131_capitulation_signal},
    "atr_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_132_capitulation_signal},
    "atr_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_133_capitulation_signal},
    "atr_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_134_capitulation_signal},
    "atr_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_135_capitulation_signal},
    "atr_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_136_capitulation_signal},
    "atr_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_137_capitulation_signal},
    "atr_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_138_capitulation_signal},
    "atr_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_139_capitulation_signal},
    "atr_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_140_capitulation_signal},
    "atr_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_141_capitulation_signal},
    "atr_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_142_capitulation_signal},
    "atr_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_143_capitulation_signal},
    "atr_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_144_capitulation_signal},
    "atr_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_145_capitulation_signal},
    "atr_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_146_capitulation_signal},
    "atr_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_147_capitulation_signal},
    "atr_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_148_capitulation_signal},
    "atr_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_149_capitulation_signal},
    "atr_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_150_capitulation_signal},
}
