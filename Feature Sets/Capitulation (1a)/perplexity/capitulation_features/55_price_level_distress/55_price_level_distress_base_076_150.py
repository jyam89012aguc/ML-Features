"""Generated capitulation features for 55_price_level_distress: sub-dollar/five-dollar distress.
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

def pld_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def pld_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def pld_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def pld_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def pld_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def pld_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def pld_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def pld_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def pld_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def pld_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def pld_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def pld_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def pld_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def pld_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def pld_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def pld_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def pld_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def pld_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def pld_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def pld_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def pld_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def pld_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def pld_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def pld_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def pld_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def pld_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def pld_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def pld_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def pld_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def pld_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def pld_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def pld_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def pld_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def pld_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def pld_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def pld_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def pld_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def pld_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def pld_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def pld_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def pld_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def pld_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def pld_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def pld_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def pld_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def pld_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def pld_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def pld_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def pld_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def pld_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def pld_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def pld_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def pld_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def pld_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def pld_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def pld_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def pld_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def pld_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def pld_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

PRICE_LEVEL_DISTRESS_REGISTRY_076_150 = {
    "pld_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_076_capitulation_signal},
    "pld_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_077_capitulation_signal},
    "pld_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_078_capitulation_signal},
    "pld_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_079_capitulation_signal},
    "pld_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_080_capitulation_signal},
    "pld_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_081_capitulation_signal},
    "pld_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_082_capitulation_signal},
    "pld_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_083_capitulation_signal},
    "pld_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_084_capitulation_signal},
    "pld_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_085_capitulation_signal},
    "pld_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_086_capitulation_signal},
    "pld_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_087_capitulation_signal},
    "pld_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_088_capitulation_signal},
    "pld_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_089_capitulation_signal},
    "pld_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_090_capitulation_signal},
    "pld_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_091_capitulation_signal},
    "pld_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_092_capitulation_signal},
    "pld_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_093_capitulation_signal},
    "pld_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_094_capitulation_signal},
    "pld_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_095_capitulation_signal},
    "pld_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_096_capitulation_signal},
    "pld_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_097_capitulation_signal},
    "pld_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_098_capitulation_signal},
    "pld_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_099_capitulation_signal},
    "pld_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_100_capitulation_signal},
    "pld_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_101_capitulation_signal},
    "pld_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_102_capitulation_signal},
    "pld_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_103_capitulation_signal},
    "pld_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_104_capitulation_signal},
    "pld_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_105_capitulation_signal},
    "pld_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_106_capitulation_signal},
    "pld_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_107_capitulation_signal},
    "pld_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_108_capitulation_signal},
    "pld_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_109_capitulation_signal},
    "pld_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_110_capitulation_signal},
    "pld_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_111_capitulation_signal},
    "pld_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_112_capitulation_signal},
    "pld_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_113_capitulation_signal},
    "pld_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_114_capitulation_signal},
    "pld_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_115_capitulation_signal},
    "pld_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_116_capitulation_signal},
    "pld_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_117_capitulation_signal},
    "pld_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_118_capitulation_signal},
    "pld_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_119_capitulation_signal},
    "pld_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_120_capitulation_signal},
    "pld_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_121_capitulation_signal},
    "pld_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_122_capitulation_signal},
    "pld_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_123_capitulation_signal},
    "pld_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_124_capitulation_signal},
    "pld_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_125_capitulation_signal},
    "pld_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_126_capitulation_signal},
    "pld_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_127_capitulation_signal},
    "pld_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_128_capitulation_signal},
    "pld_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_129_capitulation_signal},
    "pld_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_130_capitulation_signal},
    "pld_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_131_capitulation_signal},
    "pld_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_132_capitulation_signal},
    "pld_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_133_capitulation_signal},
    "pld_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_134_capitulation_signal},
    "pld_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_135_capitulation_signal},
    "pld_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_136_capitulation_signal},
    "pld_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_137_capitulation_signal},
    "pld_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_138_capitulation_signal},
    "pld_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_139_capitulation_signal},
    "pld_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_140_capitulation_signal},
    "pld_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_141_capitulation_signal},
    "pld_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_142_capitulation_signal},
    "pld_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_143_capitulation_signal},
    "pld_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_144_capitulation_signal},
    "pld_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_145_capitulation_signal},
    "pld_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_146_capitulation_signal},
    "pld_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_147_capitulation_signal},
    "pld_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_148_capitulation_signal},
    "pld_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_149_capitulation_signal},
    "pld_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_150_capitulation_signal},
}
