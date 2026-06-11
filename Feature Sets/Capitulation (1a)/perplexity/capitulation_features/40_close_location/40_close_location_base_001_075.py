"""Generated capitulation features for 40_close_location: close within daily range.
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

def clv_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def clv_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def clv_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def clv_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def clv_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def clv_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def clv_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def clv_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def clv_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def clv_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def clv_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def clv_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def clv_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def clv_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def clv_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def clv_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def clv_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def clv_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def clv_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def clv_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def clv_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def clv_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def clv_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def clv_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def clv_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def clv_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def clv_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def clv_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def clv_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def clv_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def clv_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def clv_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def clv_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def clv_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def clv_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def clv_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def clv_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def clv_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def clv_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def clv_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def clv_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def clv_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def clv_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def clv_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def clv_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def clv_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def clv_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def clv_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def clv_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def clv_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def clv_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def clv_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def clv_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def clv_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def clv_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def clv_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def clv_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def clv_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def clv_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def clv_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def clv_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def clv_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

CLOSE_LOCATION_REGISTRY_001_075 = {
    "clv_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_001_capitulation_signal},
    "clv_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_002_capitulation_signal},
    "clv_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_003_capitulation_signal},
    "clv_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_004_capitulation_signal},
    "clv_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_005_capitulation_signal},
    "clv_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_006_capitulation_signal},
    "clv_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_007_capitulation_signal},
    "clv_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_008_capitulation_signal},
    "clv_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_009_capitulation_signal},
    "clv_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_010_capitulation_signal},
    "clv_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_011_capitulation_signal},
    "clv_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_012_capitulation_signal},
    "clv_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_013_capitulation_signal},
    "clv_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_014_capitulation_signal},
    "clv_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_015_capitulation_signal},
    "clv_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_016_capitulation_signal},
    "clv_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_017_capitulation_signal},
    "clv_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_018_capitulation_signal},
    "clv_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_019_capitulation_signal},
    "clv_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_020_capitulation_signal},
    "clv_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_021_capitulation_signal},
    "clv_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_022_capitulation_signal},
    "clv_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_023_capitulation_signal},
    "clv_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_024_capitulation_signal},
    "clv_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_025_capitulation_signal},
    "clv_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_026_capitulation_signal},
    "clv_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_027_capitulation_signal},
    "clv_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_028_capitulation_signal},
    "clv_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_029_capitulation_signal},
    "clv_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_030_capitulation_signal},
    "clv_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_031_capitulation_signal},
    "clv_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_032_capitulation_signal},
    "clv_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_033_capitulation_signal},
    "clv_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_034_capitulation_signal},
    "clv_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_035_capitulation_signal},
    "clv_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_036_capitulation_signal},
    "clv_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_037_capitulation_signal},
    "clv_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_038_capitulation_signal},
    "clv_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_039_capitulation_signal},
    "clv_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_040_capitulation_signal},
    "clv_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_041_capitulation_signal},
    "clv_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_042_capitulation_signal},
    "clv_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_043_capitulation_signal},
    "clv_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_044_capitulation_signal},
    "clv_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_045_capitulation_signal},
    "clv_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_046_capitulation_signal},
    "clv_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_047_capitulation_signal},
    "clv_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_048_capitulation_signal},
    "clv_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_049_capitulation_signal},
    "clv_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_050_capitulation_signal},
    "clv_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_051_capitulation_signal},
    "clv_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_052_capitulation_signal},
    "clv_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_053_capitulation_signal},
    "clv_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_054_capitulation_signal},
    "clv_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_055_capitulation_signal},
    "clv_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_056_capitulation_signal},
    "clv_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_057_capitulation_signal},
    "clv_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_058_capitulation_signal},
    "clv_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_059_capitulation_signal},
    "clv_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_060_capitulation_signal},
    "clv_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_061_capitulation_signal},
    "clv_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_062_capitulation_signal},
    "clv_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_063_capitulation_signal},
    "clv_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_064_capitulation_signal},
    "clv_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_065_capitulation_signal},
    "clv_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_066_capitulation_signal},
    "clv_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_067_capitulation_signal},
    "clv_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_068_capitulation_signal},
    "clv_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_069_capitulation_signal},
    "clv_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_070_capitulation_signal},
    "clv_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_071_capitulation_signal},
    "clv_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_072_capitulation_signal},
    "clv_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_073_capitulation_signal},
    "clv_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_074_capitulation_signal},
    "clv_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": clv_075_capitulation_signal},
}
