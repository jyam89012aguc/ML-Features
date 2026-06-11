"""Generated capitulation features for 09_price_compression: price range narrowing near the low.
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

def pcmp_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def pcmp_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def pcmp_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def pcmp_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def pcmp_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def pcmp_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def pcmp_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def pcmp_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def pcmp_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def pcmp_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def pcmp_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def pcmp_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def pcmp_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def pcmp_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def pcmp_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def pcmp_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def pcmp_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def pcmp_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def pcmp_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def pcmp_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def pcmp_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def pcmp_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def pcmp_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def pcmp_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def pcmp_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def pcmp_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def pcmp_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def pcmp_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def pcmp_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def pcmp_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def pcmp_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def pcmp_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def pcmp_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def pcmp_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def pcmp_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def pcmp_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def pcmp_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def pcmp_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def pcmp_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def pcmp_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def pcmp_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def pcmp_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def pcmp_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def pcmp_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def pcmp_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def pcmp_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def pcmp_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def pcmp_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def pcmp_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def pcmp_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def pcmp_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def pcmp_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def pcmp_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def pcmp_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def pcmp_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pcmp_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def pcmp_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pcmp_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def pcmp_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def pcmp_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def pcmp_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

PRICE_COMPRESSION_REGISTRY_001_075 = {
    "pcmp_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_001_capitulation_signal},
    "pcmp_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_002_capitulation_signal},
    "pcmp_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_003_capitulation_signal},
    "pcmp_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_004_capitulation_signal},
    "pcmp_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_005_capitulation_signal},
    "pcmp_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_006_capitulation_signal},
    "pcmp_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_007_capitulation_signal},
    "pcmp_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_008_capitulation_signal},
    "pcmp_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_009_capitulation_signal},
    "pcmp_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_010_capitulation_signal},
    "pcmp_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_011_capitulation_signal},
    "pcmp_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_012_capitulation_signal},
    "pcmp_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_013_capitulation_signal},
    "pcmp_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_014_capitulation_signal},
    "pcmp_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_015_capitulation_signal},
    "pcmp_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_016_capitulation_signal},
    "pcmp_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_017_capitulation_signal},
    "pcmp_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_018_capitulation_signal},
    "pcmp_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_019_capitulation_signal},
    "pcmp_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_020_capitulation_signal},
    "pcmp_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_021_capitulation_signal},
    "pcmp_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_022_capitulation_signal},
    "pcmp_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_023_capitulation_signal},
    "pcmp_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_024_capitulation_signal},
    "pcmp_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_025_capitulation_signal},
    "pcmp_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_026_capitulation_signal},
    "pcmp_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_027_capitulation_signal},
    "pcmp_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_028_capitulation_signal},
    "pcmp_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_029_capitulation_signal},
    "pcmp_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_030_capitulation_signal},
    "pcmp_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_031_capitulation_signal},
    "pcmp_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_032_capitulation_signal},
    "pcmp_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_033_capitulation_signal},
    "pcmp_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_034_capitulation_signal},
    "pcmp_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_035_capitulation_signal},
    "pcmp_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_036_capitulation_signal},
    "pcmp_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_037_capitulation_signal},
    "pcmp_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_038_capitulation_signal},
    "pcmp_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_039_capitulation_signal},
    "pcmp_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_040_capitulation_signal},
    "pcmp_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_041_capitulation_signal},
    "pcmp_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_042_capitulation_signal},
    "pcmp_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_043_capitulation_signal},
    "pcmp_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_044_capitulation_signal},
    "pcmp_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_045_capitulation_signal},
    "pcmp_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_046_capitulation_signal},
    "pcmp_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_047_capitulation_signal},
    "pcmp_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_048_capitulation_signal},
    "pcmp_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_049_capitulation_signal},
    "pcmp_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_050_capitulation_signal},
    "pcmp_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_051_capitulation_signal},
    "pcmp_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_052_capitulation_signal},
    "pcmp_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_053_capitulation_signal},
    "pcmp_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_054_capitulation_signal},
    "pcmp_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_055_capitulation_signal},
    "pcmp_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_056_capitulation_signal},
    "pcmp_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_057_capitulation_signal},
    "pcmp_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_058_capitulation_signal},
    "pcmp_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_059_capitulation_signal},
    "pcmp_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_060_capitulation_signal},
    "pcmp_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_061_capitulation_signal},
    "pcmp_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_062_capitulation_signal},
    "pcmp_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_063_capitulation_signal},
    "pcmp_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_064_capitulation_signal},
    "pcmp_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_065_capitulation_signal},
    "pcmp_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_066_capitulation_signal},
    "pcmp_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_067_capitulation_signal},
    "pcmp_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_068_capitulation_signal},
    "pcmp_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_069_capitulation_signal},
    "pcmp_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_070_capitulation_signal},
    "pcmp_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_071_capitulation_signal},
    "pcmp_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_072_capitulation_signal},
    "pcmp_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_073_capitulation_signal},
    "pcmp_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_074_capitulation_signal},
    "pcmp_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pcmp_075_capitulation_signal},
}
