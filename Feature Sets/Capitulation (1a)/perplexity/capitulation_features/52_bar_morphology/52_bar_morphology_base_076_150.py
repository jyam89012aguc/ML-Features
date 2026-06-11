"""Generated capitulation features for 52_bar_morphology: candlestick body/range stats.
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

def bmf_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def bmf_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def bmf_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def bmf_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def bmf_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def bmf_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def bmf_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def bmf_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def bmf_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def bmf_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def bmf_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def bmf_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def bmf_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def bmf_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def bmf_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def bmf_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def bmf_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def bmf_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def bmf_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def bmf_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def bmf_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def bmf_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def bmf_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def bmf_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def bmf_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def bmf_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def bmf_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def bmf_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def bmf_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def bmf_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def bmf_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def bmf_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def bmf_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def bmf_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def bmf_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def bmf_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def bmf_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def bmf_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def bmf_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def bmf_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def bmf_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def bmf_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def bmf_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def bmf_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def bmf_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def bmf_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def bmf_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def bmf_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def bmf_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def bmf_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def bmf_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def bmf_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def bmf_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def bmf_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def bmf_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def bmf_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def bmf_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def bmf_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def bmf_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

BAR_MORPHOLOGY_REGISTRY_076_150 = {
    "bmf_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_076_capitulation_signal},
    "bmf_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_077_capitulation_signal},
    "bmf_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_078_capitulation_signal},
    "bmf_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_079_capitulation_signal},
    "bmf_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_080_capitulation_signal},
    "bmf_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_081_capitulation_signal},
    "bmf_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_082_capitulation_signal},
    "bmf_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_083_capitulation_signal},
    "bmf_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_084_capitulation_signal},
    "bmf_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_085_capitulation_signal},
    "bmf_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_086_capitulation_signal},
    "bmf_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_087_capitulation_signal},
    "bmf_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_088_capitulation_signal},
    "bmf_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_089_capitulation_signal},
    "bmf_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_090_capitulation_signal},
    "bmf_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_091_capitulation_signal},
    "bmf_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_092_capitulation_signal},
    "bmf_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_093_capitulation_signal},
    "bmf_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_094_capitulation_signal},
    "bmf_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_095_capitulation_signal},
    "bmf_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_096_capitulation_signal},
    "bmf_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_097_capitulation_signal},
    "bmf_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_098_capitulation_signal},
    "bmf_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_099_capitulation_signal},
    "bmf_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_100_capitulation_signal},
    "bmf_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_101_capitulation_signal},
    "bmf_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_102_capitulation_signal},
    "bmf_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_103_capitulation_signal},
    "bmf_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_104_capitulation_signal},
    "bmf_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_105_capitulation_signal},
    "bmf_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_106_capitulation_signal},
    "bmf_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_107_capitulation_signal},
    "bmf_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_108_capitulation_signal},
    "bmf_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_109_capitulation_signal},
    "bmf_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_110_capitulation_signal},
    "bmf_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_111_capitulation_signal},
    "bmf_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_112_capitulation_signal},
    "bmf_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_113_capitulation_signal},
    "bmf_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_114_capitulation_signal},
    "bmf_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_115_capitulation_signal},
    "bmf_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_116_capitulation_signal},
    "bmf_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_117_capitulation_signal},
    "bmf_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_118_capitulation_signal},
    "bmf_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_119_capitulation_signal},
    "bmf_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_120_capitulation_signal},
    "bmf_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_121_capitulation_signal},
    "bmf_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_122_capitulation_signal},
    "bmf_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_123_capitulation_signal},
    "bmf_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_124_capitulation_signal},
    "bmf_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_125_capitulation_signal},
    "bmf_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_126_capitulation_signal},
    "bmf_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_127_capitulation_signal},
    "bmf_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_128_capitulation_signal},
    "bmf_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_129_capitulation_signal},
    "bmf_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_130_capitulation_signal},
    "bmf_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_131_capitulation_signal},
    "bmf_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_132_capitulation_signal},
    "bmf_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_133_capitulation_signal},
    "bmf_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_134_capitulation_signal},
    "bmf_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_135_capitulation_signal},
    "bmf_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_136_capitulation_signal},
    "bmf_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_137_capitulation_signal},
    "bmf_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_138_capitulation_signal},
    "bmf_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_139_capitulation_signal},
    "bmf_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_140_capitulation_signal},
    "bmf_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_141_capitulation_signal},
    "bmf_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_142_capitulation_signal},
    "bmf_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_143_capitulation_signal},
    "bmf_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_144_capitulation_signal},
    "bmf_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_145_capitulation_signal},
    "bmf_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_146_capitulation_signal},
    "bmf_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_147_capitulation_signal},
    "bmf_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_148_capitulation_signal},
    "bmf_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_149_capitulation_signal},
    "bmf_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_150_capitulation_signal},
}
