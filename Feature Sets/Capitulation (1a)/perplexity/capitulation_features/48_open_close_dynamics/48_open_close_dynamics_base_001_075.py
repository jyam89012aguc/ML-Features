"""Generated capitulation features for 48_open_close_dynamics: open-close behavior.
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

def ocd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def ocd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def ocd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def ocd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def ocd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ocd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def ocd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def ocd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def ocd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def ocd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def ocd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def ocd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def ocd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def ocd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def ocd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def ocd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def ocd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def ocd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def ocd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ocd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def ocd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def ocd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def ocd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def ocd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def ocd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def ocd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def ocd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def ocd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def ocd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def ocd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def ocd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def ocd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def ocd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ocd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def ocd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def ocd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def ocd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def ocd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def ocd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def ocd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def ocd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def ocd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def ocd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def ocd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def ocd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def ocd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def ocd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ocd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ocd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def ocd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def ocd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def ocd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def ocd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def ocd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def ocd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ocd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def ocd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ocd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def ocd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def ocd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def ocd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

OPEN_CLOSE_DYNAMICS_REGISTRY_001_075 = {
    "ocd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_001_capitulation_signal},
    "ocd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_002_capitulation_signal},
    "ocd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_003_capitulation_signal},
    "ocd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_004_capitulation_signal},
    "ocd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_005_capitulation_signal},
    "ocd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_006_capitulation_signal},
    "ocd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_007_capitulation_signal},
    "ocd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_008_capitulation_signal},
    "ocd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_009_capitulation_signal},
    "ocd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_010_capitulation_signal},
    "ocd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_011_capitulation_signal},
    "ocd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_012_capitulation_signal},
    "ocd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_013_capitulation_signal},
    "ocd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_014_capitulation_signal},
    "ocd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_015_capitulation_signal},
    "ocd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_016_capitulation_signal},
    "ocd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_017_capitulation_signal},
    "ocd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_018_capitulation_signal},
    "ocd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_019_capitulation_signal},
    "ocd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_020_capitulation_signal},
    "ocd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_021_capitulation_signal},
    "ocd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_022_capitulation_signal},
    "ocd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_023_capitulation_signal},
    "ocd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_024_capitulation_signal},
    "ocd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_025_capitulation_signal},
    "ocd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_026_capitulation_signal},
    "ocd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_027_capitulation_signal},
    "ocd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_028_capitulation_signal},
    "ocd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_029_capitulation_signal},
    "ocd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_030_capitulation_signal},
    "ocd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_031_capitulation_signal},
    "ocd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_032_capitulation_signal},
    "ocd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_033_capitulation_signal},
    "ocd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_034_capitulation_signal},
    "ocd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_035_capitulation_signal},
    "ocd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_036_capitulation_signal},
    "ocd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_037_capitulation_signal},
    "ocd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_038_capitulation_signal},
    "ocd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_039_capitulation_signal},
    "ocd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_040_capitulation_signal},
    "ocd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_041_capitulation_signal},
    "ocd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_042_capitulation_signal},
    "ocd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_043_capitulation_signal},
    "ocd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_044_capitulation_signal},
    "ocd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_045_capitulation_signal},
    "ocd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_046_capitulation_signal},
    "ocd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_047_capitulation_signal},
    "ocd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_048_capitulation_signal},
    "ocd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_049_capitulation_signal},
    "ocd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_050_capitulation_signal},
    "ocd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_051_capitulation_signal},
    "ocd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_052_capitulation_signal},
    "ocd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_053_capitulation_signal},
    "ocd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_054_capitulation_signal},
    "ocd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_055_capitulation_signal},
    "ocd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_056_capitulation_signal},
    "ocd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_057_capitulation_signal},
    "ocd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_058_capitulation_signal},
    "ocd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_059_capitulation_signal},
    "ocd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_060_capitulation_signal},
    "ocd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_061_capitulation_signal},
    "ocd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_062_capitulation_signal},
    "ocd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_063_capitulation_signal},
    "ocd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_064_capitulation_signal},
    "ocd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_065_capitulation_signal},
    "ocd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_066_capitulation_signal},
    "ocd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_067_capitulation_signal},
    "ocd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_068_capitulation_signal},
    "ocd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_069_capitulation_signal},
    "ocd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_070_capitulation_signal},
    "ocd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_071_capitulation_signal},
    "ocd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_072_capitulation_signal},
    "ocd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_073_capitulation_signal},
    "ocd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_074_capitulation_signal},
    "ocd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ocd_075_capitulation_signal},
}
