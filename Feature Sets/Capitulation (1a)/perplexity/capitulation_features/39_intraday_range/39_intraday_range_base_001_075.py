"""Generated capitulation features for 39_intraday_range: high-low spread behavior.
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

def idr_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def idr_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def idr_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def idr_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def idr_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def idr_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def idr_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def idr_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def idr_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def idr_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def idr_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def idr_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def idr_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def idr_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def idr_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def idr_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def idr_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def idr_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def idr_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def idr_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def idr_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def idr_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def idr_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def idr_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def idr_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def idr_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def idr_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def idr_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def idr_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def idr_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def idr_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def idr_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def idr_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def idr_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def idr_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def idr_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def idr_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def idr_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def idr_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def idr_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def idr_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def idr_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def idr_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def idr_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def idr_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def idr_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def idr_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def idr_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def idr_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def idr_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def idr_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def idr_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def idr_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def idr_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def idr_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def idr_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def idr_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def idr_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def idr_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def idr_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def idr_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def idr_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

INTRADAY_RANGE_REGISTRY_001_075 = {
    "idr_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_001_capitulation_signal},
    "idr_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_002_capitulation_signal},
    "idr_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_003_capitulation_signal},
    "idr_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_004_capitulation_signal},
    "idr_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_005_capitulation_signal},
    "idr_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_006_capitulation_signal},
    "idr_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_007_capitulation_signal},
    "idr_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_008_capitulation_signal},
    "idr_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_009_capitulation_signal},
    "idr_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_010_capitulation_signal},
    "idr_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_011_capitulation_signal},
    "idr_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_012_capitulation_signal},
    "idr_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_013_capitulation_signal},
    "idr_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_014_capitulation_signal},
    "idr_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_015_capitulation_signal},
    "idr_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_016_capitulation_signal},
    "idr_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_017_capitulation_signal},
    "idr_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_018_capitulation_signal},
    "idr_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_019_capitulation_signal},
    "idr_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_020_capitulation_signal},
    "idr_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_021_capitulation_signal},
    "idr_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_022_capitulation_signal},
    "idr_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_023_capitulation_signal},
    "idr_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_024_capitulation_signal},
    "idr_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_025_capitulation_signal},
    "idr_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_026_capitulation_signal},
    "idr_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_027_capitulation_signal},
    "idr_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_028_capitulation_signal},
    "idr_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_029_capitulation_signal},
    "idr_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_030_capitulation_signal},
    "idr_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_031_capitulation_signal},
    "idr_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_032_capitulation_signal},
    "idr_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_033_capitulation_signal},
    "idr_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_034_capitulation_signal},
    "idr_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_035_capitulation_signal},
    "idr_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_036_capitulation_signal},
    "idr_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_037_capitulation_signal},
    "idr_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_038_capitulation_signal},
    "idr_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_039_capitulation_signal},
    "idr_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_040_capitulation_signal},
    "idr_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_041_capitulation_signal},
    "idr_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_042_capitulation_signal},
    "idr_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_043_capitulation_signal},
    "idr_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_044_capitulation_signal},
    "idr_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_045_capitulation_signal},
    "idr_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_046_capitulation_signal},
    "idr_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_047_capitulation_signal},
    "idr_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_048_capitulation_signal},
    "idr_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_049_capitulation_signal},
    "idr_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_050_capitulation_signal},
    "idr_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_051_capitulation_signal},
    "idr_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_052_capitulation_signal},
    "idr_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_053_capitulation_signal},
    "idr_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_054_capitulation_signal},
    "idr_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_055_capitulation_signal},
    "idr_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_056_capitulation_signal},
    "idr_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_057_capitulation_signal},
    "idr_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_058_capitulation_signal},
    "idr_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_059_capitulation_signal},
    "idr_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_060_capitulation_signal},
    "idr_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_061_capitulation_signal},
    "idr_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_062_capitulation_signal},
    "idr_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_063_capitulation_signal},
    "idr_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_064_capitulation_signal},
    "idr_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_065_capitulation_signal},
    "idr_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_066_capitulation_signal},
    "idr_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_067_capitulation_signal},
    "idr_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_068_capitulation_signal},
    "idr_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_069_capitulation_signal},
    "idr_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_070_capitulation_signal},
    "idr_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_071_capitulation_signal},
    "idr_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_072_capitulation_signal},
    "idr_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_073_capitulation_signal},
    "idr_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_074_capitulation_signal},
    "idr_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": idr_075_capitulation_signal},
}
