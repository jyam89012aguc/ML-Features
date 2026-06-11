"""Generated capitulation features for 36_volatility_spike: realized volatility spikes.
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

def vsp_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vsp_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vsp_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vsp_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vsp_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vsp_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vsp_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vsp_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vsp_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vsp_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vsp_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vsp_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vsp_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vsp_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vsp_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vsp_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vsp_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vsp_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vsp_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vsp_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vsp_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vsp_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vsp_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vsp_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vsp_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vsp_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vsp_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vsp_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vsp_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vsp_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vsp_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vsp_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vsp_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vsp_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vsp_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vsp_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vsp_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vsp_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vsp_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vsp_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vsp_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vsp_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vsp_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vsp_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vsp_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vsp_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vsp_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vsp_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vsp_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vsp_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vsp_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vsp_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vsp_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vsp_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vsp_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vsp_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vsp_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vsp_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vsp_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vsp_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vsp_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLATILITY_SPIKE_REGISTRY_001_075 = {
    "vsp_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_001_capitulation_signal},
    "vsp_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_002_capitulation_signal},
    "vsp_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_003_capitulation_signal},
    "vsp_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_004_capitulation_signal},
    "vsp_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_005_capitulation_signal},
    "vsp_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_006_capitulation_signal},
    "vsp_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_007_capitulation_signal},
    "vsp_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_008_capitulation_signal},
    "vsp_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_009_capitulation_signal},
    "vsp_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_010_capitulation_signal},
    "vsp_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_011_capitulation_signal},
    "vsp_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_012_capitulation_signal},
    "vsp_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_013_capitulation_signal},
    "vsp_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_014_capitulation_signal},
    "vsp_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_015_capitulation_signal},
    "vsp_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_016_capitulation_signal},
    "vsp_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_017_capitulation_signal},
    "vsp_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_018_capitulation_signal},
    "vsp_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_019_capitulation_signal},
    "vsp_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_020_capitulation_signal},
    "vsp_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_021_capitulation_signal},
    "vsp_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_022_capitulation_signal},
    "vsp_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_023_capitulation_signal},
    "vsp_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_024_capitulation_signal},
    "vsp_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_025_capitulation_signal},
    "vsp_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_026_capitulation_signal},
    "vsp_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_027_capitulation_signal},
    "vsp_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_028_capitulation_signal},
    "vsp_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_029_capitulation_signal},
    "vsp_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_030_capitulation_signal},
    "vsp_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_031_capitulation_signal},
    "vsp_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_032_capitulation_signal},
    "vsp_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_033_capitulation_signal},
    "vsp_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_034_capitulation_signal},
    "vsp_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_035_capitulation_signal},
    "vsp_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_036_capitulation_signal},
    "vsp_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_037_capitulation_signal},
    "vsp_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_038_capitulation_signal},
    "vsp_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_039_capitulation_signal},
    "vsp_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_040_capitulation_signal},
    "vsp_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_041_capitulation_signal},
    "vsp_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_042_capitulation_signal},
    "vsp_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_043_capitulation_signal},
    "vsp_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_044_capitulation_signal},
    "vsp_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_045_capitulation_signal},
    "vsp_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_046_capitulation_signal},
    "vsp_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_047_capitulation_signal},
    "vsp_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_048_capitulation_signal},
    "vsp_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_049_capitulation_signal},
    "vsp_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_050_capitulation_signal},
    "vsp_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_051_capitulation_signal},
    "vsp_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_052_capitulation_signal},
    "vsp_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_053_capitulation_signal},
    "vsp_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_054_capitulation_signal},
    "vsp_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_055_capitulation_signal},
    "vsp_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_056_capitulation_signal},
    "vsp_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_057_capitulation_signal},
    "vsp_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_058_capitulation_signal},
    "vsp_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_059_capitulation_signal},
    "vsp_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_060_capitulation_signal},
    "vsp_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_061_capitulation_signal},
    "vsp_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_062_capitulation_signal},
    "vsp_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_063_capitulation_signal},
    "vsp_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_064_capitulation_signal},
    "vsp_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_065_capitulation_signal},
    "vsp_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_066_capitulation_signal},
    "vsp_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_067_capitulation_signal},
    "vsp_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_068_capitulation_signal},
    "vsp_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_069_capitulation_signal},
    "vsp_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_070_capitulation_signal},
    "vsp_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_071_capitulation_signal},
    "vsp_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_072_capitulation_signal},
    "vsp_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_073_capitulation_signal},
    "vsp_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_074_capitulation_signal},
    "vsp_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vsp_075_capitulation_signal},
}
