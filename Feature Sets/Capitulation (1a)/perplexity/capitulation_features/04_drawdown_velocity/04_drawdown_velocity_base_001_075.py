"""Generated capitulation features for 04_drawdown_velocity: speed of decline, slope of fall.
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

def dvel_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dvel_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dvel_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dvel_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dvel_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dvel_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dvel_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dvel_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dvel_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dvel_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dvel_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dvel_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dvel_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dvel_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dvel_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dvel_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dvel_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dvel_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dvel_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dvel_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dvel_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dvel_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dvel_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dvel_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dvel_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dvel_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dvel_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dvel_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dvel_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dvel_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dvel_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dvel_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dvel_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dvel_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dvel_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dvel_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dvel_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dvel_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dvel_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dvel_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dvel_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dvel_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dvel_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dvel_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dvel_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dvel_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dvel_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dvel_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dvel_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dvel_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dvel_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dvel_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dvel_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dvel_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dvel_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvel_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dvel_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvel_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dvel_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dvel_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dvel_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DRAWDOWN_VELOCITY_REGISTRY_001_075 = {
    "dvel_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_001_capitulation_signal},
    "dvel_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_002_capitulation_signal},
    "dvel_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_003_capitulation_signal},
    "dvel_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_004_capitulation_signal},
    "dvel_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_005_capitulation_signal},
    "dvel_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_006_capitulation_signal},
    "dvel_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_007_capitulation_signal},
    "dvel_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_008_capitulation_signal},
    "dvel_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_009_capitulation_signal},
    "dvel_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_010_capitulation_signal},
    "dvel_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_011_capitulation_signal},
    "dvel_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_012_capitulation_signal},
    "dvel_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_013_capitulation_signal},
    "dvel_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_014_capitulation_signal},
    "dvel_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_015_capitulation_signal},
    "dvel_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_016_capitulation_signal},
    "dvel_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_017_capitulation_signal},
    "dvel_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_018_capitulation_signal},
    "dvel_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_019_capitulation_signal},
    "dvel_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_020_capitulation_signal},
    "dvel_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_021_capitulation_signal},
    "dvel_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_022_capitulation_signal},
    "dvel_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_023_capitulation_signal},
    "dvel_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_024_capitulation_signal},
    "dvel_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_025_capitulation_signal},
    "dvel_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_026_capitulation_signal},
    "dvel_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_027_capitulation_signal},
    "dvel_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_028_capitulation_signal},
    "dvel_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_029_capitulation_signal},
    "dvel_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_030_capitulation_signal},
    "dvel_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_031_capitulation_signal},
    "dvel_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_032_capitulation_signal},
    "dvel_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_033_capitulation_signal},
    "dvel_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_034_capitulation_signal},
    "dvel_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_035_capitulation_signal},
    "dvel_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_036_capitulation_signal},
    "dvel_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_037_capitulation_signal},
    "dvel_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_038_capitulation_signal},
    "dvel_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_039_capitulation_signal},
    "dvel_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_040_capitulation_signal},
    "dvel_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_041_capitulation_signal},
    "dvel_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_042_capitulation_signal},
    "dvel_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_043_capitulation_signal},
    "dvel_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_044_capitulation_signal},
    "dvel_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_045_capitulation_signal},
    "dvel_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_046_capitulation_signal},
    "dvel_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_047_capitulation_signal},
    "dvel_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_048_capitulation_signal},
    "dvel_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_049_capitulation_signal},
    "dvel_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_050_capitulation_signal},
    "dvel_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_051_capitulation_signal},
    "dvel_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_052_capitulation_signal},
    "dvel_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_053_capitulation_signal},
    "dvel_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_054_capitulation_signal},
    "dvel_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_055_capitulation_signal},
    "dvel_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_056_capitulation_signal},
    "dvel_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_057_capitulation_signal},
    "dvel_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_058_capitulation_signal},
    "dvel_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_059_capitulation_signal},
    "dvel_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_060_capitulation_signal},
    "dvel_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_061_capitulation_signal},
    "dvel_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_062_capitulation_signal},
    "dvel_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_063_capitulation_signal},
    "dvel_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_064_capitulation_signal},
    "dvel_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_065_capitulation_signal},
    "dvel_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_066_capitulation_signal},
    "dvel_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_067_capitulation_signal},
    "dvel_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_068_capitulation_signal},
    "dvel_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_069_capitulation_signal},
    "dvel_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_070_capitulation_signal},
    "dvel_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_071_capitulation_signal},
    "dvel_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_072_capitulation_signal},
    "dvel_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_073_capitulation_signal},
    "dvel_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_074_capitulation_signal},
    "dvel_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvel_075_capitulation_signal},
}
