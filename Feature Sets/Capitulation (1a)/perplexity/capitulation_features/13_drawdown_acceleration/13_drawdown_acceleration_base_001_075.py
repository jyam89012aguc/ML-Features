"""Generated capitulation features for 13_drawdown_acceleration: whether decline is speeding up.
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

def dacc_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dacc_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dacc_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dacc_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dacc_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dacc_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dacc_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dacc_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dacc_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dacc_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dacc_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dacc_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dacc_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dacc_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dacc_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dacc_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dacc_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dacc_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dacc_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dacc_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dacc_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dacc_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dacc_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dacc_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dacc_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dacc_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dacc_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dacc_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dacc_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dacc_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dacc_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dacc_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dacc_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dacc_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dacc_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dacc_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dacc_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dacc_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dacc_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dacc_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dacc_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dacc_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dacc_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dacc_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dacc_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dacc_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dacc_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dacc_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dacc_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dacc_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dacc_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dacc_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dacc_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dacc_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dacc_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dacc_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dacc_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dacc_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dacc_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dacc_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dacc_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DRAWDOWN_ACCELERATION_REGISTRY_001_075 = {
    "dacc_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_001_capitulation_signal},
    "dacc_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_002_capitulation_signal},
    "dacc_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_003_capitulation_signal},
    "dacc_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_004_capitulation_signal},
    "dacc_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_005_capitulation_signal},
    "dacc_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_006_capitulation_signal},
    "dacc_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_007_capitulation_signal},
    "dacc_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_008_capitulation_signal},
    "dacc_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_009_capitulation_signal},
    "dacc_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_010_capitulation_signal},
    "dacc_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_011_capitulation_signal},
    "dacc_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_012_capitulation_signal},
    "dacc_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_013_capitulation_signal},
    "dacc_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_014_capitulation_signal},
    "dacc_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_015_capitulation_signal},
    "dacc_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_016_capitulation_signal},
    "dacc_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_017_capitulation_signal},
    "dacc_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_018_capitulation_signal},
    "dacc_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_019_capitulation_signal},
    "dacc_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_020_capitulation_signal},
    "dacc_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_021_capitulation_signal},
    "dacc_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_022_capitulation_signal},
    "dacc_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_023_capitulation_signal},
    "dacc_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_024_capitulation_signal},
    "dacc_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_025_capitulation_signal},
    "dacc_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_026_capitulation_signal},
    "dacc_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_027_capitulation_signal},
    "dacc_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_028_capitulation_signal},
    "dacc_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_029_capitulation_signal},
    "dacc_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_030_capitulation_signal},
    "dacc_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_031_capitulation_signal},
    "dacc_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_032_capitulation_signal},
    "dacc_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_033_capitulation_signal},
    "dacc_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_034_capitulation_signal},
    "dacc_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_035_capitulation_signal},
    "dacc_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_036_capitulation_signal},
    "dacc_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_037_capitulation_signal},
    "dacc_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_038_capitulation_signal},
    "dacc_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_039_capitulation_signal},
    "dacc_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_040_capitulation_signal},
    "dacc_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_041_capitulation_signal},
    "dacc_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_042_capitulation_signal},
    "dacc_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_043_capitulation_signal},
    "dacc_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_044_capitulation_signal},
    "dacc_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_045_capitulation_signal},
    "dacc_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_046_capitulation_signal},
    "dacc_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_047_capitulation_signal},
    "dacc_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_048_capitulation_signal},
    "dacc_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_049_capitulation_signal},
    "dacc_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_050_capitulation_signal},
    "dacc_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_051_capitulation_signal},
    "dacc_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_052_capitulation_signal},
    "dacc_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_053_capitulation_signal},
    "dacc_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_054_capitulation_signal},
    "dacc_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_055_capitulation_signal},
    "dacc_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_056_capitulation_signal},
    "dacc_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_057_capitulation_signal},
    "dacc_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_058_capitulation_signal},
    "dacc_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_059_capitulation_signal},
    "dacc_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_060_capitulation_signal},
    "dacc_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_061_capitulation_signal},
    "dacc_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_062_capitulation_signal},
    "dacc_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_063_capitulation_signal},
    "dacc_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_064_capitulation_signal},
    "dacc_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_065_capitulation_signal},
    "dacc_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_066_capitulation_signal},
    "dacc_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_067_capitulation_signal},
    "dacc_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_068_capitulation_signal},
    "dacc_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_069_capitulation_signal},
    "dacc_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_070_capitulation_signal},
    "dacc_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_071_capitulation_signal},
    "dacc_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_072_capitulation_signal},
    "dacc_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_073_capitulation_signal},
    "dacc_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_074_capitulation_signal},
    "dacc_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dacc_075_capitulation_signal},
}
