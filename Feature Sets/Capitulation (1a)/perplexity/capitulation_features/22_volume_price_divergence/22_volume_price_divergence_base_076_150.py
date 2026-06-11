"""Generated capitulation features for 22_volume_price_divergence: volume rising while price falls.
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

def vpd_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vpd_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vpd_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vpd_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vpd_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vpd_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vpd_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vpd_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vpd_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vpd_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vpd_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vpd_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vpd_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vpd_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vpd_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vpd_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vpd_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vpd_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vpd_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vpd_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vpd_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vpd_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vpd_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vpd_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vpd_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vpd_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vpd_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vpd_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vpd_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vpd_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vpd_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vpd_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vpd_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vpd_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vpd_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vpd_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vpd_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vpd_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vpd_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vpd_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vpd_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vpd_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vpd_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vpd_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vpd_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vpd_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vpd_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vpd_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vpd_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vpd_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vpd_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vpd_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vpd_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vpd_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vpd_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vpd_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vpd_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vpd_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vpd_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_PRICE_DIVERGENCE_REGISTRY_076_150 = {
    "vpd_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_076_capitulation_signal},
    "vpd_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_077_capitulation_signal},
    "vpd_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_078_capitulation_signal},
    "vpd_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_079_capitulation_signal},
    "vpd_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_080_capitulation_signal},
    "vpd_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_081_capitulation_signal},
    "vpd_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_082_capitulation_signal},
    "vpd_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_083_capitulation_signal},
    "vpd_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_084_capitulation_signal},
    "vpd_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_085_capitulation_signal},
    "vpd_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_086_capitulation_signal},
    "vpd_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_087_capitulation_signal},
    "vpd_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_088_capitulation_signal},
    "vpd_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_089_capitulation_signal},
    "vpd_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_090_capitulation_signal},
    "vpd_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_091_capitulation_signal},
    "vpd_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_092_capitulation_signal},
    "vpd_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_093_capitulation_signal},
    "vpd_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_094_capitulation_signal},
    "vpd_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_095_capitulation_signal},
    "vpd_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_096_capitulation_signal},
    "vpd_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_097_capitulation_signal},
    "vpd_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_098_capitulation_signal},
    "vpd_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_099_capitulation_signal},
    "vpd_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_100_capitulation_signal},
    "vpd_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_101_capitulation_signal},
    "vpd_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_102_capitulation_signal},
    "vpd_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_103_capitulation_signal},
    "vpd_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_104_capitulation_signal},
    "vpd_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_105_capitulation_signal},
    "vpd_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_106_capitulation_signal},
    "vpd_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_107_capitulation_signal},
    "vpd_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_108_capitulation_signal},
    "vpd_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_109_capitulation_signal},
    "vpd_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_110_capitulation_signal},
    "vpd_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_111_capitulation_signal},
    "vpd_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_112_capitulation_signal},
    "vpd_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_113_capitulation_signal},
    "vpd_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_114_capitulation_signal},
    "vpd_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_115_capitulation_signal},
    "vpd_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_116_capitulation_signal},
    "vpd_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_117_capitulation_signal},
    "vpd_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_118_capitulation_signal},
    "vpd_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_119_capitulation_signal},
    "vpd_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_120_capitulation_signal},
    "vpd_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_121_capitulation_signal},
    "vpd_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_122_capitulation_signal},
    "vpd_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_123_capitulation_signal},
    "vpd_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_124_capitulation_signal},
    "vpd_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_125_capitulation_signal},
    "vpd_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_126_capitulation_signal},
    "vpd_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_127_capitulation_signal},
    "vpd_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_128_capitulation_signal},
    "vpd_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_129_capitulation_signal},
    "vpd_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_130_capitulation_signal},
    "vpd_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_131_capitulation_signal},
    "vpd_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_132_capitulation_signal},
    "vpd_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_133_capitulation_signal},
    "vpd_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_134_capitulation_signal},
    "vpd_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_135_capitulation_signal},
    "vpd_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_136_capitulation_signal},
    "vpd_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_137_capitulation_signal},
    "vpd_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_138_capitulation_signal},
    "vpd_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_139_capitulation_signal},
    "vpd_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_140_capitulation_signal},
    "vpd_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_141_capitulation_signal},
    "vpd_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_142_capitulation_signal},
    "vpd_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_143_capitulation_signal},
    "vpd_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_144_capitulation_signal},
    "vpd_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_145_capitulation_signal},
    "vpd_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_146_capitulation_signal},
    "vpd_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_147_capitulation_signal},
    "vpd_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_148_capitulation_signal},
    "vpd_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_149_capitulation_signal},
    "vpd_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_150_capitulation_signal},
}
