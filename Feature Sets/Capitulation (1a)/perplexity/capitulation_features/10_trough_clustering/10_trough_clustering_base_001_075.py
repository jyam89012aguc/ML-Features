"""Generated capitulation features for 10_trough_clustering: density of local minima, repeated bottoms.
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

def tcl_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def tcl_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def tcl_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def tcl_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def tcl_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tcl_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def tcl_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def tcl_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def tcl_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def tcl_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def tcl_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def tcl_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def tcl_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def tcl_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def tcl_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def tcl_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def tcl_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def tcl_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def tcl_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tcl_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def tcl_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def tcl_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def tcl_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def tcl_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def tcl_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def tcl_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def tcl_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def tcl_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def tcl_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def tcl_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def tcl_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def tcl_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def tcl_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tcl_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def tcl_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def tcl_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def tcl_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def tcl_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def tcl_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def tcl_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def tcl_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def tcl_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def tcl_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def tcl_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def tcl_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def tcl_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def tcl_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tcl_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def tcl_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def tcl_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def tcl_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def tcl_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def tcl_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def tcl_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def tcl_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tcl_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def tcl_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tcl_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def tcl_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def tcl_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def tcl_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

TROUGH_CLUSTERING_REGISTRY_001_075 = {
    "tcl_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_001_capitulation_signal},
    "tcl_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_002_capitulation_signal},
    "tcl_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_003_capitulation_signal},
    "tcl_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_004_capitulation_signal},
    "tcl_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_005_capitulation_signal},
    "tcl_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_006_capitulation_signal},
    "tcl_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_007_capitulation_signal},
    "tcl_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_008_capitulation_signal},
    "tcl_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_009_capitulation_signal},
    "tcl_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_010_capitulation_signal},
    "tcl_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_011_capitulation_signal},
    "tcl_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_012_capitulation_signal},
    "tcl_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_013_capitulation_signal},
    "tcl_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_014_capitulation_signal},
    "tcl_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_015_capitulation_signal},
    "tcl_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_016_capitulation_signal},
    "tcl_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_017_capitulation_signal},
    "tcl_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_018_capitulation_signal},
    "tcl_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_019_capitulation_signal},
    "tcl_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_020_capitulation_signal},
    "tcl_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_021_capitulation_signal},
    "tcl_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_022_capitulation_signal},
    "tcl_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_023_capitulation_signal},
    "tcl_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_024_capitulation_signal},
    "tcl_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_025_capitulation_signal},
    "tcl_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_026_capitulation_signal},
    "tcl_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_027_capitulation_signal},
    "tcl_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_028_capitulation_signal},
    "tcl_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_029_capitulation_signal},
    "tcl_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_030_capitulation_signal},
    "tcl_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_031_capitulation_signal},
    "tcl_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_032_capitulation_signal},
    "tcl_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_033_capitulation_signal},
    "tcl_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_034_capitulation_signal},
    "tcl_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_035_capitulation_signal},
    "tcl_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_036_capitulation_signal},
    "tcl_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_037_capitulation_signal},
    "tcl_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_038_capitulation_signal},
    "tcl_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_039_capitulation_signal},
    "tcl_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_040_capitulation_signal},
    "tcl_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_041_capitulation_signal},
    "tcl_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_042_capitulation_signal},
    "tcl_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_043_capitulation_signal},
    "tcl_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_044_capitulation_signal},
    "tcl_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_045_capitulation_signal},
    "tcl_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_046_capitulation_signal},
    "tcl_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_047_capitulation_signal},
    "tcl_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_048_capitulation_signal},
    "tcl_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_049_capitulation_signal},
    "tcl_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_050_capitulation_signal},
    "tcl_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_051_capitulation_signal},
    "tcl_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_052_capitulation_signal},
    "tcl_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_053_capitulation_signal},
    "tcl_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_054_capitulation_signal},
    "tcl_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_055_capitulation_signal},
    "tcl_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_056_capitulation_signal},
    "tcl_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_057_capitulation_signal},
    "tcl_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_058_capitulation_signal},
    "tcl_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_059_capitulation_signal},
    "tcl_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_060_capitulation_signal},
    "tcl_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_061_capitulation_signal},
    "tcl_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_062_capitulation_signal},
    "tcl_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_063_capitulation_signal},
    "tcl_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_064_capitulation_signal},
    "tcl_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_065_capitulation_signal},
    "tcl_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_066_capitulation_signal},
    "tcl_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_067_capitulation_signal},
    "tcl_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_068_capitulation_signal},
    "tcl_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_069_capitulation_signal},
    "tcl_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_070_capitulation_signal},
    "tcl_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_071_capitulation_signal},
    "tcl_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_072_capitulation_signal},
    "tcl_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_073_capitulation_signal},
    "tcl_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_074_capitulation_signal},
    "tcl_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tcl_075_capitulation_signal},
}
