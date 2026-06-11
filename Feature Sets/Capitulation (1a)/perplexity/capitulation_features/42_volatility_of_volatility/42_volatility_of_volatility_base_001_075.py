"""Generated capitulation features for 42_volatility_of_volatility: instability of volatility.
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

def vov_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vov_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vov_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vov_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vov_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vov_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vov_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vov_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vov_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vov_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vov_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vov_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vov_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vov_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vov_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vov_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vov_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vov_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vov_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vov_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vov_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vov_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vov_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vov_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vov_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vov_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vov_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vov_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vov_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vov_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vov_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vov_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vov_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vov_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vov_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vov_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vov_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vov_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vov_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vov_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vov_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vov_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vov_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vov_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vov_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vov_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vov_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vov_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vov_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vov_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vov_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vov_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vov_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vov_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vov_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vov_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vov_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vov_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vov_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vov_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vov_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vov_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLATILITY_OF_VOLATILITY_REGISTRY_001_075 = {
    "vov_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_001_capitulation_signal},
    "vov_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_002_capitulation_signal},
    "vov_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_003_capitulation_signal},
    "vov_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_004_capitulation_signal},
    "vov_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_005_capitulation_signal},
    "vov_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_006_capitulation_signal},
    "vov_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_007_capitulation_signal},
    "vov_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_008_capitulation_signal},
    "vov_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_009_capitulation_signal},
    "vov_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_010_capitulation_signal},
    "vov_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_011_capitulation_signal},
    "vov_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_012_capitulation_signal},
    "vov_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_013_capitulation_signal},
    "vov_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_014_capitulation_signal},
    "vov_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_015_capitulation_signal},
    "vov_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_016_capitulation_signal},
    "vov_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_017_capitulation_signal},
    "vov_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_018_capitulation_signal},
    "vov_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_019_capitulation_signal},
    "vov_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_020_capitulation_signal},
    "vov_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_021_capitulation_signal},
    "vov_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_022_capitulation_signal},
    "vov_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_023_capitulation_signal},
    "vov_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_024_capitulation_signal},
    "vov_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_025_capitulation_signal},
    "vov_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_026_capitulation_signal},
    "vov_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_027_capitulation_signal},
    "vov_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_028_capitulation_signal},
    "vov_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_029_capitulation_signal},
    "vov_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_030_capitulation_signal},
    "vov_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_031_capitulation_signal},
    "vov_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_032_capitulation_signal},
    "vov_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_033_capitulation_signal},
    "vov_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_034_capitulation_signal},
    "vov_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_035_capitulation_signal},
    "vov_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_036_capitulation_signal},
    "vov_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_037_capitulation_signal},
    "vov_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_038_capitulation_signal},
    "vov_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_039_capitulation_signal},
    "vov_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_040_capitulation_signal},
    "vov_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_041_capitulation_signal},
    "vov_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_042_capitulation_signal},
    "vov_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_043_capitulation_signal},
    "vov_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_044_capitulation_signal},
    "vov_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_045_capitulation_signal},
    "vov_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_046_capitulation_signal},
    "vov_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_047_capitulation_signal},
    "vov_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_048_capitulation_signal},
    "vov_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_049_capitulation_signal},
    "vov_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_050_capitulation_signal},
    "vov_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_051_capitulation_signal},
    "vov_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_052_capitulation_signal},
    "vov_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_053_capitulation_signal},
    "vov_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_054_capitulation_signal},
    "vov_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_055_capitulation_signal},
    "vov_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_056_capitulation_signal},
    "vov_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_057_capitulation_signal},
    "vov_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_058_capitulation_signal},
    "vov_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_059_capitulation_signal},
    "vov_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_060_capitulation_signal},
    "vov_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_061_capitulation_signal},
    "vov_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_062_capitulation_signal},
    "vov_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_063_capitulation_signal},
    "vov_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_064_capitulation_signal},
    "vov_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_065_capitulation_signal},
    "vov_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_066_capitulation_signal},
    "vov_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_067_capitulation_signal},
    "vov_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_068_capitulation_signal},
    "vov_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_069_capitulation_signal},
    "vov_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_070_capitulation_signal},
    "vov_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_071_capitulation_signal},
    "vov_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_072_capitulation_signal},
    "vov_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_073_capitulation_signal},
    "vov_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_074_capitulation_signal},
    "vov_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vov_075_capitulation_signal},
}
