"""Generated capitulation features for 17_volume_climax: single-day extreme volume events.
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

def vcx_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def vcx_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def vcx_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def vcx_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def vcx_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def vcx_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def vcx_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def vcx_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def vcx_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def vcx_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def vcx_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def vcx_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def vcx_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def vcx_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def vcx_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def vcx_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vcx_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def vcx_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def vcx_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def vcx_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def vcx_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def vcx_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def vcx_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def vcx_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def vcx_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def vcx_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def vcx_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def vcx_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def vcx_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def vcx_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vcx_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def vcx_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def vcx_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def vcx_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def vcx_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def vcx_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def vcx_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def vcx_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def vcx_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def vcx_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def vcx_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def vcx_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def vcx_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def vcx_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vcx_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def vcx_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def vcx_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def vcx_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def vcx_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def vcx_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def vcx_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def vcx_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def vcx_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def vcx_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def vcx_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def vcx_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def vcx_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def vcx_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vcx_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

VOLUME_CLIMAX_REGISTRY_076_150 = {
    "vcx_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_076_capitulation_signal},
    "vcx_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_077_capitulation_signal},
    "vcx_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_078_capitulation_signal},
    "vcx_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_079_capitulation_signal},
    "vcx_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_080_capitulation_signal},
    "vcx_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_081_capitulation_signal},
    "vcx_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_082_capitulation_signal},
    "vcx_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_083_capitulation_signal},
    "vcx_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_084_capitulation_signal},
    "vcx_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_085_capitulation_signal},
    "vcx_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_086_capitulation_signal},
    "vcx_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_087_capitulation_signal},
    "vcx_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_088_capitulation_signal},
    "vcx_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_089_capitulation_signal},
    "vcx_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_090_capitulation_signal},
    "vcx_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_091_capitulation_signal},
    "vcx_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_092_capitulation_signal},
    "vcx_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_093_capitulation_signal},
    "vcx_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_094_capitulation_signal},
    "vcx_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_095_capitulation_signal},
    "vcx_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_096_capitulation_signal},
    "vcx_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_097_capitulation_signal},
    "vcx_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_098_capitulation_signal},
    "vcx_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_099_capitulation_signal},
    "vcx_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_100_capitulation_signal},
    "vcx_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_101_capitulation_signal},
    "vcx_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_102_capitulation_signal},
    "vcx_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_103_capitulation_signal},
    "vcx_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_104_capitulation_signal},
    "vcx_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_105_capitulation_signal},
    "vcx_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_106_capitulation_signal},
    "vcx_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_107_capitulation_signal},
    "vcx_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_108_capitulation_signal},
    "vcx_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_109_capitulation_signal},
    "vcx_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_110_capitulation_signal},
    "vcx_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_111_capitulation_signal},
    "vcx_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_112_capitulation_signal},
    "vcx_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_113_capitulation_signal},
    "vcx_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_114_capitulation_signal},
    "vcx_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_115_capitulation_signal},
    "vcx_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_116_capitulation_signal},
    "vcx_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_117_capitulation_signal},
    "vcx_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_118_capitulation_signal},
    "vcx_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_119_capitulation_signal},
    "vcx_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_120_capitulation_signal},
    "vcx_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_121_capitulation_signal},
    "vcx_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_122_capitulation_signal},
    "vcx_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_123_capitulation_signal},
    "vcx_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_124_capitulation_signal},
    "vcx_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_125_capitulation_signal},
    "vcx_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_126_capitulation_signal},
    "vcx_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_127_capitulation_signal},
    "vcx_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_128_capitulation_signal},
    "vcx_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_129_capitulation_signal},
    "vcx_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_130_capitulation_signal},
    "vcx_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_131_capitulation_signal},
    "vcx_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_132_capitulation_signal},
    "vcx_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_133_capitulation_signal},
    "vcx_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_134_capitulation_signal},
    "vcx_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_135_capitulation_signal},
    "vcx_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_136_capitulation_signal},
    "vcx_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_137_capitulation_signal},
    "vcx_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_138_capitulation_signal},
    "vcx_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_139_capitulation_signal},
    "vcx_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_140_capitulation_signal},
    "vcx_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_141_capitulation_signal},
    "vcx_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_142_capitulation_signal},
    "vcx_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_143_capitulation_signal},
    "vcx_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_144_capitulation_signal},
    "vcx_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_145_capitulation_signal},
    "vcx_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_146_capitulation_signal},
    "vcx_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_147_capitulation_signal},
    "vcx_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_148_capitulation_signal},
    "vcx_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_149_capitulation_signal},
    "vcx_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_150_capitulation_signal},
}
