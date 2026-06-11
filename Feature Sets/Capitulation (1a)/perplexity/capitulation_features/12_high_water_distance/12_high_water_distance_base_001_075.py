"""Generated capitulation features for 12_high_water_distance: distance/time from prior all-time high.
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

def hwd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def hwd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def hwd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def hwd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def hwd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def hwd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def hwd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def hwd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def hwd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def hwd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def hwd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def hwd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def hwd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def hwd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def hwd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def hwd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def hwd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def hwd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def hwd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def hwd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def hwd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def hwd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def hwd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def hwd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def hwd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def hwd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def hwd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def hwd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def hwd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def hwd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def hwd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def hwd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def hwd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def hwd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def hwd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def hwd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def hwd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def hwd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def hwd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def hwd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def hwd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def hwd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def hwd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def hwd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def hwd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def hwd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def hwd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def hwd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def hwd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def hwd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def hwd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def hwd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def hwd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def hwd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def hwd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def hwd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def hwd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def hwd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def hwd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def hwd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def hwd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

HIGH_WATER_DISTANCE_REGISTRY_001_075 = {
    "hwd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_001_capitulation_signal},
    "hwd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_002_capitulation_signal},
    "hwd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_003_capitulation_signal},
    "hwd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_004_capitulation_signal},
    "hwd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_005_capitulation_signal},
    "hwd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_006_capitulation_signal},
    "hwd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_007_capitulation_signal},
    "hwd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_008_capitulation_signal},
    "hwd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_009_capitulation_signal},
    "hwd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_010_capitulation_signal},
    "hwd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_011_capitulation_signal},
    "hwd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_012_capitulation_signal},
    "hwd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_013_capitulation_signal},
    "hwd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_014_capitulation_signal},
    "hwd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_015_capitulation_signal},
    "hwd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_016_capitulation_signal},
    "hwd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_017_capitulation_signal},
    "hwd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_018_capitulation_signal},
    "hwd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_019_capitulation_signal},
    "hwd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_020_capitulation_signal},
    "hwd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_021_capitulation_signal},
    "hwd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_022_capitulation_signal},
    "hwd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_023_capitulation_signal},
    "hwd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_024_capitulation_signal},
    "hwd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_025_capitulation_signal},
    "hwd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_026_capitulation_signal},
    "hwd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_027_capitulation_signal},
    "hwd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_028_capitulation_signal},
    "hwd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_029_capitulation_signal},
    "hwd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_030_capitulation_signal},
    "hwd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_031_capitulation_signal},
    "hwd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_032_capitulation_signal},
    "hwd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_033_capitulation_signal},
    "hwd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_034_capitulation_signal},
    "hwd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_035_capitulation_signal},
    "hwd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_036_capitulation_signal},
    "hwd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_037_capitulation_signal},
    "hwd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_038_capitulation_signal},
    "hwd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_039_capitulation_signal},
    "hwd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_040_capitulation_signal},
    "hwd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_041_capitulation_signal},
    "hwd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_042_capitulation_signal},
    "hwd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_043_capitulation_signal},
    "hwd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_044_capitulation_signal},
    "hwd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_045_capitulation_signal},
    "hwd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_046_capitulation_signal},
    "hwd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_047_capitulation_signal},
    "hwd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_048_capitulation_signal},
    "hwd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_049_capitulation_signal},
    "hwd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_050_capitulation_signal},
    "hwd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_051_capitulation_signal},
    "hwd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_052_capitulation_signal},
    "hwd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_053_capitulation_signal},
    "hwd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_054_capitulation_signal},
    "hwd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_055_capitulation_signal},
    "hwd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_056_capitulation_signal},
    "hwd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_057_capitulation_signal},
    "hwd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_058_capitulation_signal},
    "hwd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_059_capitulation_signal},
    "hwd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_060_capitulation_signal},
    "hwd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_061_capitulation_signal},
    "hwd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_062_capitulation_signal},
    "hwd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_063_capitulation_signal},
    "hwd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_064_capitulation_signal},
    "hwd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_065_capitulation_signal},
    "hwd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_066_capitulation_signal},
    "hwd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_067_capitulation_signal},
    "hwd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_068_capitulation_signal},
    "hwd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_069_capitulation_signal},
    "hwd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_070_capitulation_signal},
    "hwd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_071_capitulation_signal},
    "hwd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_072_capitulation_signal},
    "hwd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_073_capitulation_signal},
    "hwd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_074_capitulation_signal},
    "hwd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": hwd_075_capitulation_signal},
}
