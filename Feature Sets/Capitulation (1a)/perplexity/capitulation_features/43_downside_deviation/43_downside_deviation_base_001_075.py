"""Generated capitulation features for 43_downside_deviation: downside-only dispersion.
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

def dsd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dsd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dsd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dsd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dsd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dsd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dsd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dsd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dsd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dsd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dsd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dsd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dsd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dsd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dsd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dsd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dsd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dsd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dsd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dsd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dsd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dsd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dsd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dsd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dsd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dsd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dsd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dsd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dsd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dsd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dsd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dsd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dsd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dsd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dsd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dsd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dsd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dsd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dsd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dsd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dsd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dsd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dsd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dsd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dsd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dsd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dsd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dsd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dsd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dsd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dsd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dsd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dsd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dsd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dsd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dsd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dsd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dsd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dsd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DOWNSIDE_DEVIATION_REGISTRY_001_075 = {
    "dsd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_001_capitulation_signal},
    "dsd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_002_capitulation_signal},
    "dsd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_003_capitulation_signal},
    "dsd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_004_capitulation_signal},
    "dsd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_005_capitulation_signal},
    "dsd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_006_capitulation_signal},
    "dsd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_007_capitulation_signal},
    "dsd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_008_capitulation_signal},
    "dsd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_009_capitulation_signal},
    "dsd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_010_capitulation_signal},
    "dsd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_011_capitulation_signal},
    "dsd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_012_capitulation_signal},
    "dsd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_013_capitulation_signal},
    "dsd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_014_capitulation_signal},
    "dsd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_015_capitulation_signal},
    "dsd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_016_capitulation_signal},
    "dsd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_017_capitulation_signal},
    "dsd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_018_capitulation_signal},
    "dsd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_019_capitulation_signal},
    "dsd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_020_capitulation_signal},
    "dsd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_021_capitulation_signal},
    "dsd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_022_capitulation_signal},
    "dsd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_023_capitulation_signal},
    "dsd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_024_capitulation_signal},
    "dsd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_025_capitulation_signal},
    "dsd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_026_capitulation_signal},
    "dsd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_027_capitulation_signal},
    "dsd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_028_capitulation_signal},
    "dsd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_029_capitulation_signal},
    "dsd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_030_capitulation_signal},
    "dsd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_031_capitulation_signal},
    "dsd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_032_capitulation_signal},
    "dsd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_033_capitulation_signal},
    "dsd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_034_capitulation_signal},
    "dsd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_035_capitulation_signal},
    "dsd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_036_capitulation_signal},
    "dsd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_037_capitulation_signal},
    "dsd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_038_capitulation_signal},
    "dsd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_039_capitulation_signal},
    "dsd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_040_capitulation_signal},
    "dsd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_041_capitulation_signal},
    "dsd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_042_capitulation_signal},
    "dsd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_043_capitulation_signal},
    "dsd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_044_capitulation_signal},
    "dsd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_045_capitulation_signal},
    "dsd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_046_capitulation_signal},
    "dsd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_047_capitulation_signal},
    "dsd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_048_capitulation_signal},
    "dsd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_049_capitulation_signal},
    "dsd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_050_capitulation_signal},
    "dsd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_051_capitulation_signal},
    "dsd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_052_capitulation_signal},
    "dsd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_053_capitulation_signal},
    "dsd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_054_capitulation_signal},
    "dsd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_055_capitulation_signal},
    "dsd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_056_capitulation_signal},
    "dsd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_057_capitulation_signal},
    "dsd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_058_capitulation_signal},
    "dsd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_059_capitulation_signal},
    "dsd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_060_capitulation_signal},
    "dsd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_061_capitulation_signal},
    "dsd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_062_capitulation_signal},
    "dsd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_063_capitulation_signal},
    "dsd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_064_capitulation_signal},
    "dsd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_065_capitulation_signal},
    "dsd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_066_capitulation_signal},
    "dsd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_067_capitulation_signal},
    "dsd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_068_capitulation_signal},
    "dsd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_069_capitulation_signal},
    "dsd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_070_capitulation_signal},
    "dsd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_071_capitulation_signal},
    "dsd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_072_capitulation_signal},
    "dsd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_073_capitulation_signal},
    "dsd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_074_capitulation_signal},
    "dsd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsd_075_capitulation_signal},
}
