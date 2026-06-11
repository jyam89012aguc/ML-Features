"""Generated capitulation features for 56_zero_volume_days: no-trade days.
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

def zvd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def zvd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def zvd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def zvd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def zvd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def zvd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def zvd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def zvd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def zvd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def zvd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def zvd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def zvd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def zvd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def zvd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def zvd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def zvd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def zvd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def zvd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def zvd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def zvd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def zvd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def zvd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def zvd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def zvd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def zvd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def zvd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def zvd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def zvd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def zvd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def zvd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def zvd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def zvd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def zvd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def zvd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def zvd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def zvd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def zvd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def zvd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def zvd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def zvd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def zvd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def zvd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def zvd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def zvd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def zvd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def zvd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def zvd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def zvd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def zvd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def zvd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def zvd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def zvd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def zvd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def zvd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def zvd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def zvd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def zvd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def zvd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def zvd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def zvd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def zvd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

ZERO_VOLUME_DAYS_REGISTRY_001_075 = {
    "zvd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_001_capitulation_signal},
    "zvd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_002_capitulation_signal},
    "zvd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_003_capitulation_signal},
    "zvd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_004_capitulation_signal},
    "zvd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_005_capitulation_signal},
    "zvd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_006_capitulation_signal},
    "zvd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_007_capitulation_signal},
    "zvd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_008_capitulation_signal},
    "zvd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_009_capitulation_signal},
    "zvd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_010_capitulation_signal},
    "zvd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_011_capitulation_signal},
    "zvd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_012_capitulation_signal},
    "zvd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_013_capitulation_signal},
    "zvd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_014_capitulation_signal},
    "zvd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_015_capitulation_signal},
    "zvd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_016_capitulation_signal},
    "zvd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_017_capitulation_signal},
    "zvd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_018_capitulation_signal},
    "zvd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_019_capitulation_signal},
    "zvd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_020_capitulation_signal},
    "zvd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_021_capitulation_signal},
    "zvd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_022_capitulation_signal},
    "zvd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_023_capitulation_signal},
    "zvd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_024_capitulation_signal},
    "zvd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_025_capitulation_signal},
    "zvd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_026_capitulation_signal},
    "zvd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_027_capitulation_signal},
    "zvd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_028_capitulation_signal},
    "zvd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_029_capitulation_signal},
    "zvd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_030_capitulation_signal},
    "zvd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_031_capitulation_signal},
    "zvd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_032_capitulation_signal},
    "zvd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_033_capitulation_signal},
    "zvd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_034_capitulation_signal},
    "zvd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_035_capitulation_signal},
    "zvd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_036_capitulation_signal},
    "zvd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_037_capitulation_signal},
    "zvd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_038_capitulation_signal},
    "zvd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_039_capitulation_signal},
    "zvd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_040_capitulation_signal},
    "zvd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_041_capitulation_signal},
    "zvd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_042_capitulation_signal},
    "zvd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_043_capitulation_signal},
    "zvd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_044_capitulation_signal},
    "zvd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_045_capitulation_signal},
    "zvd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_046_capitulation_signal},
    "zvd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_047_capitulation_signal},
    "zvd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_048_capitulation_signal},
    "zvd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_049_capitulation_signal},
    "zvd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_050_capitulation_signal},
    "zvd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_051_capitulation_signal},
    "zvd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_052_capitulation_signal},
    "zvd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_053_capitulation_signal},
    "zvd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_054_capitulation_signal},
    "zvd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_055_capitulation_signal},
    "zvd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_056_capitulation_signal},
    "zvd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_057_capitulation_signal},
    "zvd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_058_capitulation_signal},
    "zvd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_059_capitulation_signal},
    "zvd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_060_capitulation_signal},
    "zvd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_061_capitulation_signal},
    "zvd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_062_capitulation_signal},
    "zvd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_063_capitulation_signal},
    "zvd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_064_capitulation_signal},
    "zvd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_065_capitulation_signal},
    "zvd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_066_capitulation_signal},
    "zvd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_067_capitulation_signal},
    "zvd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_068_capitulation_signal},
    "zvd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_069_capitulation_signal},
    "zvd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_070_capitulation_signal},
    "zvd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_071_capitulation_signal},
    "zvd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_072_capitulation_signal},
    "zvd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_073_capitulation_signal},
    "zvd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_074_capitulation_signal},
    "zvd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": zvd_075_capitulation_signal},
}
