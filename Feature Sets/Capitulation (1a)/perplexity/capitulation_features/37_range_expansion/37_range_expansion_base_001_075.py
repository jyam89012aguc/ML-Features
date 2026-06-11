"""Generated capitulation features for 37_range_expansion: true-range expansion.
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

def rex_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def rex_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def rex_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def rex_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def rex_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rex_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def rex_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def rex_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def rex_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def rex_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def rex_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def rex_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def rex_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def rex_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def rex_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def rex_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def rex_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def rex_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def rex_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rex_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def rex_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def rex_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def rex_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def rex_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def rex_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def rex_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def rex_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def rex_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def rex_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def rex_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def rex_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def rex_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def rex_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rex_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def rex_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def rex_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def rex_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def rex_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def rex_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def rex_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def rex_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def rex_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def rex_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def rex_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def rex_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def rex_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def rex_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rex_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rex_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rex_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def rex_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def rex_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def rex_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def rex_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def rex_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def rex_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rex_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def rex_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rex_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def rex_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def rex_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def rex_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

RANGE_EXPANSION_REGISTRY_001_075 = {
    "rex_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_001_capitulation_signal},
    "rex_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_002_capitulation_signal},
    "rex_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_003_capitulation_signal},
    "rex_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_004_capitulation_signal},
    "rex_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_005_capitulation_signal},
    "rex_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_006_capitulation_signal},
    "rex_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_007_capitulation_signal},
    "rex_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_008_capitulation_signal},
    "rex_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_009_capitulation_signal},
    "rex_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_010_capitulation_signal},
    "rex_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_011_capitulation_signal},
    "rex_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_012_capitulation_signal},
    "rex_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_013_capitulation_signal},
    "rex_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_014_capitulation_signal},
    "rex_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_015_capitulation_signal},
    "rex_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_016_capitulation_signal},
    "rex_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_017_capitulation_signal},
    "rex_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_018_capitulation_signal},
    "rex_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_019_capitulation_signal},
    "rex_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_020_capitulation_signal},
    "rex_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_021_capitulation_signal},
    "rex_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_022_capitulation_signal},
    "rex_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_023_capitulation_signal},
    "rex_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_024_capitulation_signal},
    "rex_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_025_capitulation_signal},
    "rex_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_026_capitulation_signal},
    "rex_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_027_capitulation_signal},
    "rex_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_028_capitulation_signal},
    "rex_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_029_capitulation_signal},
    "rex_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_030_capitulation_signal},
    "rex_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_031_capitulation_signal},
    "rex_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_032_capitulation_signal},
    "rex_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_033_capitulation_signal},
    "rex_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_034_capitulation_signal},
    "rex_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_035_capitulation_signal},
    "rex_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_036_capitulation_signal},
    "rex_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_037_capitulation_signal},
    "rex_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_038_capitulation_signal},
    "rex_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_039_capitulation_signal},
    "rex_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_040_capitulation_signal},
    "rex_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_041_capitulation_signal},
    "rex_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_042_capitulation_signal},
    "rex_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_043_capitulation_signal},
    "rex_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_044_capitulation_signal},
    "rex_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_045_capitulation_signal},
    "rex_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_046_capitulation_signal},
    "rex_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_047_capitulation_signal},
    "rex_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_048_capitulation_signal},
    "rex_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_049_capitulation_signal},
    "rex_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_050_capitulation_signal},
    "rex_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_051_capitulation_signal},
    "rex_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_052_capitulation_signal},
    "rex_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_053_capitulation_signal},
    "rex_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_054_capitulation_signal},
    "rex_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_055_capitulation_signal},
    "rex_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_056_capitulation_signal},
    "rex_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_057_capitulation_signal},
    "rex_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_058_capitulation_signal},
    "rex_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_059_capitulation_signal},
    "rex_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_060_capitulation_signal},
    "rex_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_061_capitulation_signal},
    "rex_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_062_capitulation_signal},
    "rex_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_063_capitulation_signal},
    "rex_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_064_capitulation_signal},
    "rex_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_065_capitulation_signal},
    "rex_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_066_capitulation_signal},
    "rex_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_067_capitulation_signal},
    "rex_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_068_capitulation_signal},
    "rex_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_069_capitulation_signal},
    "rex_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_070_capitulation_signal},
    "rex_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_071_capitulation_signal},
    "rex_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_072_capitulation_signal},
    "rex_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_073_capitulation_signal},
    "rex_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_074_capitulation_signal},
    "rex_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rex_075_capitulation_signal},
}
