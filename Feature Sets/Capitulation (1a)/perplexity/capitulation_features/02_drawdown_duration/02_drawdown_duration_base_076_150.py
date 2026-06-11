"""Generated capitulation features for 02_drawdown_duration: time in drawdown, days since high.
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

def ddur_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def ddur_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def ddur_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def ddur_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def ddur_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def ddur_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def ddur_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def ddur_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def ddur_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def ddur_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def ddur_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def ddur_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def ddur_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def ddur_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def ddur_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def ddur_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ddur_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def ddur_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def ddur_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def ddur_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def ddur_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def ddur_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def ddur_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def ddur_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def ddur_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def ddur_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def ddur_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def ddur_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def ddur_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def ddur_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ddur_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def ddur_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def ddur_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def ddur_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def ddur_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def ddur_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def ddur_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def ddur_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def ddur_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def ddur_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def ddur_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def ddur_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def ddur_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def ddur_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ddur_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def ddur_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def ddur_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def ddur_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def ddur_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def ddur_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def ddur_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def ddur_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def ddur_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def ddur_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def ddur_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def ddur_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def ddur_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def ddur_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ddur_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

DRAWDOWN_DURATION_REGISTRY_076_150 = {
    "ddur_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_076_capitulation_signal},
    "ddur_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_077_capitulation_signal},
    "ddur_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_078_capitulation_signal},
    "ddur_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_079_capitulation_signal},
    "ddur_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_080_capitulation_signal},
    "ddur_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_081_capitulation_signal},
    "ddur_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_082_capitulation_signal},
    "ddur_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_083_capitulation_signal},
    "ddur_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_084_capitulation_signal},
    "ddur_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_085_capitulation_signal},
    "ddur_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_086_capitulation_signal},
    "ddur_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_087_capitulation_signal},
    "ddur_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_088_capitulation_signal},
    "ddur_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_089_capitulation_signal},
    "ddur_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_090_capitulation_signal},
    "ddur_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_091_capitulation_signal},
    "ddur_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_092_capitulation_signal},
    "ddur_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_093_capitulation_signal},
    "ddur_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_094_capitulation_signal},
    "ddur_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_095_capitulation_signal},
    "ddur_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_096_capitulation_signal},
    "ddur_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_097_capitulation_signal},
    "ddur_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_098_capitulation_signal},
    "ddur_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_099_capitulation_signal},
    "ddur_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_100_capitulation_signal},
    "ddur_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_101_capitulation_signal},
    "ddur_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_102_capitulation_signal},
    "ddur_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_103_capitulation_signal},
    "ddur_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_104_capitulation_signal},
    "ddur_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_105_capitulation_signal},
    "ddur_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_106_capitulation_signal},
    "ddur_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_107_capitulation_signal},
    "ddur_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_108_capitulation_signal},
    "ddur_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_109_capitulation_signal},
    "ddur_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_110_capitulation_signal},
    "ddur_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_111_capitulation_signal},
    "ddur_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_112_capitulation_signal},
    "ddur_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_113_capitulation_signal},
    "ddur_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_114_capitulation_signal},
    "ddur_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_115_capitulation_signal},
    "ddur_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_116_capitulation_signal},
    "ddur_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_117_capitulation_signal},
    "ddur_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_118_capitulation_signal},
    "ddur_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_119_capitulation_signal},
    "ddur_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_120_capitulation_signal},
    "ddur_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_121_capitulation_signal},
    "ddur_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_122_capitulation_signal},
    "ddur_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_123_capitulation_signal},
    "ddur_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_124_capitulation_signal},
    "ddur_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_125_capitulation_signal},
    "ddur_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_126_capitulation_signal},
    "ddur_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_127_capitulation_signal},
    "ddur_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_128_capitulation_signal},
    "ddur_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_129_capitulation_signal},
    "ddur_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_130_capitulation_signal},
    "ddur_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_131_capitulation_signal},
    "ddur_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_132_capitulation_signal},
    "ddur_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_133_capitulation_signal},
    "ddur_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_134_capitulation_signal},
    "ddur_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_135_capitulation_signal},
    "ddur_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_136_capitulation_signal},
    "ddur_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_137_capitulation_signal},
    "ddur_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_138_capitulation_signal},
    "ddur_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_139_capitulation_signal},
    "ddur_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_140_capitulation_signal},
    "ddur_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_141_capitulation_signal},
    "ddur_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_142_capitulation_signal},
    "ddur_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_143_capitulation_signal},
    "ddur_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_144_capitulation_signal},
    "ddur_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_145_capitulation_signal},
    "ddur_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_146_capitulation_signal},
    "ddur_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_147_capitulation_signal},
    "ddur_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_148_capitulation_signal},
    "ddur_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_149_capitulation_signal},
    "ddur_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_150_capitulation_signal},
}
