"""Generated capitulation features for 51_shadow_wick_analysis: wick ratios.
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

def swk_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def swk_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def swk_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def swk_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def swk_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def swk_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def swk_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def swk_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def swk_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def swk_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def swk_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def swk_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def swk_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def swk_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def swk_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def swk_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def swk_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def swk_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def swk_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def swk_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def swk_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def swk_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def swk_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def swk_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def swk_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def swk_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def swk_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def swk_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def swk_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def swk_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def swk_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def swk_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def swk_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def swk_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def swk_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def swk_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def swk_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def swk_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def swk_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def swk_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def swk_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def swk_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def swk_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def swk_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def swk_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def swk_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def swk_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def swk_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def swk_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def swk_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def swk_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def swk_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def swk_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def swk_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def swk_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def swk_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def swk_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def swk_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def swk_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

SHADOW_WICK_ANALYSIS_REGISTRY_076_150 = {
    "swk_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_076_capitulation_signal},
    "swk_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_077_capitulation_signal},
    "swk_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_078_capitulation_signal},
    "swk_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_079_capitulation_signal},
    "swk_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_080_capitulation_signal},
    "swk_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_081_capitulation_signal},
    "swk_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_082_capitulation_signal},
    "swk_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_083_capitulation_signal},
    "swk_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_084_capitulation_signal},
    "swk_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_085_capitulation_signal},
    "swk_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_086_capitulation_signal},
    "swk_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_087_capitulation_signal},
    "swk_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_088_capitulation_signal},
    "swk_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_089_capitulation_signal},
    "swk_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_090_capitulation_signal},
    "swk_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_091_capitulation_signal},
    "swk_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_092_capitulation_signal},
    "swk_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_093_capitulation_signal},
    "swk_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_094_capitulation_signal},
    "swk_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_095_capitulation_signal},
    "swk_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_096_capitulation_signal},
    "swk_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_097_capitulation_signal},
    "swk_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_098_capitulation_signal},
    "swk_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_099_capitulation_signal},
    "swk_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_100_capitulation_signal},
    "swk_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_101_capitulation_signal},
    "swk_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_102_capitulation_signal},
    "swk_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_103_capitulation_signal},
    "swk_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_104_capitulation_signal},
    "swk_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_105_capitulation_signal},
    "swk_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_106_capitulation_signal},
    "swk_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_107_capitulation_signal},
    "swk_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_108_capitulation_signal},
    "swk_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_109_capitulation_signal},
    "swk_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_110_capitulation_signal},
    "swk_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_111_capitulation_signal},
    "swk_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_112_capitulation_signal},
    "swk_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_113_capitulation_signal},
    "swk_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_114_capitulation_signal},
    "swk_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_115_capitulation_signal},
    "swk_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_116_capitulation_signal},
    "swk_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_117_capitulation_signal},
    "swk_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_118_capitulation_signal},
    "swk_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_119_capitulation_signal},
    "swk_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_120_capitulation_signal},
    "swk_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_121_capitulation_signal},
    "swk_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_122_capitulation_signal},
    "swk_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_123_capitulation_signal},
    "swk_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_124_capitulation_signal},
    "swk_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_125_capitulation_signal},
    "swk_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_126_capitulation_signal},
    "swk_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_127_capitulation_signal},
    "swk_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_128_capitulation_signal},
    "swk_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_129_capitulation_signal},
    "swk_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_130_capitulation_signal},
    "swk_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_131_capitulation_signal},
    "swk_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_132_capitulation_signal},
    "swk_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_133_capitulation_signal},
    "swk_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_134_capitulation_signal},
    "swk_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_135_capitulation_signal},
    "swk_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_136_capitulation_signal},
    "swk_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_137_capitulation_signal},
    "swk_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_138_capitulation_signal},
    "swk_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_139_capitulation_signal},
    "swk_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_140_capitulation_signal},
    "swk_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_141_capitulation_signal},
    "swk_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_142_capitulation_signal},
    "swk_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_143_capitulation_signal},
    "swk_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_144_capitulation_signal},
    "swk_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_145_capitulation_signal},
    "swk_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_146_capitulation_signal},
    "swk_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_147_capitulation_signal},
    "swk_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_148_capitulation_signal},
    "swk_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_149_capitulation_signal},
    "swk_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_150_capitulation_signal},
}
