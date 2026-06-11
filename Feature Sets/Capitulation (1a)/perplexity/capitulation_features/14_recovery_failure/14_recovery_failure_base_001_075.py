"""Generated capitulation features for 14_recovery_failure: failed bounces, lower-highs.
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

def rfl_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def rfl_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def rfl_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def rfl_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def rfl_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rfl_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def rfl_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def rfl_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def rfl_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def rfl_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def rfl_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def rfl_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def rfl_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def rfl_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def rfl_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def rfl_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def rfl_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def rfl_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def rfl_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rfl_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def rfl_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def rfl_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def rfl_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def rfl_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def rfl_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def rfl_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def rfl_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def rfl_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def rfl_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def rfl_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def rfl_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def rfl_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def rfl_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rfl_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def rfl_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def rfl_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def rfl_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def rfl_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def rfl_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def rfl_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def rfl_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def rfl_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def rfl_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def rfl_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def rfl_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def rfl_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def rfl_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rfl_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rfl_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def rfl_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def rfl_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def rfl_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def rfl_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def rfl_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def rfl_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rfl_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def rfl_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rfl_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def rfl_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def rfl_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def rfl_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

RECOVERY_FAILURE_REGISTRY_001_075 = {
    "rfl_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_001_capitulation_signal},
    "rfl_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_002_capitulation_signal},
    "rfl_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_003_capitulation_signal},
    "rfl_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_004_capitulation_signal},
    "rfl_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_005_capitulation_signal},
    "rfl_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_006_capitulation_signal},
    "rfl_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_007_capitulation_signal},
    "rfl_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_008_capitulation_signal},
    "rfl_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_009_capitulation_signal},
    "rfl_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_010_capitulation_signal},
    "rfl_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_011_capitulation_signal},
    "rfl_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_012_capitulation_signal},
    "rfl_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_013_capitulation_signal},
    "rfl_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_014_capitulation_signal},
    "rfl_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_015_capitulation_signal},
    "rfl_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_016_capitulation_signal},
    "rfl_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_017_capitulation_signal},
    "rfl_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_018_capitulation_signal},
    "rfl_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_019_capitulation_signal},
    "rfl_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_020_capitulation_signal},
    "rfl_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_021_capitulation_signal},
    "rfl_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_022_capitulation_signal},
    "rfl_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_023_capitulation_signal},
    "rfl_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_024_capitulation_signal},
    "rfl_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_025_capitulation_signal},
    "rfl_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_026_capitulation_signal},
    "rfl_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_027_capitulation_signal},
    "rfl_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_028_capitulation_signal},
    "rfl_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_029_capitulation_signal},
    "rfl_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_030_capitulation_signal},
    "rfl_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_031_capitulation_signal},
    "rfl_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_032_capitulation_signal},
    "rfl_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_033_capitulation_signal},
    "rfl_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_034_capitulation_signal},
    "rfl_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_035_capitulation_signal},
    "rfl_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_036_capitulation_signal},
    "rfl_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_037_capitulation_signal},
    "rfl_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_038_capitulation_signal},
    "rfl_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_039_capitulation_signal},
    "rfl_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_040_capitulation_signal},
    "rfl_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_041_capitulation_signal},
    "rfl_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_042_capitulation_signal},
    "rfl_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_043_capitulation_signal},
    "rfl_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_044_capitulation_signal},
    "rfl_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_045_capitulation_signal},
    "rfl_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_046_capitulation_signal},
    "rfl_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_047_capitulation_signal},
    "rfl_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_048_capitulation_signal},
    "rfl_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_049_capitulation_signal},
    "rfl_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_050_capitulation_signal},
    "rfl_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_051_capitulation_signal},
    "rfl_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_052_capitulation_signal},
    "rfl_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_053_capitulation_signal},
    "rfl_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_054_capitulation_signal},
    "rfl_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_055_capitulation_signal},
    "rfl_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_056_capitulation_signal},
    "rfl_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_057_capitulation_signal},
    "rfl_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_058_capitulation_signal},
    "rfl_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_059_capitulation_signal},
    "rfl_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_060_capitulation_signal},
    "rfl_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_061_capitulation_signal},
    "rfl_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_062_capitulation_signal},
    "rfl_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_063_capitulation_signal},
    "rfl_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_064_capitulation_signal},
    "rfl_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_065_capitulation_signal},
    "rfl_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_066_capitulation_signal},
    "rfl_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_067_capitulation_signal},
    "rfl_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_068_capitulation_signal},
    "rfl_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_069_capitulation_signal},
    "rfl_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_070_capitulation_signal},
    "rfl_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_071_capitulation_signal},
    "rfl_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_072_capitulation_signal},
    "rfl_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_073_capitulation_signal},
    "rfl_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_074_capitulation_signal},
    "rfl_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rfl_075_capitulation_signal},
}
