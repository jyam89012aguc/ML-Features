"""Generated capitulation features for 15_volume_blowoff: volume spikes vs trailing median.
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

def vb_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vb_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vb_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vb_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vb_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vb_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vb_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vb_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vb_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vb_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vb_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vb_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vb_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vb_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vb_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vb_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vb_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vb_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vb_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vb_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vb_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vb_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vb_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vb_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vb_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vb_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vb_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vb_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vb_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vb_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vb_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vb_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vb_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vb_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vb_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vb_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vb_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vb_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vb_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vb_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vb_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vb_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vb_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vb_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vb_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vb_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vb_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vb_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vb_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vb_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vb_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vb_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vb_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vb_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vb_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vb_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vb_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vb_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vb_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_BLOWOFF_REGISTRY_076_150 = {
    "vb_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_076_capitulation_signal},
    "vb_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_077_capitulation_signal},
    "vb_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_078_capitulation_signal},
    "vb_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_079_capitulation_signal},
    "vb_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_080_capitulation_signal},
    "vb_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_081_capitulation_signal},
    "vb_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_082_capitulation_signal},
    "vb_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_083_capitulation_signal},
    "vb_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_084_capitulation_signal},
    "vb_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_085_capitulation_signal},
    "vb_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_086_capitulation_signal},
    "vb_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_087_capitulation_signal},
    "vb_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_088_capitulation_signal},
    "vb_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_089_capitulation_signal},
    "vb_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_090_capitulation_signal},
    "vb_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_091_capitulation_signal},
    "vb_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_092_capitulation_signal},
    "vb_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_093_capitulation_signal},
    "vb_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_094_capitulation_signal},
    "vb_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_095_capitulation_signal},
    "vb_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_096_capitulation_signal},
    "vb_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_097_capitulation_signal},
    "vb_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_098_capitulation_signal},
    "vb_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_099_capitulation_signal},
    "vb_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_100_capitulation_signal},
    "vb_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_101_capitulation_signal},
    "vb_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_102_capitulation_signal},
    "vb_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_103_capitulation_signal},
    "vb_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_104_capitulation_signal},
    "vb_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_105_capitulation_signal},
    "vb_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_106_capitulation_signal},
    "vb_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_107_capitulation_signal},
    "vb_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_108_capitulation_signal},
    "vb_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_109_capitulation_signal},
    "vb_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_110_capitulation_signal},
    "vb_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_111_capitulation_signal},
    "vb_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_112_capitulation_signal},
    "vb_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_113_capitulation_signal},
    "vb_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_114_capitulation_signal},
    "vb_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_115_capitulation_signal},
    "vb_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_116_capitulation_signal},
    "vb_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_117_capitulation_signal},
    "vb_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_118_capitulation_signal},
    "vb_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_119_capitulation_signal},
    "vb_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_120_capitulation_signal},
    "vb_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_121_capitulation_signal},
    "vb_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_122_capitulation_signal},
    "vb_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_123_capitulation_signal},
    "vb_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_124_capitulation_signal},
    "vb_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_125_capitulation_signal},
    "vb_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_126_capitulation_signal},
    "vb_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_127_capitulation_signal},
    "vb_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_128_capitulation_signal},
    "vb_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_129_capitulation_signal},
    "vb_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_130_capitulation_signal},
    "vb_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_131_capitulation_signal},
    "vb_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_132_capitulation_signal},
    "vb_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_133_capitulation_signal},
    "vb_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_134_capitulation_signal},
    "vb_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_135_capitulation_signal},
    "vb_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_136_capitulation_signal},
    "vb_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_137_capitulation_signal},
    "vb_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_138_capitulation_signal},
    "vb_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_139_capitulation_signal},
    "vb_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_140_capitulation_signal},
    "vb_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_141_capitulation_signal},
    "vb_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_142_capitulation_signal},
    "vb_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_143_capitulation_signal},
    "vb_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_144_capitulation_signal},
    "vb_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_145_capitulation_signal},
    "vb_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_146_capitulation_signal},
    "vb_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_147_capitulation_signal},
    "vb_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_148_capitulation_signal},
    "vb_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_149_capitulation_signal},
    "vb_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_150_capitulation_signal},
}
