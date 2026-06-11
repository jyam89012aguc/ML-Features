"""Generated capitulation features for 29_consecutive_loss: loss streaks.
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

def ccl_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def ccl_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def ccl_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def ccl_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def ccl_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def ccl_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def ccl_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def ccl_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def ccl_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def ccl_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def ccl_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def ccl_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def ccl_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def ccl_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def ccl_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def ccl_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ccl_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def ccl_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def ccl_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def ccl_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def ccl_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def ccl_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def ccl_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def ccl_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def ccl_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def ccl_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def ccl_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def ccl_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def ccl_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def ccl_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ccl_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def ccl_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def ccl_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def ccl_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def ccl_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def ccl_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def ccl_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def ccl_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def ccl_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def ccl_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def ccl_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def ccl_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def ccl_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def ccl_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ccl_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def ccl_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def ccl_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def ccl_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def ccl_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def ccl_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def ccl_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def ccl_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def ccl_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def ccl_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def ccl_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def ccl_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def ccl_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def ccl_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ccl_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

CONSECUTIVE_LOSS_REGISTRY_076_150 = {
    "ccl_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_076_capitulation_signal},
    "ccl_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_077_capitulation_signal},
    "ccl_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_078_capitulation_signal},
    "ccl_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_079_capitulation_signal},
    "ccl_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_080_capitulation_signal},
    "ccl_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_081_capitulation_signal},
    "ccl_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_082_capitulation_signal},
    "ccl_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_083_capitulation_signal},
    "ccl_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_084_capitulation_signal},
    "ccl_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_085_capitulation_signal},
    "ccl_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_086_capitulation_signal},
    "ccl_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_087_capitulation_signal},
    "ccl_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_088_capitulation_signal},
    "ccl_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_089_capitulation_signal},
    "ccl_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_090_capitulation_signal},
    "ccl_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_091_capitulation_signal},
    "ccl_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_092_capitulation_signal},
    "ccl_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_093_capitulation_signal},
    "ccl_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_094_capitulation_signal},
    "ccl_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_095_capitulation_signal},
    "ccl_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_096_capitulation_signal},
    "ccl_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_097_capitulation_signal},
    "ccl_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_098_capitulation_signal},
    "ccl_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_099_capitulation_signal},
    "ccl_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_100_capitulation_signal},
    "ccl_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_101_capitulation_signal},
    "ccl_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_102_capitulation_signal},
    "ccl_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_103_capitulation_signal},
    "ccl_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_104_capitulation_signal},
    "ccl_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_105_capitulation_signal},
    "ccl_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_106_capitulation_signal},
    "ccl_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_107_capitulation_signal},
    "ccl_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_108_capitulation_signal},
    "ccl_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_109_capitulation_signal},
    "ccl_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_110_capitulation_signal},
    "ccl_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_111_capitulation_signal},
    "ccl_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_112_capitulation_signal},
    "ccl_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_113_capitulation_signal},
    "ccl_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_114_capitulation_signal},
    "ccl_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_115_capitulation_signal},
    "ccl_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_116_capitulation_signal},
    "ccl_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_117_capitulation_signal},
    "ccl_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_118_capitulation_signal},
    "ccl_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_119_capitulation_signal},
    "ccl_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_120_capitulation_signal},
    "ccl_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_121_capitulation_signal},
    "ccl_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_122_capitulation_signal},
    "ccl_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_123_capitulation_signal},
    "ccl_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_124_capitulation_signal},
    "ccl_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_125_capitulation_signal},
    "ccl_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_126_capitulation_signal},
    "ccl_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_127_capitulation_signal},
    "ccl_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_128_capitulation_signal},
    "ccl_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_129_capitulation_signal},
    "ccl_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_130_capitulation_signal},
    "ccl_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_131_capitulation_signal},
    "ccl_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_132_capitulation_signal},
    "ccl_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_133_capitulation_signal},
    "ccl_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_134_capitulation_signal},
    "ccl_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_135_capitulation_signal},
    "ccl_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_136_capitulation_signal},
    "ccl_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_137_capitulation_signal},
    "ccl_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_138_capitulation_signal},
    "ccl_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_139_capitulation_signal},
    "ccl_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_140_capitulation_signal},
    "ccl_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_141_capitulation_signal},
    "ccl_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_142_capitulation_signal},
    "ccl_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_143_capitulation_signal},
    "ccl_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_144_capitulation_signal},
    "ccl_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_145_capitulation_signal},
    "ccl_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_146_capitulation_signal},
    "ccl_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_147_capitulation_signal},
    "ccl_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_148_capitulation_signal},
    "ccl_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_149_capitulation_signal},
    "ccl_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_150_capitulation_signal},
}
