"""Generated capitulation features for 45_panic_bar_signatures: wide-range/long-tail bars.
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

def pbs_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def pbs_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def pbs_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def pbs_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def pbs_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def pbs_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def pbs_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def pbs_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def pbs_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def pbs_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def pbs_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def pbs_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def pbs_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def pbs_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def pbs_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def pbs_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def pbs_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def pbs_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def pbs_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def pbs_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def pbs_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def pbs_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def pbs_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def pbs_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def pbs_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def pbs_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def pbs_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def pbs_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def pbs_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def pbs_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def pbs_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def pbs_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def pbs_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def pbs_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def pbs_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def pbs_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def pbs_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def pbs_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def pbs_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def pbs_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def pbs_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def pbs_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def pbs_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def pbs_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def pbs_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def pbs_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def pbs_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def pbs_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def pbs_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def pbs_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def pbs_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def pbs_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def pbs_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def pbs_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def pbs_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def pbs_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def pbs_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def pbs_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def pbs_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

PANIC_BAR_SIGNATURES_REGISTRY_076_150 = {
    "pbs_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_076_capitulation_signal},
    "pbs_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_077_capitulation_signal},
    "pbs_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_078_capitulation_signal},
    "pbs_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_079_capitulation_signal},
    "pbs_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_080_capitulation_signal},
    "pbs_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_081_capitulation_signal},
    "pbs_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_082_capitulation_signal},
    "pbs_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_083_capitulation_signal},
    "pbs_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_084_capitulation_signal},
    "pbs_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_085_capitulation_signal},
    "pbs_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_086_capitulation_signal},
    "pbs_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_087_capitulation_signal},
    "pbs_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_088_capitulation_signal},
    "pbs_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_089_capitulation_signal},
    "pbs_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_090_capitulation_signal},
    "pbs_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_091_capitulation_signal},
    "pbs_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_092_capitulation_signal},
    "pbs_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_093_capitulation_signal},
    "pbs_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_094_capitulation_signal},
    "pbs_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_095_capitulation_signal},
    "pbs_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_096_capitulation_signal},
    "pbs_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_097_capitulation_signal},
    "pbs_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_098_capitulation_signal},
    "pbs_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_099_capitulation_signal},
    "pbs_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_100_capitulation_signal},
    "pbs_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_101_capitulation_signal},
    "pbs_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_102_capitulation_signal},
    "pbs_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_103_capitulation_signal},
    "pbs_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_104_capitulation_signal},
    "pbs_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_105_capitulation_signal},
    "pbs_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_106_capitulation_signal},
    "pbs_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_107_capitulation_signal},
    "pbs_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_108_capitulation_signal},
    "pbs_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_109_capitulation_signal},
    "pbs_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_110_capitulation_signal},
    "pbs_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_111_capitulation_signal},
    "pbs_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_112_capitulation_signal},
    "pbs_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_113_capitulation_signal},
    "pbs_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_114_capitulation_signal},
    "pbs_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_115_capitulation_signal},
    "pbs_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_116_capitulation_signal},
    "pbs_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_117_capitulation_signal},
    "pbs_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_118_capitulation_signal},
    "pbs_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_119_capitulation_signal},
    "pbs_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_120_capitulation_signal},
    "pbs_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_121_capitulation_signal},
    "pbs_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_122_capitulation_signal},
    "pbs_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_123_capitulation_signal},
    "pbs_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_124_capitulation_signal},
    "pbs_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_125_capitulation_signal},
    "pbs_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_126_capitulation_signal},
    "pbs_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_127_capitulation_signal},
    "pbs_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_128_capitulation_signal},
    "pbs_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_129_capitulation_signal},
    "pbs_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_130_capitulation_signal},
    "pbs_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_131_capitulation_signal},
    "pbs_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_132_capitulation_signal},
    "pbs_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_133_capitulation_signal},
    "pbs_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_134_capitulation_signal},
    "pbs_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_135_capitulation_signal},
    "pbs_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_136_capitulation_signal},
    "pbs_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_137_capitulation_signal},
    "pbs_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_138_capitulation_signal},
    "pbs_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_139_capitulation_signal},
    "pbs_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_140_capitulation_signal},
    "pbs_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_141_capitulation_signal},
    "pbs_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_142_capitulation_signal},
    "pbs_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_143_capitulation_signal},
    "pbs_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_144_capitulation_signal},
    "pbs_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_145_capitulation_signal},
    "pbs_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_146_capitulation_signal},
    "pbs_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_147_capitulation_signal},
    "pbs_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_148_capitulation_signal},
    "pbs_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_149_capitulation_signal},
    "pbs_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_150_capitulation_signal},
}
