"""Generated capitulation features for 53_liquidity_collapse: illiquidity spikes.
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

def lqc_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def lqc_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def lqc_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def lqc_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def lqc_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def lqc_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def lqc_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def lqc_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def lqc_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def lqc_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def lqc_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def lqc_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def lqc_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def lqc_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def lqc_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def lqc_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def lqc_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def lqc_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def lqc_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def lqc_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def lqc_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def lqc_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def lqc_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def lqc_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def lqc_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def lqc_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def lqc_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def lqc_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def lqc_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def lqc_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def lqc_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def lqc_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def lqc_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def lqc_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def lqc_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def lqc_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def lqc_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def lqc_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def lqc_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def lqc_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def lqc_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def lqc_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def lqc_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def lqc_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def lqc_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def lqc_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def lqc_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def lqc_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def lqc_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def lqc_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def lqc_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def lqc_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def lqc_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def lqc_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def lqc_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def lqc_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def lqc_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def lqc_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def lqc_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

LIQUIDITY_COLLAPSE_REGISTRY_076_150 = {
    "lqc_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_076_capitulation_signal},
    "lqc_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_077_capitulation_signal},
    "lqc_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_078_capitulation_signal},
    "lqc_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_079_capitulation_signal},
    "lqc_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_080_capitulation_signal},
    "lqc_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_081_capitulation_signal},
    "lqc_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_082_capitulation_signal},
    "lqc_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_083_capitulation_signal},
    "lqc_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_084_capitulation_signal},
    "lqc_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_085_capitulation_signal},
    "lqc_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_086_capitulation_signal},
    "lqc_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_087_capitulation_signal},
    "lqc_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_088_capitulation_signal},
    "lqc_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_089_capitulation_signal},
    "lqc_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_090_capitulation_signal},
    "lqc_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_091_capitulation_signal},
    "lqc_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_092_capitulation_signal},
    "lqc_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_093_capitulation_signal},
    "lqc_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_094_capitulation_signal},
    "lqc_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_095_capitulation_signal},
    "lqc_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_096_capitulation_signal},
    "lqc_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_097_capitulation_signal},
    "lqc_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_098_capitulation_signal},
    "lqc_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_099_capitulation_signal},
    "lqc_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_100_capitulation_signal},
    "lqc_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_101_capitulation_signal},
    "lqc_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_102_capitulation_signal},
    "lqc_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_103_capitulation_signal},
    "lqc_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_104_capitulation_signal},
    "lqc_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_105_capitulation_signal},
    "lqc_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_106_capitulation_signal},
    "lqc_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_107_capitulation_signal},
    "lqc_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_108_capitulation_signal},
    "lqc_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_109_capitulation_signal},
    "lqc_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_110_capitulation_signal},
    "lqc_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_111_capitulation_signal},
    "lqc_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_112_capitulation_signal},
    "lqc_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_113_capitulation_signal},
    "lqc_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_114_capitulation_signal},
    "lqc_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_115_capitulation_signal},
    "lqc_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_116_capitulation_signal},
    "lqc_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_117_capitulation_signal},
    "lqc_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_118_capitulation_signal},
    "lqc_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_119_capitulation_signal},
    "lqc_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_120_capitulation_signal},
    "lqc_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_121_capitulation_signal},
    "lqc_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_122_capitulation_signal},
    "lqc_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_123_capitulation_signal},
    "lqc_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_124_capitulation_signal},
    "lqc_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_125_capitulation_signal},
    "lqc_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_126_capitulation_signal},
    "lqc_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_127_capitulation_signal},
    "lqc_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_128_capitulation_signal},
    "lqc_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_129_capitulation_signal},
    "lqc_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_130_capitulation_signal},
    "lqc_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_131_capitulation_signal},
    "lqc_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_132_capitulation_signal},
    "lqc_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_133_capitulation_signal},
    "lqc_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_134_capitulation_signal},
    "lqc_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_135_capitulation_signal},
    "lqc_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_136_capitulation_signal},
    "lqc_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_137_capitulation_signal},
    "lqc_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_138_capitulation_signal},
    "lqc_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_139_capitulation_signal},
    "lqc_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_140_capitulation_signal},
    "lqc_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_141_capitulation_signal},
    "lqc_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_142_capitulation_signal},
    "lqc_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_143_capitulation_signal},
    "lqc_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_144_capitulation_signal},
    "lqc_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_145_capitulation_signal},
    "lqc_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_146_capitulation_signal},
    "lqc_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_147_capitulation_signal},
    "lqc_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_148_capitulation_signal},
    "lqc_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_149_capitulation_signal},
    "lqc_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_150_capitulation_signal},
}
