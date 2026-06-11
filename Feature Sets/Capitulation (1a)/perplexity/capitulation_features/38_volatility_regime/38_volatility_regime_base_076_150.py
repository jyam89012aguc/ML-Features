"""Generated capitulation features for 38_volatility_regime: volatility regime shift.
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

def vrg_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vrg_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vrg_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vrg_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vrg_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vrg_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vrg_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vrg_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vrg_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vrg_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vrg_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vrg_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vrg_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vrg_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vrg_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vrg_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vrg_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vrg_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vrg_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vrg_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vrg_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vrg_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vrg_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vrg_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vrg_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vrg_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vrg_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vrg_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vrg_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vrg_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vrg_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vrg_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vrg_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vrg_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vrg_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vrg_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vrg_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vrg_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vrg_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vrg_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vrg_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vrg_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vrg_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vrg_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vrg_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vrg_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vrg_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vrg_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vrg_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vrg_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vrg_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vrg_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vrg_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vrg_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vrg_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vrg_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vrg_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vrg_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vrg_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLATILITY_REGIME_REGISTRY_076_150 = {
    "vrg_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_076_capitulation_signal},
    "vrg_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_077_capitulation_signal},
    "vrg_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_078_capitulation_signal},
    "vrg_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_079_capitulation_signal},
    "vrg_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_080_capitulation_signal},
    "vrg_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_081_capitulation_signal},
    "vrg_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_082_capitulation_signal},
    "vrg_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_083_capitulation_signal},
    "vrg_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_084_capitulation_signal},
    "vrg_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_085_capitulation_signal},
    "vrg_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_086_capitulation_signal},
    "vrg_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_087_capitulation_signal},
    "vrg_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_088_capitulation_signal},
    "vrg_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_089_capitulation_signal},
    "vrg_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_090_capitulation_signal},
    "vrg_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_091_capitulation_signal},
    "vrg_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_092_capitulation_signal},
    "vrg_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_093_capitulation_signal},
    "vrg_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_094_capitulation_signal},
    "vrg_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_095_capitulation_signal},
    "vrg_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_096_capitulation_signal},
    "vrg_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_097_capitulation_signal},
    "vrg_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_098_capitulation_signal},
    "vrg_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_099_capitulation_signal},
    "vrg_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_100_capitulation_signal},
    "vrg_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_101_capitulation_signal},
    "vrg_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_102_capitulation_signal},
    "vrg_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_103_capitulation_signal},
    "vrg_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_104_capitulation_signal},
    "vrg_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_105_capitulation_signal},
    "vrg_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_106_capitulation_signal},
    "vrg_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_107_capitulation_signal},
    "vrg_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_108_capitulation_signal},
    "vrg_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_109_capitulation_signal},
    "vrg_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_110_capitulation_signal},
    "vrg_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_111_capitulation_signal},
    "vrg_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_112_capitulation_signal},
    "vrg_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_113_capitulation_signal},
    "vrg_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_114_capitulation_signal},
    "vrg_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_115_capitulation_signal},
    "vrg_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_116_capitulation_signal},
    "vrg_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_117_capitulation_signal},
    "vrg_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_118_capitulation_signal},
    "vrg_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_119_capitulation_signal},
    "vrg_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_120_capitulation_signal},
    "vrg_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_121_capitulation_signal},
    "vrg_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_122_capitulation_signal},
    "vrg_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_123_capitulation_signal},
    "vrg_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_124_capitulation_signal},
    "vrg_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_125_capitulation_signal},
    "vrg_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_126_capitulation_signal},
    "vrg_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_127_capitulation_signal},
    "vrg_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_128_capitulation_signal},
    "vrg_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_129_capitulation_signal},
    "vrg_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_130_capitulation_signal},
    "vrg_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_131_capitulation_signal},
    "vrg_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_132_capitulation_signal},
    "vrg_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_133_capitulation_signal},
    "vrg_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_134_capitulation_signal},
    "vrg_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_135_capitulation_signal},
    "vrg_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_136_capitulation_signal},
    "vrg_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_137_capitulation_signal},
    "vrg_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_138_capitulation_signal},
    "vrg_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_139_capitulation_signal},
    "vrg_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_140_capitulation_signal},
    "vrg_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_141_capitulation_signal},
    "vrg_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_142_capitulation_signal},
    "vrg_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_143_capitulation_signal},
    "vrg_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_144_capitulation_signal},
    "vrg_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_145_capitulation_signal},
    "vrg_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_146_capitulation_signal},
    "vrg_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_147_capitulation_signal},
    "vrg_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_148_capitulation_signal},
    "vrg_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_149_capitulation_signal},
    "vrg_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_150_capitulation_signal},
}
