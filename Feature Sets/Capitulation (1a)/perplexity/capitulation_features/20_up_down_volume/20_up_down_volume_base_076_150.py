"""Generated capitulation features for 20_up_down_volume: down-day vs up-day volume.
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

def udv_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def udv_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def udv_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def udv_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def udv_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def udv_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def udv_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def udv_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def udv_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def udv_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def udv_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def udv_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def udv_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def udv_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def udv_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def udv_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def udv_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def udv_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def udv_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def udv_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def udv_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def udv_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def udv_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def udv_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def udv_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def udv_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def udv_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def udv_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def udv_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def udv_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def udv_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def udv_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def udv_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def udv_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def udv_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def udv_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def udv_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def udv_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def udv_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def udv_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def udv_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def udv_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def udv_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def udv_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def udv_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def udv_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def udv_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def udv_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def udv_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def udv_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def udv_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def udv_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def udv_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def udv_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def udv_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def udv_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def udv_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def udv_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def udv_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

UP_DOWN_VOLUME_REGISTRY_076_150 = {
    "udv_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_076_capitulation_signal},
    "udv_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_077_capitulation_signal},
    "udv_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_078_capitulation_signal},
    "udv_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_079_capitulation_signal},
    "udv_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_080_capitulation_signal},
    "udv_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_081_capitulation_signal},
    "udv_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_082_capitulation_signal},
    "udv_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_083_capitulation_signal},
    "udv_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_084_capitulation_signal},
    "udv_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_085_capitulation_signal},
    "udv_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_086_capitulation_signal},
    "udv_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_087_capitulation_signal},
    "udv_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_088_capitulation_signal},
    "udv_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_089_capitulation_signal},
    "udv_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_090_capitulation_signal},
    "udv_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_091_capitulation_signal},
    "udv_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_092_capitulation_signal},
    "udv_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_093_capitulation_signal},
    "udv_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_094_capitulation_signal},
    "udv_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_095_capitulation_signal},
    "udv_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_096_capitulation_signal},
    "udv_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_097_capitulation_signal},
    "udv_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_098_capitulation_signal},
    "udv_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_099_capitulation_signal},
    "udv_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_100_capitulation_signal},
    "udv_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_101_capitulation_signal},
    "udv_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_102_capitulation_signal},
    "udv_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_103_capitulation_signal},
    "udv_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_104_capitulation_signal},
    "udv_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_105_capitulation_signal},
    "udv_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_106_capitulation_signal},
    "udv_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_107_capitulation_signal},
    "udv_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_108_capitulation_signal},
    "udv_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_109_capitulation_signal},
    "udv_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_110_capitulation_signal},
    "udv_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_111_capitulation_signal},
    "udv_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_112_capitulation_signal},
    "udv_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_113_capitulation_signal},
    "udv_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_114_capitulation_signal},
    "udv_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_115_capitulation_signal},
    "udv_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_116_capitulation_signal},
    "udv_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_117_capitulation_signal},
    "udv_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_118_capitulation_signal},
    "udv_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_119_capitulation_signal},
    "udv_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_120_capitulation_signal},
    "udv_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_121_capitulation_signal},
    "udv_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_122_capitulation_signal},
    "udv_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_123_capitulation_signal},
    "udv_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_124_capitulation_signal},
    "udv_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_125_capitulation_signal},
    "udv_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_126_capitulation_signal},
    "udv_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_127_capitulation_signal},
    "udv_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_128_capitulation_signal},
    "udv_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_129_capitulation_signal},
    "udv_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_130_capitulation_signal},
    "udv_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_131_capitulation_signal},
    "udv_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_132_capitulation_signal},
    "udv_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_133_capitulation_signal},
    "udv_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_134_capitulation_signal},
    "udv_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_135_capitulation_signal},
    "udv_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_136_capitulation_signal},
    "udv_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_137_capitulation_signal},
    "udv_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_138_capitulation_signal},
    "udv_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_139_capitulation_signal},
    "udv_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_140_capitulation_signal},
    "udv_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_141_capitulation_signal},
    "udv_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_142_capitulation_signal},
    "udv_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_143_capitulation_signal},
    "udv_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_144_capitulation_signal},
    "udv_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_145_capitulation_signal},
    "udv_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_146_capitulation_signal},
    "udv_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_147_capitulation_signal},
    "udv_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_148_capitulation_signal},
    "udv_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_149_capitulation_signal},
    "udv_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_150_capitulation_signal},
}
