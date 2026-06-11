"""Generated capitulation features for 06_low_proximity: closeness to trailing min, new-low frequency.
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

def lp_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def lp_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def lp_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def lp_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def lp_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def lp_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def lp_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def lp_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def lp_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def lp_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def lp_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def lp_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def lp_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def lp_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def lp_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def lp_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def lp_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def lp_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def lp_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def lp_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def lp_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def lp_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def lp_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def lp_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def lp_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def lp_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def lp_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def lp_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def lp_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def lp_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def lp_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def lp_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def lp_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def lp_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def lp_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def lp_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def lp_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def lp_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def lp_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def lp_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def lp_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def lp_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def lp_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def lp_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def lp_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def lp_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def lp_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def lp_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lp_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lp_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def lp_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def lp_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def lp_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def lp_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def lp_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def lp_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lp_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def lp_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lp_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def lp_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def lp_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def lp_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

LOW_PROXIMITY_REGISTRY_001_075 = {
    "lp_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_001_capitulation_signal},
    "lp_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_002_capitulation_signal},
    "lp_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_003_capitulation_signal},
    "lp_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_004_capitulation_signal},
    "lp_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_005_capitulation_signal},
    "lp_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_006_capitulation_signal},
    "lp_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_007_capitulation_signal},
    "lp_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_008_capitulation_signal},
    "lp_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_009_capitulation_signal},
    "lp_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_010_capitulation_signal},
    "lp_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_011_capitulation_signal},
    "lp_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_012_capitulation_signal},
    "lp_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_013_capitulation_signal},
    "lp_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_014_capitulation_signal},
    "lp_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_015_capitulation_signal},
    "lp_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_016_capitulation_signal},
    "lp_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_017_capitulation_signal},
    "lp_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_018_capitulation_signal},
    "lp_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_019_capitulation_signal},
    "lp_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_020_capitulation_signal},
    "lp_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_021_capitulation_signal},
    "lp_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_022_capitulation_signal},
    "lp_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_023_capitulation_signal},
    "lp_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_024_capitulation_signal},
    "lp_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_025_capitulation_signal},
    "lp_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_026_capitulation_signal},
    "lp_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_027_capitulation_signal},
    "lp_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_028_capitulation_signal},
    "lp_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_029_capitulation_signal},
    "lp_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_030_capitulation_signal},
    "lp_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_031_capitulation_signal},
    "lp_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_032_capitulation_signal},
    "lp_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_033_capitulation_signal},
    "lp_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_034_capitulation_signal},
    "lp_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_035_capitulation_signal},
    "lp_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_036_capitulation_signal},
    "lp_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_037_capitulation_signal},
    "lp_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_038_capitulation_signal},
    "lp_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_039_capitulation_signal},
    "lp_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_040_capitulation_signal},
    "lp_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_041_capitulation_signal},
    "lp_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_042_capitulation_signal},
    "lp_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_043_capitulation_signal},
    "lp_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_044_capitulation_signal},
    "lp_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_045_capitulation_signal},
    "lp_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_046_capitulation_signal},
    "lp_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_047_capitulation_signal},
    "lp_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_048_capitulation_signal},
    "lp_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_049_capitulation_signal},
    "lp_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_050_capitulation_signal},
    "lp_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_051_capitulation_signal},
    "lp_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_052_capitulation_signal},
    "lp_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_053_capitulation_signal},
    "lp_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_054_capitulation_signal},
    "lp_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_055_capitulation_signal},
    "lp_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_056_capitulation_signal},
    "lp_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_057_capitulation_signal},
    "lp_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_058_capitulation_signal},
    "lp_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_059_capitulation_signal},
    "lp_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_060_capitulation_signal},
    "lp_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_061_capitulation_signal},
    "lp_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_062_capitulation_signal},
    "lp_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_063_capitulation_signal},
    "lp_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_064_capitulation_signal},
    "lp_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_065_capitulation_signal},
    "lp_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_066_capitulation_signal},
    "lp_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_067_capitulation_signal},
    "lp_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_068_capitulation_signal},
    "lp_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_069_capitulation_signal},
    "lp_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_070_capitulation_signal},
    "lp_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_071_capitulation_signal},
    "lp_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_072_capitulation_signal},
    "lp_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_073_capitulation_signal},
    "lp_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_074_capitulation_signal},
    "lp_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_075_capitulation_signal},
}
