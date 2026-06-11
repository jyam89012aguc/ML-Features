"""Generated capitulation features for 23_dollar_volume_shock: dollar-volume spikes.
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

def dvs_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def dvs_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def dvs_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def dvs_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def dvs_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def dvs_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def dvs_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def dvs_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def dvs_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def dvs_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def dvs_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def dvs_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def dvs_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def dvs_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def dvs_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def dvs_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dvs_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def dvs_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def dvs_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def dvs_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def dvs_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def dvs_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def dvs_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def dvs_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def dvs_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def dvs_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def dvs_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def dvs_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def dvs_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def dvs_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dvs_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def dvs_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def dvs_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def dvs_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def dvs_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def dvs_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def dvs_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def dvs_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def dvs_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def dvs_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def dvs_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def dvs_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def dvs_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def dvs_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dvs_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def dvs_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def dvs_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def dvs_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def dvs_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def dvs_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def dvs_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def dvs_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def dvs_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def dvs_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def dvs_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def dvs_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def dvs_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def dvs_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dvs_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DOLLAR_VOLUME_SHOCK_REGISTRY_076_150 = {
    "dvs_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_076_capitulation_signal},
    "dvs_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_077_capitulation_signal},
    "dvs_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_078_capitulation_signal},
    "dvs_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_079_capitulation_signal},
    "dvs_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_080_capitulation_signal},
    "dvs_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_081_capitulation_signal},
    "dvs_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_082_capitulation_signal},
    "dvs_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_083_capitulation_signal},
    "dvs_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_084_capitulation_signal},
    "dvs_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_085_capitulation_signal},
    "dvs_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_086_capitulation_signal},
    "dvs_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_087_capitulation_signal},
    "dvs_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_088_capitulation_signal},
    "dvs_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_089_capitulation_signal},
    "dvs_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_090_capitulation_signal},
    "dvs_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_091_capitulation_signal},
    "dvs_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_092_capitulation_signal},
    "dvs_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_093_capitulation_signal},
    "dvs_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_094_capitulation_signal},
    "dvs_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_095_capitulation_signal},
    "dvs_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_096_capitulation_signal},
    "dvs_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_097_capitulation_signal},
    "dvs_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_098_capitulation_signal},
    "dvs_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_099_capitulation_signal},
    "dvs_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_100_capitulation_signal},
    "dvs_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_101_capitulation_signal},
    "dvs_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_102_capitulation_signal},
    "dvs_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_103_capitulation_signal},
    "dvs_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_104_capitulation_signal},
    "dvs_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_105_capitulation_signal},
    "dvs_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_106_capitulation_signal},
    "dvs_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_107_capitulation_signal},
    "dvs_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_108_capitulation_signal},
    "dvs_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_109_capitulation_signal},
    "dvs_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_110_capitulation_signal},
    "dvs_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_111_capitulation_signal},
    "dvs_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_112_capitulation_signal},
    "dvs_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_113_capitulation_signal},
    "dvs_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_114_capitulation_signal},
    "dvs_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_115_capitulation_signal},
    "dvs_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_116_capitulation_signal},
    "dvs_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_117_capitulation_signal},
    "dvs_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_118_capitulation_signal},
    "dvs_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_119_capitulation_signal},
    "dvs_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_120_capitulation_signal},
    "dvs_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_121_capitulation_signal},
    "dvs_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_122_capitulation_signal},
    "dvs_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_123_capitulation_signal},
    "dvs_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_124_capitulation_signal},
    "dvs_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_125_capitulation_signal},
    "dvs_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_126_capitulation_signal},
    "dvs_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_127_capitulation_signal},
    "dvs_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_128_capitulation_signal},
    "dvs_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_129_capitulation_signal},
    "dvs_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_130_capitulation_signal},
    "dvs_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_131_capitulation_signal},
    "dvs_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_132_capitulation_signal},
    "dvs_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_133_capitulation_signal},
    "dvs_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_134_capitulation_signal},
    "dvs_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_135_capitulation_signal},
    "dvs_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_136_capitulation_signal},
    "dvs_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_137_capitulation_signal},
    "dvs_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_138_capitulation_signal},
    "dvs_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_139_capitulation_signal},
    "dvs_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_140_capitulation_signal},
    "dvs_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_141_capitulation_signal},
    "dvs_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_142_capitulation_signal},
    "dvs_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_143_capitulation_signal},
    "dvs_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_144_capitulation_signal},
    "dvs_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_145_capitulation_signal},
    "dvs_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_146_capitulation_signal},
    "dvs_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_147_capitulation_signal},
    "dvs_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_148_capitulation_signal},
    "dvs_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_149_capitulation_signal},
    "dvs_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_150_capitulation_signal},
}
