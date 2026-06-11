"""Generated capitulation features for 25_momentum_decay: trailing return decay.
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

def mdc_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def mdc_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def mdc_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def mdc_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def mdc_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def mdc_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def mdc_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def mdc_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def mdc_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def mdc_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def mdc_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def mdc_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def mdc_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def mdc_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def mdc_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def mdc_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mdc_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def mdc_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def mdc_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def mdc_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def mdc_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def mdc_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def mdc_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def mdc_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def mdc_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def mdc_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def mdc_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def mdc_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def mdc_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def mdc_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mdc_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def mdc_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def mdc_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def mdc_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def mdc_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def mdc_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def mdc_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def mdc_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def mdc_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def mdc_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def mdc_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def mdc_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def mdc_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def mdc_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mdc_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def mdc_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def mdc_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def mdc_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def mdc_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def mdc_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def mdc_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def mdc_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def mdc_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def mdc_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def mdc_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def mdc_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def mdc_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def mdc_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mdc_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

MOMENTUM_DECAY_REGISTRY_076_150 = {
    "mdc_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_076_capitulation_signal},
    "mdc_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_077_capitulation_signal},
    "mdc_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_078_capitulation_signal},
    "mdc_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_079_capitulation_signal},
    "mdc_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_080_capitulation_signal},
    "mdc_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_081_capitulation_signal},
    "mdc_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_082_capitulation_signal},
    "mdc_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_083_capitulation_signal},
    "mdc_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_084_capitulation_signal},
    "mdc_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_085_capitulation_signal},
    "mdc_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_086_capitulation_signal},
    "mdc_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_087_capitulation_signal},
    "mdc_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_088_capitulation_signal},
    "mdc_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_089_capitulation_signal},
    "mdc_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_090_capitulation_signal},
    "mdc_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_091_capitulation_signal},
    "mdc_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_092_capitulation_signal},
    "mdc_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_093_capitulation_signal},
    "mdc_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_094_capitulation_signal},
    "mdc_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_095_capitulation_signal},
    "mdc_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_096_capitulation_signal},
    "mdc_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_097_capitulation_signal},
    "mdc_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_098_capitulation_signal},
    "mdc_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_099_capitulation_signal},
    "mdc_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_100_capitulation_signal},
    "mdc_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_101_capitulation_signal},
    "mdc_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_102_capitulation_signal},
    "mdc_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_103_capitulation_signal},
    "mdc_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_104_capitulation_signal},
    "mdc_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_105_capitulation_signal},
    "mdc_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_106_capitulation_signal},
    "mdc_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_107_capitulation_signal},
    "mdc_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_108_capitulation_signal},
    "mdc_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_109_capitulation_signal},
    "mdc_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_110_capitulation_signal},
    "mdc_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_111_capitulation_signal},
    "mdc_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_112_capitulation_signal},
    "mdc_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_113_capitulation_signal},
    "mdc_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_114_capitulation_signal},
    "mdc_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_115_capitulation_signal},
    "mdc_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_116_capitulation_signal},
    "mdc_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_117_capitulation_signal},
    "mdc_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_118_capitulation_signal},
    "mdc_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_119_capitulation_signal},
    "mdc_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_120_capitulation_signal},
    "mdc_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_121_capitulation_signal},
    "mdc_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_122_capitulation_signal},
    "mdc_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_123_capitulation_signal},
    "mdc_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_124_capitulation_signal},
    "mdc_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_125_capitulation_signal},
    "mdc_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_126_capitulation_signal},
    "mdc_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_127_capitulation_signal},
    "mdc_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_128_capitulation_signal},
    "mdc_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_129_capitulation_signal},
    "mdc_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_130_capitulation_signal},
    "mdc_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_131_capitulation_signal},
    "mdc_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_132_capitulation_signal},
    "mdc_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_133_capitulation_signal},
    "mdc_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_134_capitulation_signal},
    "mdc_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_135_capitulation_signal},
    "mdc_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_136_capitulation_signal},
    "mdc_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_137_capitulation_signal},
    "mdc_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_138_capitulation_signal},
    "mdc_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_139_capitulation_signal},
    "mdc_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_140_capitulation_signal},
    "mdc_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_141_capitulation_signal},
    "mdc_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_142_capitulation_signal},
    "mdc_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_143_capitulation_signal},
    "mdc_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_144_capitulation_signal},
    "mdc_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_145_capitulation_signal},
    "mdc_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_146_capitulation_signal},
    "mdc_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_147_capitulation_signal},
    "mdc_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_148_capitulation_signal},
    "mdc_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_149_capitulation_signal},
    "mdc_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_150_capitulation_signal},
}
