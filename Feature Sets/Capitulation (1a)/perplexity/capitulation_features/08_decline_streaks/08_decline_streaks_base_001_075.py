"""Generated capitulation features for 08_decline_streaks: consecutive down days/weeks/months.
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

def dstk_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dstk_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dstk_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dstk_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dstk_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dstk_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dstk_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dstk_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dstk_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dstk_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dstk_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dstk_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dstk_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dstk_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dstk_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dstk_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dstk_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dstk_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dstk_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dstk_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dstk_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dstk_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dstk_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dstk_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dstk_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dstk_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dstk_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dstk_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dstk_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dstk_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dstk_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dstk_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dstk_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dstk_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dstk_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dstk_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dstk_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dstk_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dstk_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dstk_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dstk_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dstk_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dstk_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dstk_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dstk_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dstk_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dstk_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dstk_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dstk_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dstk_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dstk_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dstk_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dstk_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dstk_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dstk_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dstk_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dstk_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dstk_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dstk_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dstk_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dstk_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DECLINE_STREAKS_REGISTRY_001_075 = {
    "dstk_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_001_capitulation_signal},
    "dstk_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_002_capitulation_signal},
    "dstk_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_003_capitulation_signal},
    "dstk_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_004_capitulation_signal},
    "dstk_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_005_capitulation_signal},
    "dstk_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_006_capitulation_signal},
    "dstk_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_007_capitulation_signal},
    "dstk_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_008_capitulation_signal},
    "dstk_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_009_capitulation_signal},
    "dstk_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_010_capitulation_signal},
    "dstk_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_011_capitulation_signal},
    "dstk_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_012_capitulation_signal},
    "dstk_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_013_capitulation_signal},
    "dstk_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_014_capitulation_signal},
    "dstk_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_015_capitulation_signal},
    "dstk_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_016_capitulation_signal},
    "dstk_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_017_capitulation_signal},
    "dstk_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_018_capitulation_signal},
    "dstk_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_019_capitulation_signal},
    "dstk_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_020_capitulation_signal},
    "dstk_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_021_capitulation_signal},
    "dstk_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_022_capitulation_signal},
    "dstk_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_023_capitulation_signal},
    "dstk_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_024_capitulation_signal},
    "dstk_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_025_capitulation_signal},
    "dstk_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_026_capitulation_signal},
    "dstk_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_027_capitulation_signal},
    "dstk_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_028_capitulation_signal},
    "dstk_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_029_capitulation_signal},
    "dstk_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_030_capitulation_signal},
    "dstk_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_031_capitulation_signal},
    "dstk_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_032_capitulation_signal},
    "dstk_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_033_capitulation_signal},
    "dstk_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_034_capitulation_signal},
    "dstk_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_035_capitulation_signal},
    "dstk_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_036_capitulation_signal},
    "dstk_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_037_capitulation_signal},
    "dstk_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_038_capitulation_signal},
    "dstk_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_039_capitulation_signal},
    "dstk_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_040_capitulation_signal},
    "dstk_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_041_capitulation_signal},
    "dstk_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_042_capitulation_signal},
    "dstk_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_043_capitulation_signal},
    "dstk_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_044_capitulation_signal},
    "dstk_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_045_capitulation_signal},
    "dstk_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_046_capitulation_signal},
    "dstk_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_047_capitulation_signal},
    "dstk_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_048_capitulation_signal},
    "dstk_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_049_capitulation_signal},
    "dstk_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_050_capitulation_signal},
    "dstk_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_051_capitulation_signal},
    "dstk_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_052_capitulation_signal},
    "dstk_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_053_capitulation_signal},
    "dstk_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_054_capitulation_signal},
    "dstk_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_055_capitulation_signal},
    "dstk_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_056_capitulation_signal},
    "dstk_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_057_capitulation_signal},
    "dstk_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_058_capitulation_signal},
    "dstk_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_059_capitulation_signal},
    "dstk_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_060_capitulation_signal},
    "dstk_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_061_capitulation_signal},
    "dstk_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_062_capitulation_signal},
    "dstk_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_063_capitulation_signal},
    "dstk_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_064_capitulation_signal},
    "dstk_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_065_capitulation_signal},
    "dstk_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_066_capitulation_signal},
    "dstk_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_067_capitulation_signal},
    "dstk_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_068_capitulation_signal},
    "dstk_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_069_capitulation_signal},
    "dstk_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_070_capitulation_signal},
    "dstk_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_071_capitulation_signal},
    "dstk_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_072_capitulation_signal},
    "dstk_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_073_capitulation_signal},
    "dstk_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_074_capitulation_signal},
    "dstk_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dstk_075_capitulation_signal},
}
