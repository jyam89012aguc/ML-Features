"""Generated capitulation features for 11_decline_path_entropy: smooth-vs-jagged structure.
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

def dpe_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dpe_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dpe_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dpe_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dpe_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dpe_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dpe_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dpe_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dpe_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dpe_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dpe_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dpe_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dpe_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dpe_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dpe_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dpe_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dpe_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dpe_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dpe_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dpe_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dpe_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dpe_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dpe_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dpe_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dpe_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dpe_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dpe_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dpe_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dpe_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dpe_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dpe_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dpe_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dpe_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dpe_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dpe_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dpe_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dpe_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dpe_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dpe_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dpe_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dpe_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dpe_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dpe_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dpe_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dpe_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dpe_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dpe_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dpe_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dpe_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dpe_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dpe_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dpe_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dpe_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dpe_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dpe_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dpe_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dpe_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dpe_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dpe_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dpe_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dpe_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DECLINE_PATH_ENTROPY_REGISTRY_001_075 = {
    "dpe_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_001_capitulation_signal},
    "dpe_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_002_capitulation_signal},
    "dpe_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_003_capitulation_signal},
    "dpe_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_004_capitulation_signal},
    "dpe_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_005_capitulation_signal},
    "dpe_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_006_capitulation_signal},
    "dpe_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_007_capitulation_signal},
    "dpe_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_008_capitulation_signal},
    "dpe_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_009_capitulation_signal},
    "dpe_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_010_capitulation_signal},
    "dpe_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_011_capitulation_signal},
    "dpe_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_012_capitulation_signal},
    "dpe_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_013_capitulation_signal},
    "dpe_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_014_capitulation_signal},
    "dpe_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_015_capitulation_signal},
    "dpe_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_016_capitulation_signal},
    "dpe_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_017_capitulation_signal},
    "dpe_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_018_capitulation_signal},
    "dpe_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_019_capitulation_signal},
    "dpe_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_020_capitulation_signal},
    "dpe_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_021_capitulation_signal},
    "dpe_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_022_capitulation_signal},
    "dpe_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_023_capitulation_signal},
    "dpe_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_024_capitulation_signal},
    "dpe_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_025_capitulation_signal},
    "dpe_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_026_capitulation_signal},
    "dpe_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_027_capitulation_signal},
    "dpe_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_028_capitulation_signal},
    "dpe_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_029_capitulation_signal},
    "dpe_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_030_capitulation_signal},
    "dpe_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_031_capitulation_signal},
    "dpe_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_032_capitulation_signal},
    "dpe_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_033_capitulation_signal},
    "dpe_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_034_capitulation_signal},
    "dpe_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_035_capitulation_signal},
    "dpe_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_036_capitulation_signal},
    "dpe_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_037_capitulation_signal},
    "dpe_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_038_capitulation_signal},
    "dpe_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_039_capitulation_signal},
    "dpe_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_040_capitulation_signal},
    "dpe_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_041_capitulation_signal},
    "dpe_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_042_capitulation_signal},
    "dpe_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_043_capitulation_signal},
    "dpe_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_044_capitulation_signal},
    "dpe_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_045_capitulation_signal},
    "dpe_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_046_capitulation_signal},
    "dpe_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_047_capitulation_signal},
    "dpe_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_048_capitulation_signal},
    "dpe_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_049_capitulation_signal},
    "dpe_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_050_capitulation_signal},
    "dpe_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_051_capitulation_signal},
    "dpe_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_052_capitulation_signal},
    "dpe_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_053_capitulation_signal},
    "dpe_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_054_capitulation_signal},
    "dpe_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_055_capitulation_signal},
    "dpe_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_056_capitulation_signal},
    "dpe_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_057_capitulation_signal},
    "dpe_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_058_capitulation_signal},
    "dpe_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_059_capitulation_signal},
    "dpe_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_060_capitulation_signal},
    "dpe_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_061_capitulation_signal},
    "dpe_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_062_capitulation_signal},
    "dpe_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_063_capitulation_signal},
    "dpe_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_064_capitulation_signal},
    "dpe_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_065_capitulation_signal},
    "dpe_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_066_capitulation_signal},
    "dpe_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_067_capitulation_signal},
    "dpe_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_068_capitulation_signal},
    "dpe_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_069_capitulation_signal},
    "dpe_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_070_capitulation_signal},
    "dpe_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_071_capitulation_signal},
    "dpe_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_072_capitulation_signal},
    "dpe_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_073_capitulation_signal},
    "dpe_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_074_capitulation_signal},
    "dpe_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dpe_075_capitulation_signal},
}
