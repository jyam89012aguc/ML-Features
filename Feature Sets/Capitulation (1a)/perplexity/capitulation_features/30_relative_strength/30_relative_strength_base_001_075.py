"""Generated capitulation features for 30_relative_strength: price vs moving averages.
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

def rst_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def rst_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def rst_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def rst_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def rst_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rst_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def rst_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def rst_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def rst_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def rst_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def rst_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def rst_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def rst_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def rst_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def rst_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def rst_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def rst_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def rst_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def rst_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rst_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def rst_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def rst_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def rst_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def rst_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def rst_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def rst_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def rst_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def rst_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def rst_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def rst_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def rst_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def rst_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def rst_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rst_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def rst_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def rst_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def rst_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def rst_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def rst_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def rst_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def rst_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def rst_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def rst_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def rst_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def rst_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def rst_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def rst_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rst_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rst_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rst_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def rst_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def rst_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def rst_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def rst_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def rst_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def rst_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rst_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def rst_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rst_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def rst_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def rst_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def rst_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

RELATIVE_STRENGTH_REGISTRY_001_075 = {
    "rst_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_001_capitulation_signal},
    "rst_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_002_capitulation_signal},
    "rst_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_003_capitulation_signal},
    "rst_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_004_capitulation_signal},
    "rst_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_005_capitulation_signal},
    "rst_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_006_capitulation_signal},
    "rst_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_007_capitulation_signal},
    "rst_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_008_capitulation_signal},
    "rst_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_009_capitulation_signal},
    "rst_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_010_capitulation_signal},
    "rst_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_011_capitulation_signal},
    "rst_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_012_capitulation_signal},
    "rst_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_013_capitulation_signal},
    "rst_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_014_capitulation_signal},
    "rst_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_015_capitulation_signal},
    "rst_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_016_capitulation_signal},
    "rst_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_017_capitulation_signal},
    "rst_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_018_capitulation_signal},
    "rst_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_019_capitulation_signal},
    "rst_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_020_capitulation_signal},
    "rst_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_021_capitulation_signal},
    "rst_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_022_capitulation_signal},
    "rst_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_023_capitulation_signal},
    "rst_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_024_capitulation_signal},
    "rst_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_025_capitulation_signal},
    "rst_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_026_capitulation_signal},
    "rst_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_027_capitulation_signal},
    "rst_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_028_capitulation_signal},
    "rst_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_029_capitulation_signal},
    "rst_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_030_capitulation_signal},
    "rst_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_031_capitulation_signal},
    "rst_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_032_capitulation_signal},
    "rst_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_033_capitulation_signal},
    "rst_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_034_capitulation_signal},
    "rst_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_035_capitulation_signal},
    "rst_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_036_capitulation_signal},
    "rst_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_037_capitulation_signal},
    "rst_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_038_capitulation_signal},
    "rst_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_039_capitulation_signal},
    "rst_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_040_capitulation_signal},
    "rst_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_041_capitulation_signal},
    "rst_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_042_capitulation_signal},
    "rst_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_043_capitulation_signal},
    "rst_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_044_capitulation_signal},
    "rst_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_045_capitulation_signal},
    "rst_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_046_capitulation_signal},
    "rst_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_047_capitulation_signal},
    "rst_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_048_capitulation_signal},
    "rst_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_049_capitulation_signal},
    "rst_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_050_capitulation_signal},
    "rst_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_051_capitulation_signal},
    "rst_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_052_capitulation_signal},
    "rst_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_053_capitulation_signal},
    "rst_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_054_capitulation_signal},
    "rst_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_055_capitulation_signal},
    "rst_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_056_capitulation_signal},
    "rst_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_057_capitulation_signal},
    "rst_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_058_capitulation_signal},
    "rst_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_059_capitulation_signal},
    "rst_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_060_capitulation_signal},
    "rst_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_061_capitulation_signal},
    "rst_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_062_capitulation_signal},
    "rst_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_063_capitulation_signal},
    "rst_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_064_capitulation_signal},
    "rst_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_065_capitulation_signal},
    "rst_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_066_capitulation_signal},
    "rst_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_067_capitulation_signal},
    "rst_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_068_capitulation_signal},
    "rst_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_069_capitulation_signal},
    "rst_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_070_capitulation_signal},
    "rst_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_071_capitulation_signal},
    "rst_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_072_capitulation_signal},
    "rst_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_073_capitulation_signal},
    "rst_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_074_capitulation_signal},
    "rst_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rst_075_capitulation_signal},
}
