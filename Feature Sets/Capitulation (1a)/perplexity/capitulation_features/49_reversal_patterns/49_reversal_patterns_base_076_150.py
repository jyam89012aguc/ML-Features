"""Generated capitulation features for 49_reversal_patterns: intraday reversal bars.
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

def rev_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def rev_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def rev_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def rev_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def rev_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def rev_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def rev_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def rev_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def rev_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def rev_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def rev_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def rev_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def rev_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def rev_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def rev_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def rev_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rev_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def rev_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def rev_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def rev_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def rev_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def rev_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def rev_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def rev_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def rev_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def rev_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def rev_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def rev_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def rev_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def rev_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rev_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def rev_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def rev_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def rev_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def rev_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def rev_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def rev_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def rev_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def rev_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def rev_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def rev_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def rev_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def rev_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def rev_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rev_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def rev_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def rev_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def rev_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def rev_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def rev_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def rev_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def rev_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def rev_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def rev_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def rev_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def rev_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def rev_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def rev_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rev_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

REVERSAL_PATTERNS_REGISTRY_076_150 = {
    "rev_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_076_capitulation_signal},
    "rev_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_077_capitulation_signal},
    "rev_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_078_capitulation_signal},
    "rev_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_079_capitulation_signal},
    "rev_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_080_capitulation_signal},
    "rev_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_081_capitulation_signal},
    "rev_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_082_capitulation_signal},
    "rev_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_083_capitulation_signal},
    "rev_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_084_capitulation_signal},
    "rev_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_085_capitulation_signal},
    "rev_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_086_capitulation_signal},
    "rev_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_087_capitulation_signal},
    "rev_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_088_capitulation_signal},
    "rev_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_089_capitulation_signal},
    "rev_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_090_capitulation_signal},
    "rev_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_091_capitulation_signal},
    "rev_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_092_capitulation_signal},
    "rev_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_093_capitulation_signal},
    "rev_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_094_capitulation_signal},
    "rev_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_095_capitulation_signal},
    "rev_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_096_capitulation_signal},
    "rev_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_097_capitulation_signal},
    "rev_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_098_capitulation_signal},
    "rev_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_099_capitulation_signal},
    "rev_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_100_capitulation_signal},
    "rev_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_101_capitulation_signal},
    "rev_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_102_capitulation_signal},
    "rev_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_103_capitulation_signal},
    "rev_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_104_capitulation_signal},
    "rev_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_105_capitulation_signal},
    "rev_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_106_capitulation_signal},
    "rev_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_107_capitulation_signal},
    "rev_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_108_capitulation_signal},
    "rev_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_109_capitulation_signal},
    "rev_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_110_capitulation_signal},
    "rev_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_111_capitulation_signal},
    "rev_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_112_capitulation_signal},
    "rev_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_113_capitulation_signal},
    "rev_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_114_capitulation_signal},
    "rev_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_115_capitulation_signal},
    "rev_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_116_capitulation_signal},
    "rev_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_117_capitulation_signal},
    "rev_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_118_capitulation_signal},
    "rev_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_119_capitulation_signal},
    "rev_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_120_capitulation_signal},
    "rev_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_121_capitulation_signal},
    "rev_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_122_capitulation_signal},
    "rev_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_123_capitulation_signal},
    "rev_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_124_capitulation_signal},
    "rev_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_125_capitulation_signal},
    "rev_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_126_capitulation_signal},
    "rev_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_127_capitulation_signal},
    "rev_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_128_capitulation_signal},
    "rev_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_129_capitulation_signal},
    "rev_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_130_capitulation_signal},
    "rev_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_131_capitulation_signal},
    "rev_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_132_capitulation_signal},
    "rev_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_133_capitulation_signal},
    "rev_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_134_capitulation_signal},
    "rev_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_135_capitulation_signal},
    "rev_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_136_capitulation_signal},
    "rev_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_137_capitulation_signal},
    "rev_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_138_capitulation_signal},
    "rev_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_139_capitulation_signal},
    "rev_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_140_capitulation_signal},
    "rev_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_141_capitulation_signal},
    "rev_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_142_capitulation_signal},
    "rev_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_143_capitulation_signal},
    "rev_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_144_capitulation_signal},
    "rev_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_145_capitulation_signal},
    "rev_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_146_capitulation_signal},
    "rev_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_147_capitulation_signal},
    "rev_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_148_capitulation_signal},
    "rev_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_149_capitulation_signal},
    "rev_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_150_capitulation_signal},
}
