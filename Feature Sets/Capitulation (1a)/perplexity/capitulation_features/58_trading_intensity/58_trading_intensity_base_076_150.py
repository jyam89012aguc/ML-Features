"""Generated capitulation features for 58_trading_intensity: trade-frequency proxies.
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

def tin_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def tin_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def tin_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def tin_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def tin_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def tin_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def tin_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def tin_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def tin_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def tin_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def tin_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def tin_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def tin_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def tin_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def tin_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def tin_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tin_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def tin_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def tin_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def tin_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def tin_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def tin_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def tin_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def tin_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def tin_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def tin_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def tin_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def tin_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def tin_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def tin_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tin_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def tin_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def tin_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def tin_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def tin_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def tin_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def tin_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def tin_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def tin_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def tin_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def tin_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def tin_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def tin_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def tin_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tin_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def tin_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def tin_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def tin_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def tin_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def tin_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def tin_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def tin_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def tin_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def tin_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def tin_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def tin_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def tin_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def tin_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tin_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

TRADING_INTENSITY_REGISTRY_076_150 = {
    "tin_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_076_capitulation_signal},
    "tin_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_077_capitulation_signal},
    "tin_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_078_capitulation_signal},
    "tin_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_079_capitulation_signal},
    "tin_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_080_capitulation_signal},
    "tin_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_081_capitulation_signal},
    "tin_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_082_capitulation_signal},
    "tin_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_083_capitulation_signal},
    "tin_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_084_capitulation_signal},
    "tin_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_085_capitulation_signal},
    "tin_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_086_capitulation_signal},
    "tin_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_087_capitulation_signal},
    "tin_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_088_capitulation_signal},
    "tin_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_089_capitulation_signal},
    "tin_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_090_capitulation_signal},
    "tin_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_091_capitulation_signal},
    "tin_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_092_capitulation_signal},
    "tin_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_093_capitulation_signal},
    "tin_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_094_capitulation_signal},
    "tin_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_095_capitulation_signal},
    "tin_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_096_capitulation_signal},
    "tin_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_097_capitulation_signal},
    "tin_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_098_capitulation_signal},
    "tin_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_099_capitulation_signal},
    "tin_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_100_capitulation_signal},
    "tin_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_101_capitulation_signal},
    "tin_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_102_capitulation_signal},
    "tin_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_103_capitulation_signal},
    "tin_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_104_capitulation_signal},
    "tin_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_105_capitulation_signal},
    "tin_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_106_capitulation_signal},
    "tin_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_107_capitulation_signal},
    "tin_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_108_capitulation_signal},
    "tin_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_109_capitulation_signal},
    "tin_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_110_capitulation_signal},
    "tin_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_111_capitulation_signal},
    "tin_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_112_capitulation_signal},
    "tin_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_113_capitulation_signal},
    "tin_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_114_capitulation_signal},
    "tin_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_115_capitulation_signal},
    "tin_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_116_capitulation_signal},
    "tin_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_117_capitulation_signal},
    "tin_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_118_capitulation_signal},
    "tin_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_119_capitulation_signal},
    "tin_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_120_capitulation_signal},
    "tin_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_121_capitulation_signal},
    "tin_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_122_capitulation_signal},
    "tin_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_123_capitulation_signal},
    "tin_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_124_capitulation_signal},
    "tin_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_125_capitulation_signal},
    "tin_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_126_capitulation_signal},
    "tin_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_127_capitulation_signal},
    "tin_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_128_capitulation_signal},
    "tin_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_129_capitulation_signal},
    "tin_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_130_capitulation_signal},
    "tin_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_131_capitulation_signal},
    "tin_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_132_capitulation_signal},
    "tin_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_133_capitulation_signal},
    "tin_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_134_capitulation_signal},
    "tin_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_135_capitulation_signal},
    "tin_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_136_capitulation_signal},
    "tin_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_137_capitulation_signal},
    "tin_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_138_capitulation_signal},
    "tin_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_139_capitulation_signal},
    "tin_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_140_capitulation_signal},
    "tin_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_141_capitulation_signal},
    "tin_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_142_capitulation_signal},
    "tin_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_143_capitulation_signal},
    "tin_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_144_capitulation_signal},
    "tin_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_145_capitulation_signal},
    "tin_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_146_capitulation_signal},
    "tin_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_147_capitulation_signal},
    "tin_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_148_capitulation_signal},
    "tin_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_149_capitulation_signal},
    "tin_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_150_capitulation_signal},
}
