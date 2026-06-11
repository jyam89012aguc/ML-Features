"""Generated capitulation features for 57_spread_proxy: spread illiquidity proxy.
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

def spr_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def spr_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def spr_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def spr_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def spr_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def spr_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def spr_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def spr_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def spr_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def spr_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def spr_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def spr_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def spr_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def spr_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def spr_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def spr_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def spr_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def spr_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def spr_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def spr_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def spr_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def spr_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def spr_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def spr_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def spr_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def spr_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def spr_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def spr_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def spr_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def spr_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def spr_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def spr_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def spr_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def spr_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def spr_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def spr_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def spr_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def spr_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def spr_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def spr_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def spr_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def spr_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def spr_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def spr_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def spr_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def spr_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def spr_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def spr_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def spr_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def spr_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def spr_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def spr_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def spr_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def spr_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def spr_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def spr_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def spr_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def spr_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def spr_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

SPREAD_PROXY_REGISTRY_076_150 = {
    "spr_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_076_capitulation_signal},
    "spr_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_077_capitulation_signal},
    "spr_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_078_capitulation_signal},
    "spr_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_079_capitulation_signal},
    "spr_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_080_capitulation_signal},
    "spr_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_081_capitulation_signal},
    "spr_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_082_capitulation_signal},
    "spr_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_083_capitulation_signal},
    "spr_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_084_capitulation_signal},
    "spr_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_085_capitulation_signal},
    "spr_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_086_capitulation_signal},
    "spr_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_087_capitulation_signal},
    "spr_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_088_capitulation_signal},
    "spr_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_089_capitulation_signal},
    "spr_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_090_capitulation_signal},
    "spr_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_091_capitulation_signal},
    "spr_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_092_capitulation_signal},
    "spr_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_093_capitulation_signal},
    "spr_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_094_capitulation_signal},
    "spr_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_095_capitulation_signal},
    "spr_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_096_capitulation_signal},
    "spr_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_097_capitulation_signal},
    "spr_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_098_capitulation_signal},
    "spr_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_099_capitulation_signal},
    "spr_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_100_capitulation_signal},
    "spr_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_101_capitulation_signal},
    "spr_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_102_capitulation_signal},
    "spr_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_103_capitulation_signal},
    "spr_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_104_capitulation_signal},
    "spr_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_105_capitulation_signal},
    "spr_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_106_capitulation_signal},
    "spr_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_107_capitulation_signal},
    "spr_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_108_capitulation_signal},
    "spr_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_109_capitulation_signal},
    "spr_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_110_capitulation_signal},
    "spr_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_111_capitulation_signal},
    "spr_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_112_capitulation_signal},
    "spr_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_113_capitulation_signal},
    "spr_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_114_capitulation_signal},
    "spr_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_115_capitulation_signal},
    "spr_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_116_capitulation_signal},
    "spr_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_117_capitulation_signal},
    "spr_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_118_capitulation_signal},
    "spr_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_119_capitulation_signal},
    "spr_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_120_capitulation_signal},
    "spr_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_121_capitulation_signal},
    "spr_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_122_capitulation_signal},
    "spr_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_123_capitulation_signal},
    "spr_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_124_capitulation_signal},
    "spr_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_125_capitulation_signal},
    "spr_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_126_capitulation_signal},
    "spr_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_127_capitulation_signal},
    "spr_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_128_capitulation_signal},
    "spr_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_129_capitulation_signal},
    "spr_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_130_capitulation_signal},
    "spr_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_131_capitulation_signal},
    "spr_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_132_capitulation_signal},
    "spr_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_133_capitulation_signal},
    "spr_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_134_capitulation_signal},
    "spr_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_135_capitulation_signal},
    "spr_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_136_capitulation_signal},
    "spr_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_137_capitulation_signal},
    "spr_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_138_capitulation_signal},
    "spr_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_139_capitulation_signal},
    "spr_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_140_capitulation_signal},
    "spr_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_141_capitulation_signal},
    "spr_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_142_capitulation_signal},
    "spr_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_143_capitulation_signal},
    "spr_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_144_capitulation_signal},
    "spr_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_145_capitulation_signal},
    "spr_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_146_capitulation_signal},
    "spr_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_147_capitulation_signal},
    "spr_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_148_capitulation_signal},
    "spr_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_149_capitulation_signal},
    "spr_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_150_capitulation_signal},
}
