"""Generated capitulation features for 05_underwater_curve: area/depth of underwater equity curve.
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

def uw_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def uw_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def uw_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def uw_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def uw_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def uw_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def uw_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def uw_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def uw_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def uw_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def uw_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def uw_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def uw_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def uw_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def uw_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def uw_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def uw_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def uw_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def uw_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def uw_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def uw_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def uw_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def uw_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def uw_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def uw_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def uw_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def uw_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def uw_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def uw_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def uw_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def uw_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def uw_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def uw_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def uw_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def uw_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def uw_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def uw_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def uw_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def uw_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def uw_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def uw_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def uw_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def uw_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def uw_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def uw_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def uw_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def uw_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def uw_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def uw_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def uw_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def uw_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def uw_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def uw_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def uw_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def uw_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def uw_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def uw_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def uw_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def uw_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def uw_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def uw_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def uw_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

UNDERWATER_CURVE_REGISTRY_001_075 = {
    "uw_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_001_capitulation_signal},
    "uw_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_002_capitulation_signal},
    "uw_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_003_capitulation_signal},
    "uw_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_004_capitulation_signal},
    "uw_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_005_capitulation_signal},
    "uw_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_006_capitulation_signal},
    "uw_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_007_capitulation_signal},
    "uw_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_008_capitulation_signal},
    "uw_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_009_capitulation_signal},
    "uw_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_010_capitulation_signal},
    "uw_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_011_capitulation_signal},
    "uw_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_012_capitulation_signal},
    "uw_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_013_capitulation_signal},
    "uw_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_014_capitulation_signal},
    "uw_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_015_capitulation_signal},
    "uw_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_016_capitulation_signal},
    "uw_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_017_capitulation_signal},
    "uw_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_018_capitulation_signal},
    "uw_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_019_capitulation_signal},
    "uw_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_020_capitulation_signal},
    "uw_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_021_capitulation_signal},
    "uw_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_022_capitulation_signal},
    "uw_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_023_capitulation_signal},
    "uw_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_024_capitulation_signal},
    "uw_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_025_capitulation_signal},
    "uw_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_026_capitulation_signal},
    "uw_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_027_capitulation_signal},
    "uw_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_028_capitulation_signal},
    "uw_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_029_capitulation_signal},
    "uw_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_030_capitulation_signal},
    "uw_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_031_capitulation_signal},
    "uw_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_032_capitulation_signal},
    "uw_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_033_capitulation_signal},
    "uw_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_034_capitulation_signal},
    "uw_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_035_capitulation_signal},
    "uw_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_036_capitulation_signal},
    "uw_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_037_capitulation_signal},
    "uw_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_038_capitulation_signal},
    "uw_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_039_capitulation_signal},
    "uw_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_040_capitulation_signal},
    "uw_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_041_capitulation_signal},
    "uw_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_042_capitulation_signal},
    "uw_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_043_capitulation_signal},
    "uw_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_044_capitulation_signal},
    "uw_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_045_capitulation_signal},
    "uw_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_046_capitulation_signal},
    "uw_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_047_capitulation_signal},
    "uw_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_048_capitulation_signal},
    "uw_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_049_capitulation_signal},
    "uw_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_050_capitulation_signal},
    "uw_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_051_capitulation_signal},
    "uw_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_052_capitulation_signal},
    "uw_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_053_capitulation_signal},
    "uw_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_054_capitulation_signal},
    "uw_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_055_capitulation_signal},
    "uw_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_056_capitulation_signal},
    "uw_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_057_capitulation_signal},
    "uw_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_058_capitulation_signal},
    "uw_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_059_capitulation_signal},
    "uw_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_060_capitulation_signal},
    "uw_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_061_capitulation_signal},
    "uw_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_062_capitulation_signal},
    "uw_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_063_capitulation_signal},
    "uw_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_064_capitulation_signal},
    "uw_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_065_capitulation_signal},
    "uw_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_066_capitulation_signal},
    "uw_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_067_capitulation_signal},
    "uw_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_068_capitulation_signal},
    "uw_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_069_capitulation_signal},
    "uw_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_070_capitulation_signal},
    "uw_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_071_capitulation_signal},
    "uw_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_072_capitulation_signal},
    "uw_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_073_capitulation_signal},
    "uw_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_074_capitulation_signal},
    "uw_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": uw_075_capitulation_signal},
}
