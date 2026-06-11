"""Generated capitulation features for 03_drawdown_shape: convexity/concavity of decline path.
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

def dsh_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dsh_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dsh_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dsh_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dsh_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dsh_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dsh_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dsh_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dsh_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dsh_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dsh_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dsh_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dsh_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dsh_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dsh_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dsh_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dsh_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dsh_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dsh_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dsh_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dsh_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dsh_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dsh_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dsh_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dsh_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dsh_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dsh_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dsh_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dsh_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dsh_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dsh_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dsh_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dsh_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dsh_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dsh_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dsh_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dsh_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dsh_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dsh_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dsh_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dsh_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dsh_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dsh_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dsh_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dsh_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dsh_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dsh_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dsh_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dsh_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dsh_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dsh_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dsh_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dsh_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dsh_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dsh_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dsh_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dsh_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dsh_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dsh_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dsh_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dsh_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DRAWDOWN_SHAPE_REGISTRY_001_075 = {
    "dsh_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_001_capitulation_signal},
    "dsh_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_002_capitulation_signal},
    "dsh_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_003_capitulation_signal},
    "dsh_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_004_capitulation_signal},
    "dsh_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_005_capitulation_signal},
    "dsh_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_006_capitulation_signal},
    "dsh_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_007_capitulation_signal},
    "dsh_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_008_capitulation_signal},
    "dsh_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_009_capitulation_signal},
    "dsh_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_010_capitulation_signal},
    "dsh_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_011_capitulation_signal},
    "dsh_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_012_capitulation_signal},
    "dsh_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_013_capitulation_signal},
    "dsh_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_014_capitulation_signal},
    "dsh_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_015_capitulation_signal},
    "dsh_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_016_capitulation_signal},
    "dsh_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_017_capitulation_signal},
    "dsh_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_018_capitulation_signal},
    "dsh_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_019_capitulation_signal},
    "dsh_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_020_capitulation_signal},
    "dsh_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_021_capitulation_signal},
    "dsh_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_022_capitulation_signal},
    "dsh_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_023_capitulation_signal},
    "dsh_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_024_capitulation_signal},
    "dsh_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_025_capitulation_signal},
    "dsh_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_026_capitulation_signal},
    "dsh_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_027_capitulation_signal},
    "dsh_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_028_capitulation_signal},
    "dsh_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_029_capitulation_signal},
    "dsh_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_030_capitulation_signal},
    "dsh_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_031_capitulation_signal},
    "dsh_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_032_capitulation_signal},
    "dsh_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_033_capitulation_signal},
    "dsh_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_034_capitulation_signal},
    "dsh_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_035_capitulation_signal},
    "dsh_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_036_capitulation_signal},
    "dsh_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_037_capitulation_signal},
    "dsh_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_038_capitulation_signal},
    "dsh_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_039_capitulation_signal},
    "dsh_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_040_capitulation_signal},
    "dsh_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_041_capitulation_signal},
    "dsh_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_042_capitulation_signal},
    "dsh_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_043_capitulation_signal},
    "dsh_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_044_capitulation_signal},
    "dsh_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_045_capitulation_signal},
    "dsh_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_046_capitulation_signal},
    "dsh_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_047_capitulation_signal},
    "dsh_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_048_capitulation_signal},
    "dsh_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_049_capitulation_signal},
    "dsh_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_050_capitulation_signal},
    "dsh_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_051_capitulation_signal},
    "dsh_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_052_capitulation_signal},
    "dsh_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_053_capitulation_signal},
    "dsh_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_054_capitulation_signal},
    "dsh_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_055_capitulation_signal},
    "dsh_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_056_capitulation_signal},
    "dsh_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_057_capitulation_signal},
    "dsh_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_058_capitulation_signal},
    "dsh_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_059_capitulation_signal},
    "dsh_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_060_capitulation_signal},
    "dsh_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_061_capitulation_signal},
    "dsh_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_062_capitulation_signal},
    "dsh_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_063_capitulation_signal},
    "dsh_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_064_capitulation_signal},
    "dsh_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_065_capitulation_signal},
    "dsh_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_066_capitulation_signal},
    "dsh_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_067_capitulation_signal},
    "dsh_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_068_capitulation_signal},
    "dsh_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_069_capitulation_signal},
    "dsh_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_070_capitulation_signal},
    "dsh_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_071_capitulation_signal},
    "dsh_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_072_capitulation_signal},
    "dsh_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_073_capitulation_signal},
    "dsh_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_074_capitulation_signal},
    "dsh_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dsh_075_capitulation_signal},
}
