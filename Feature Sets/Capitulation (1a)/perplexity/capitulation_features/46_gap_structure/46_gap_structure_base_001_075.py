"""Generated capitulation features for 46_gap_structure: overnight gap frequency.
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

def gap_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def gap_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def gap_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def gap_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def gap_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def gap_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def gap_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def gap_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def gap_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def gap_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def gap_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def gap_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def gap_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def gap_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def gap_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def gap_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def gap_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def gap_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def gap_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def gap_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def gap_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def gap_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def gap_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def gap_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def gap_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def gap_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def gap_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def gap_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def gap_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def gap_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def gap_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def gap_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def gap_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def gap_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def gap_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def gap_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def gap_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def gap_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def gap_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def gap_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def gap_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def gap_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def gap_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def gap_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def gap_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def gap_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def gap_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def gap_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gap_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gap_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def gap_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def gap_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def gap_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def gap_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def gap_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def gap_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gap_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def gap_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gap_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def gap_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def gap_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def gap_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

GAP_STRUCTURE_REGISTRY_001_075 = {
    "gap_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_001_capitulation_signal},
    "gap_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_002_capitulation_signal},
    "gap_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_003_capitulation_signal},
    "gap_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_004_capitulation_signal},
    "gap_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_005_capitulation_signal},
    "gap_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_006_capitulation_signal},
    "gap_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_007_capitulation_signal},
    "gap_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_008_capitulation_signal},
    "gap_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_009_capitulation_signal},
    "gap_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_010_capitulation_signal},
    "gap_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_011_capitulation_signal},
    "gap_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_012_capitulation_signal},
    "gap_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_013_capitulation_signal},
    "gap_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_014_capitulation_signal},
    "gap_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_015_capitulation_signal},
    "gap_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_016_capitulation_signal},
    "gap_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_017_capitulation_signal},
    "gap_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_018_capitulation_signal},
    "gap_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_019_capitulation_signal},
    "gap_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_020_capitulation_signal},
    "gap_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_021_capitulation_signal},
    "gap_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_022_capitulation_signal},
    "gap_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_023_capitulation_signal},
    "gap_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_024_capitulation_signal},
    "gap_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_025_capitulation_signal},
    "gap_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_026_capitulation_signal},
    "gap_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_027_capitulation_signal},
    "gap_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_028_capitulation_signal},
    "gap_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_029_capitulation_signal},
    "gap_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_030_capitulation_signal},
    "gap_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_031_capitulation_signal},
    "gap_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_032_capitulation_signal},
    "gap_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_033_capitulation_signal},
    "gap_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_034_capitulation_signal},
    "gap_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_035_capitulation_signal},
    "gap_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_036_capitulation_signal},
    "gap_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_037_capitulation_signal},
    "gap_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_038_capitulation_signal},
    "gap_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_039_capitulation_signal},
    "gap_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_040_capitulation_signal},
    "gap_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_041_capitulation_signal},
    "gap_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_042_capitulation_signal},
    "gap_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_043_capitulation_signal},
    "gap_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_044_capitulation_signal},
    "gap_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_045_capitulation_signal},
    "gap_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_046_capitulation_signal},
    "gap_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_047_capitulation_signal},
    "gap_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_048_capitulation_signal},
    "gap_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_049_capitulation_signal},
    "gap_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_050_capitulation_signal},
    "gap_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_051_capitulation_signal},
    "gap_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_052_capitulation_signal},
    "gap_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_053_capitulation_signal},
    "gap_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_054_capitulation_signal},
    "gap_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_055_capitulation_signal},
    "gap_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_056_capitulation_signal},
    "gap_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_057_capitulation_signal},
    "gap_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_058_capitulation_signal},
    "gap_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_059_capitulation_signal},
    "gap_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_060_capitulation_signal},
    "gap_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_061_capitulation_signal},
    "gap_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_062_capitulation_signal},
    "gap_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_063_capitulation_signal},
    "gap_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_064_capitulation_signal},
    "gap_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_065_capitulation_signal},
    "gap_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_066_capitulation_signal},
    "gap_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_067_capitulation_signal},
    "gap_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_068_capitulation_signal},
    "gap_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_069_capitulation_signal},
    "gap_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_070_capitulation_signal},
    "gap_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_071_capitulation_signal},
    "gap_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_072_capitulation_signal},
    "gap_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_073_capitulation_signal},
    "gap_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_074_capitulation_signal},
    "gap_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gap_075_capitulation_signal},
}
