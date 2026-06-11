"""Generated capitulation features for 35_capitulation_thrust: final-leg-down thrust.
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

def cth_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def cth_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def cth_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def cth_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def cth_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def cth_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def cth_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def cth_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def cth_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def cth_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def cth_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def cth_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def cth_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def cth_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def cth_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def cth_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def cth_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def cth_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def cth_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def cth_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def cth_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def cth_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def cth_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def cth_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def cth_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def cth_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def cth_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def cth_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def cth_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def cth_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def cth_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def cth_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def cth_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def cth_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def cth_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def cth_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def cth_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def cth_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def cth_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def cth_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def cth_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def cth_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def cth_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def cth_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def cth_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def cth_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def cth_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def cth_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def cth_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def cth_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def cth_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def cth_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def cth_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def cth_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def cth_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def cth_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def cth_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def cth_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def cth_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def cth_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def cth_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def cth_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

CAPITULATION_THRUST_REGISTRY_001_075 = {
    "cth_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_001_capitulation_signal},
    "cth_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_002_capitulation_signal},
    "cth_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_003_capitulation_signal},
    "cth_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_004_capitulation_signal},
    "cth_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_005_capitulation_signal},
    "cth_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_006_capitulation_signal},
    "cth_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_007_capitulation_signal},
    "cth_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_008_capitulation_signal},
    "cth_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_009_capitulation_signal},
    "cth_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_010_capitulation_signal},
    "cth_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_011_capitulation_signal},
    "cth_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_012_capitulation_signal},
    "cth_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_013_capitulation_signal},
    "cth_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_014_capitulation_signal},
    "cth_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_015_capitulation_signal},
    "cth_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_016_capitulation_signal},
    "cth_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_017_capitulation_signal},
    "cth_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_018_capitulation_signal},
    "cth_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_019_capitulation_signal},
    "cth_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_020_capitulation_signal},
    "cth_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_021_capitulation_signal},
    "cth_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_022_capitulation_signal},
    "cth_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_023_capitulation_signal},
    "cth_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_024_capitulation_signal},
    "cth_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_025_capitulation_signal},
    "cth_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_026_capitulation_signal},
    "cth_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_027_capitulation_signal},
    "cth_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_028_capitulation_signal},
    "cth_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_029_capitulation_signal},
    "cth_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_030_capitulation_signal},
    "cth_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_031_capitulation_signal},
    "cth_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_032_capitulation_signal},
    "cth_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_033_capitulation_signal},
    "cth_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_034_capitulation_signal},
    "cth_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_035_capitulation_signal},
    "cth_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_036_capitulation_signal},
    "cth_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_037_capitulation_signal},
    "cth_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_038_capitulation_signal},
    "cth_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_039_capitulation_signal},
    "cth_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_040_capitulation_signal},
    "cth_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_041_capitulation_signal},
    "cth_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_042_capitulation_signal},
    "cth_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_043_capitulation_signal},
    "cth_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_044_capitulation_signal},
    "cth_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_045_capitulation_signal},
    "cth_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_046_capitulation_signal},
    "cth_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_047_capitulation_signal},
    "cth_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_048_capitulation_signal},
    "cth_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_049_capitulation_signal},
    "cth_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_050_capitulation_signal},
    "cth_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_051_capitulation_signal},
    "cth_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_052_capitulation_signal},
    "cth_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_053_capitulation_signal},
    "cth_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_054_capitulation_signal},
    "cth_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_055_capitulation_signal},
    "cth_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_056_capitulation_signal},
    "cth_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_057_capitulation_signal},
    "cth_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_058_capitulation_signal},
    "cth_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_059_capitulation_signal},
    "cth_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_060_capitulation_signal},
    "cth_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_061_capitulation_signal},
    "cth_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_062_capitulation_signal},
    "cth_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_063_capitulation_signal},
    "cth_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_064_capitulation_signal},
    "cth_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_065_capitulation_signal},
    "cth_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_066_capitulation_signal},
    "cth_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_067_capitulation_signal},
    "cth_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_068_capitulation_signal},
    "cth_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_069_capitulation_signal},
    "cth_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_070_capitulation_signal},
    "cth_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_071_capitulation_signal},
    "cth_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_072_capitulation_signal},
    "cth_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_073_capitulation_signal},
    "cth_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_074_capitulation_signal},
    "cth_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": cth_075_capitulation_signal},
}
