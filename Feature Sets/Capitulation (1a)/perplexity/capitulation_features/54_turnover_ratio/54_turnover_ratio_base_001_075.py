"""Generated capitulation features for 54_turnover_ratio: volume/share extremes.
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

def tnv_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def tnv_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def tnv_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def tnv_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def tnv_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tnv_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def tnv_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def tnv_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def tnv_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def tnv_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def tnv_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def tnv_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def tnv_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def tnv_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def tnv_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def tnv_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def tnv_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def tnv_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def tnv_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tnv_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def tnv_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def tnv_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def tnv_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def tnv_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def tnv_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def tnv_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def tnv_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def tnv_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def tnv_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def tnv_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def tnv_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def tnv_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def tnv_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tnv_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def tnv_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def tnv_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def tnv_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def tnv_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def tnv_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def tnv_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def tnv_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def tnv_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def tnv_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def tnv_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def tnv_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def tnv_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def tnv_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tnv_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def tnv_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def tnv_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def tnv_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def tnv_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def tnv_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def tnv_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def tnv_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tnv_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def tnv_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tnv_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def tnv_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def tnv_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def tnv_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

TURNOVER_RATIO_REGISTRY_001_075 = {
    "tnv_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_001_capitulation_signal},
    "tnv_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_002_capitulation_signal},
    "tnv_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_003_capitulation_signal},
    "tnv_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_004_capitulation_signal},
    "tnv_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_005_capitulation_signal},
    "tnv_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_006_capitulation_signal},
    "tnv_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_007_capitulation_signal},
    "tnv_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_008_capitulation_signal},
    "tnv_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_009_capitulation_signal},
    "tnv_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_010_capitulation_signal},
    "tnv_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_011_capitulation_signal},
    "tnv_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_012_capitulation_signal},
    "tnv_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_013_capitulation_signal},
    "tnv_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_014_capitulation_signal},
    "tnv_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_015_capitulation_signal},
    "tnv_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_016_capitulation_signal},
    "tnv_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_017_capitulation_signal},
    "tnv_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_018_capitulation_signal},
    "tnv_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_019_capitulation_signal},
    "tnv_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_020_capitulation_signal},
    "tnv_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_021_capitulation_signal},
    "tnv_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_022_capitulation_signal},
    "tnv_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_023_capitulation_signal},
    "tnv_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_024_capitulation_signal},
    "tnv_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_025_capitulation_signal},
    "tnv_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_026_capitulation_signal},
    "tnv_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_027_capitulation_signal},
    "tnv_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_028_capitulation_signal},
    "tnv_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_029_capitulation_signal},
    "tnv_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_030_capitulation_signal},
    "tnv_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_031_capitulation_signal},
    "tnv_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_032_capitulation_signal},
    "tnv_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_033_capitulation_signal},
    "tnv_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_034_capitulation_signal},
    "tnv_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_035_capitulation_signal},
    "tnv_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_036_capitulation_signal},
    "tnv_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_037_capitulation_signal},
    "tnv_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_038_capitulation_signal},
    "tnv_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_039_capitulation_signal},
    "tnv_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_040_capitulation_signal},
    "tnv_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_041_capitulation_signal},
    "tnv_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_042_capitulation_signal},
    "tnv_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_043_capitulation_signal},
    "tnv_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_044_capitulation_signal},
    "tnv_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_045_capitulation_signal},
    "tnv_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_046_capitulation_signal},
    "tnv_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_047_capitulation_signal},
    "tnv_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_048_capitulation_signal},
    "tnv_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_049_capitulation_signal},
    "tnv_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_050_capitulation_signal},
    "tnv_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_051_capitulation_signal},
    "tnv_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_052_capitulation_signal},
    "tnv_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_053_capitulation_signal},
    "tnv_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_054_capitulation_signal},
    "tnv_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_055_capitulation_signal},
    "tnv_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_056_capitulation_signal},
    "tnv_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_057_capitulation_signal},
    "tnv_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_058_capitulation_signal},
    "tnv_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_059_capitulation_signal},
    "tnv_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_060_capitulation_signal},
    "tnv_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_061_capitulation_signal},
    "tnv_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_062_capitulation_signal},
    "tnv_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_063_capitulation_signal},
    "tnv_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_064_capitulation_signal},
    "tnv_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_065_capitulation_signal},
    "tnv_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_066_capitulation_signal},
    "tnv_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_067_capitulation_signal},
    "tnv_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_068_capitulation_signal},
    "tnv_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_069_capitulation_signal},
    "tnv_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_070_capitulation_signal},
    "tnv_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_071_capitulation_signal},
    "tnv_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_072_capitulation_signal},
    "tnv_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_073_capitulation_signal},
    "tnv_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_074_capitulation_signal},
    "tnv_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tnv_075_capitulation_signal},
}
