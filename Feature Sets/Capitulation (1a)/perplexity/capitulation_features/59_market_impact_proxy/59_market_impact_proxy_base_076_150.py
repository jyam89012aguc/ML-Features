"""Generated capitulation features for 59_market_impact_proxy: return per dollar-volume.
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

def mip_076_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1260, min_periods=max(3, 1260//4)).median())

def mip_077_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(63, min_periods=max(3, 63//4)).mean()

def mip_078_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_079_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(21, min_periods=max(3, 21//4)).mean()

def mip_080_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).skew()

def mip_081_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).kurt()

def mip_082_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(126, min_periods=max(3, 126//4)).median())

def mip_083_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 252)

def mip_084_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 504)

def mip_085_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(21, min_periods=max(3, 21//4)).mean(), _s(close).rolling(756, min_periods=max(3, 756//4)).mean()) - 1.0

def mip_086_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_087_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_088_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126) - _s(close).pct_change(5)

def mip_089_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_090_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).max()) - 1.0

def mip_091_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).min()) - 1.0

def mip_092_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63)

def mip_093_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 126)

def mip_094_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(252, min_periods=max(3, 252//4)).median())

def mip_095_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mip_096_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_097_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1008, min_periods=max(3, 1008//4)).mean()

def mip_098_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1260, min_periods=max(3, 1260//4)).skew()

def mip_099_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).kurt()

def mip_100_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(10, min_periods=max(3, 10//4)).median())

def mip_101_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 21)

def mip_102_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 42)

def mip_103_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(63, min_periods=max(3, 63//4)).mean()) - 1.0

def mip_104_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_105_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_106_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(504)

def mip_107_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_108_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1008, min_periods=max(3, 1008//4)).max()) - 1.0

def mip_109_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).min()) - 1.0

def mip_110_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(5)

def mip_111_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 10)

def mip_112_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(21, min_periods=max(3, 21//4)).median())

def mip_113_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mip_114_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_115_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(126, min_periods=max(3, 126//4)).mean()

def mip_116_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(252, min_periods=max(3, 252//4)).skew()

def mip_117_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).kurt()

def mip_118_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(756, min_periods=max(3, 756//4)).median())

def mip_119_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1008)

def mip_120_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 1260)

def mip_121_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(5, min_periods=max(3, 5//4)).mean()) - 1.0

def mip_122_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_123_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_124_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(42)

def mip_125_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_126_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(126, min_periods=max(3, 126//4)).max()) - 1.0

def mip_127_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).min()) - 1.0

def mip_128_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(504)

def mip_129_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 756)

def mip_130_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(1008, min_periods=max(3, 1008//4)).median())

def mip_131_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mip_132_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_133_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(10, min_periods=max(3, 10//4)).mean()

def mip_134_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(21, min_periods=max(3, 21//4)).skew()

def mip_135_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(42, min_periods=max(3, 42//4)).kurt()

def mip_136_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(63, min_periods=max(3, 63//4)).median())

def mip_137_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 126)

def mip_138_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 252)

def mip_139_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(504, min_periods=max(3, 504//4)).mean()) - 1.0

def mip_140_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_141_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_142_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(1260)

def mip_143_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_144_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).max()) - 1.0

def mip_145_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(21, min_periods=max(3, 21//4)).min()) - 1.0

def mip_146_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42)

def mip_147_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 63)

def mip_148_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(126, min_periods=max(3, 126//4)).median())

def mip_149_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mip_150_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

MARKET_IMPACT_PROXY_REGISTRY_076_150 = {
    "mip_076_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_076_capitulation_signal},
    "mip_077_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_077_capitulation_signal},
    "mip_078_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_078_capitulation_signal},
    "mip_079_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_079_capitulation_signal},
    "mip_080_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_080_capitulation_signal},
    "mip_081_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_081_capitulation_signal},
    "mip_082_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_082_capitulation_signal},
    "mip_083_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_083_capitulation_signal},
    "mip_084_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_084_capitulation_signal},
    "mip_085_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_085_capitulation_signal},
    "mip_086_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_086_capitulation_signal},
    "mip_087_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_087_capitulation_signal},
    "mip_088_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_088_capitulation_signal},
    "mip_089_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_089_capitulation_signal},
    "mip_090_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_090_capitulation_signal},
    "mip_091_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_091_capitulation_signal},
    "mip_092_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_092_capitulation_signal},
    "mip_093_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_093_capitulation_signal},
    "mip_094_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_094_capitulation_signal},
    "mip_095_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_095_capitulation_signal},
    "mip_096_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_096_capitulation_signal},
    "mip_097_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_097_capitulation_signal},
    "mip_098_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_098_capitulation_signal},
    "mip_099_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_099_capitulation_signal},
    "mip_100_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_100_capitulation_signal},
    "mip_101_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_101_capitulation_signal},
    "mip_102_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_102_capitulation_signal},
    "mip_103_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_103_capitulation_signal},
    "mip_104_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_104_capitulation_signal},
    "mip_105_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_105_capitulation_signal},
    "mip_106_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_106_capitulation_signal},
    "mip_107_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_107_capitulation_signal},
    "mip_108_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_108_capitulation_signal},
    "mip_109_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_109_capitulation_signal},
    "mip_110_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_110_capitulation_signal},
    "mip_111_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_111_capitulation_signal},
    "mip_112_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_112_capitulation_signal},
    "mip_113_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_113_capitulation_signal},
    "mip_114_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_114_capitulation_signal},
    "mip_115_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_115_capitulation_signal},
    "mip_116_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_116_capitulation_signal},
    "mip_117_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_117_capitulation_signal},
    "mip_118_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_118_capitulation_signal},
    "mip_119_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_119_capitulation_signal},
    "mip_120_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_120_capitulation_signal},
    "mip_121_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_121_capitulation_signal},
    "mip_122_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_122_capitulation_signal},
    "mip_123_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_123_capitulation_signal},
    "mip_124_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_124_capitulation_signal},
    "mip_125_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_125_capitulation_signal},
    "mip_126_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_126_capitulation_signal},
    "mip_127_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_127_capitulation_signal},
    "mip_128_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_128_capitulation_signal},
    "mip_129_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_129_capitulation_signal},
    "mip_130_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_130_capitulation_signal},
    "mip_131_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_131_capitulation_signal},
    "mip_132_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_132_capitulation_signal},
    "mip_133_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_133_capitulation_signal},
    "mip_134_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_134_capitulation_signal},
    "mip_135_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_135_capitulation_signal},
    "mip_136_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_136_capitulation_signal},
    "mip_137_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_137_capitulation_signal},
    "mip_138_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_138_capitulation_signal},
    "mip_139_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_139_capitulation_signal},
    "mip_140_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_140_capitulation_signal},
    "mip_141_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_141_capitulation_signal},
    "mip_142_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_142_capitulation_signal},
    "mip_143_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_143_capitulation_signal},
    "mip_144_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_144_capitulation_signal},
    "mip_145_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_145_capitulation_signal},
    "mip_146_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_146_capitulation_signal},
    "mip_147_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_147_capitulation_signal},
    "mip_148_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_148_capitulation_signal},
    "mip_149_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_149_capitulation_signal},
    "mip_150_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_150_capitulation_signal},
}
