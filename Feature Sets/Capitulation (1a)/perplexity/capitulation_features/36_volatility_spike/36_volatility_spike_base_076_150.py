"""Generated capitulation features for 36_volatility_spike: realized volatility spikes.
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

def vsp_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vsp_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vsp_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vsp_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vsp_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vsp_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vsp_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vsp_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vsp_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vsp_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vsp_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vsp_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vsp_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vsp_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vsp_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vsp_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vsp_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vsp_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vsp_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vsp_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vsp_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vsp_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vsp_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vsp_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vsp_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vsp_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vsp_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vsp_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vsp_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vsp_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vsp_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vsp_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vsp_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vsp_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vsp_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vsp_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vsp_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vsp_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vsp_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vsp_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vsp_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vsp_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vsp_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vsp_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vsp_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vsp_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vsp_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vsp_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vsp_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vsp_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vsp_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vsp_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vsp_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vsp_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vsp_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vsp_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vsp_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vsp_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vsp_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLATILITY_SPIKE_REGISTRY_076_150 = {
    "vsp_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_076_capitulation_signal},
    "vsp_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_077_capitulation_signal},
    "vsp_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_078_capitulation_signal},
    "vsp_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_079_capitulation_signal},
    "vsp_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_080_capitulation_signal},
    "vsp_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_081_capitulation_signal},
    "vsp_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_082_capitulation_signal},
    "vsp_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_083_capitulation_signal},
    "vsp_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_084_capitulation_signal},
    "vsp_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_085_capitulation_signal},
    "vsp_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_086_capitulation_signal},
    "vsp_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_087_capitulation_signal},
    "vsp_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_088_capitulation_signal},
    "vsp_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_089_capitulation_signal},
    "vsp_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_090_capitulation_signal},
    "vsp_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_091_capitulation_signal},
    "vsp_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_092_capitulation_signal},
    "vsp_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_093_capitulation_signal},
    "vsp_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_094_capitulation_signal},
    "vsp_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_095_capitulation_signal},
    "vsp_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_096_capitulation_signal},
    "vsp_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_097_capitulation_signal},
    "vsp_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_098_capitulation_signal},
    "vsp_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_099_capitulation_signal},
    "vsp_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_100_capitulation_signal},
    "vsp_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_101_capitulation_signal},
    "vsp_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_102_capitulation_signal},
    "vsp_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_103_capitulation_signal},
    "vsp_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_104_capitulation_signal},
    "vsp_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_105_capitulation_signal},
    "vsp_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_106_capitulation_signal},
    "vsp_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_107_capitulation_signal},
    "vsp_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_108_capitulation_signal},
    "vsp_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_109_capitulation_signal},
    "vsp_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_110_capitulation_signal},
    "vsp_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_111_capitulation_signal},
    "vsp_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_112_capitulation_signal},
    "vsp_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_113_capitulation_signal},
    "vsp_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_114_capitulation_signal},
    "vsp_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_115_capitulation_signal},
    "vsp_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_116_capitulation_signal},
    "vsp_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_117_capitulation_signal},
    "vsp_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_118_capitulation_signal},
    "vsp_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_119_capitulation_signal},
    "vsp_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_120_capitulation_signal},
    "vsp_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_121_capitulation_signal},
    "vsp_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_122_capitulation_signal},
    "vsp_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_123_capitulation_signal},
    "vsp_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_124_capitulation_signal},
    "vsp_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_125_capitulation_signal},
    "vsp_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_126_capitulation_signal},
    "vsp_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_127_capitulation_signal},
    "vsp_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_128_capitulation_signal},
    "vsp_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_129_capitulation_signal},
    "vsp_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_130_capitulation_signal},
    "vsp_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_131_capitulation_signal},
    "vsp_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_132_capitulation_signal},
    "vsp_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_133_capitulation_signal},
    "vsp_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_134_capitulation_signal},
    "vsp_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_135_capitulation_signal},
    "vsp_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_136_capitulation_signal},
    "vsp_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_137_capitulation_signal},
    "vsp_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_138_capitulation_signal},
    "vsp_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_139_capitulation_signal},
    "vsp_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_140_capitulation_signal},
    "vsp_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_141_capitulation_signal},
    "vsp_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_142_capitulation_signal},
    "vsp_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_143_capitulation_signal},
    "vsp_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_144_capitulation_signal},
    "vsp_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_145_capitulation_signal},
    "vsp_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_146_capitulation_signal},
    "vsp_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_147_capitulation_signal},
    "vsp_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_148_capitulation_signal},
    "vsp_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_149_capitulation_signal},
    "vsp_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_150_capitulation_signal},
}
