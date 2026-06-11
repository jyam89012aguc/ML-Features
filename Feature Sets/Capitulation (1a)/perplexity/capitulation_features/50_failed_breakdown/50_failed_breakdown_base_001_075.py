"""Generated capitulation features for 50_failed_breakdown: undercut-and-reclaim.
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

def fbd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def fbd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def fbd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def fbd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def fbd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def fbd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def fbd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def fbd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def fbd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def fbd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def fbd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def fbd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def fbd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def fbd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def fbd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def fbd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def fbd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def fbd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def fbd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def fbd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def fbd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def fbd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def fbd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def fbd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def fbd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def fbd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def fbd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def fbd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def fbd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def fbd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def fbd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def fbd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def fbd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def fbd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def fbd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def fbd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def fbd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def fbd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def fbd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def fbd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def fbd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def fbd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def fbd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def fbd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def fbd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def fbd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def fbd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def fbd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def fbd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def fbd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def fbd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def fbd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def fbd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def fbd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def fbd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def fbd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def fbd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def fbd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def fbd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def fbd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def fbd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

FAILED_BREAKDOWN_REGISTRY_001_075 = {
    "fbd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_001_capitulation_signal},
    "fbd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_002_capitulation_signal},
    "fbd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_003_capitulation_signal},
    "fbd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_004_capitulation_signal},
    "fbd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_005_capitulation_signal},
    "fbd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_006_capitulation_signal},
    "fbd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_007_capitulation_signal},
    "fbd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_008_capitulation_signal},
    "fbd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_009_capitulation_signal},
    "fbd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_010_capitulation_signal},
    "fbd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_011_capitulation_signal},
    "fbd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_012_capitulation_signal},
    "fbd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_013_capitulation_signal},
    "fbd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_014_capitulation_signal},
    "fbd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_015_capitulation_signal},
    "fbd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_016_capitulation_signal},
    "fbd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_017_capitulation_signal},
    "fbd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_018_capitulation_signal},
    "fbd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_019_capitulation_signal},
    "fbd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_020_capitulation_signal},
    "fbd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_021_capitulation_signal},
    "fbd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_022_capitulation_signal},
    "fbd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_023_capitulation_signal},
    "fbd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_024_capitulation_signal},
    "fbd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_025_capitulation_signal},
    "fbd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_026_capitulation_signal},
    "fbd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_027_capitulation_signal},
    "fbd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_028_capitulation_signal},
    "fbd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_029_capitulation_signal},
    "fbd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_030_capitulation_signal},
    "fbd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_031_capitulation_signal},
    "fbd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_032_capitulation_signal},
    "fbd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_033_capitulation_signal},
    "fbd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_034_capitulation_signal},
    "fbd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_035_capitulation_signal},
    "fbd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_036_capitulation_signal},
    "fbd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_037_capitulation_signal},
    "fbd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_038_capitulation_signal},
    "fbd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_039_capitulation_signal},
    "fbd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_040_capitulation_signal},
    "fbd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_041_capitulation_signal},
    "fbd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_042_capitulation_signal},
    "fbd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_043_capitulation_signal},
    "fbd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_044_capitulation_signal},
    "fbd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_045_capitulation_signal},
    "fbd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_046_capitulation_signal},
    "fbd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_047_capitulation_signal},
    "fbd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_048_capitulation_signal},
    "fbd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_049_capitulation_signal},
    "fbd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_050_capitulation_signal},
    "fbd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_051_capitulation_signal},
    "fbd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_052_capitulation_signal},
    "fbd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_053_capitulation_signal},
    "fbd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_054_capitulation_signal},
    "fbd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_055_capitulation_signal},
    "fbd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_056_capitulation_signal},
    "fbd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_057_capitulation_signal},
    "fbd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_058_capitulation_signal},
    "fbd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_059_capitulation_signal},
    "fbd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_060_capitulation_signal},
    "fbd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_061_capitulation_signal},
    "fbd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_062_capitulation_signal},
    "fbd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_063_capitulation_signal},
    "fbd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_064_capitulation_signal},
    "fbd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_065_capitulation_signal},
    "fbd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_066_capitulation_signal},
    "fbd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_067_capitulation_signal},
    "fbd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_068_capitulation_signal},
    "fbd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_069_capitulation_signal},
    "fbd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_070_capitulation_signal},
    "fbd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_071_capitulation_signal},
    "fbd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_072_capitulation_signal},
    "fbd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_073_capitulation_signal},
    "fbd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_074_capitulation_signal},
    "fbd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": fbd_075_capitulation_signal},
}
