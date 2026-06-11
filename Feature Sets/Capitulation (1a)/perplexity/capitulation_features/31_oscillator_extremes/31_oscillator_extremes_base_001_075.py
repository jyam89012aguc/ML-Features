"""Generated capitulation features for 31_oscillator_extremes: stochastic extremes.
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

def osc_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def osc_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def osc_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def osc_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def osc_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def osc_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def osc_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def osc_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def osc_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def osc_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def osc_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def osc_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def osc_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def osc_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def osc_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def osc_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def osc_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def osc_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def osc_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def osc_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def osc_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def osc_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def osc_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def osc_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def osc_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def osc_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def osc_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def osc_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def osc_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def osc_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def osc_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def osc_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def osc_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def osc_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def osc_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def osc_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def osc_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def osc_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def osc_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def osc_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def osc_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def osc_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def osc_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def osc_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def osc_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def osc_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def osc_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def osc_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def osc_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def osc_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def osc_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def osc_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def osc_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def osc_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def osc_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def osc_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def osc_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def osc_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def osc_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def osc_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def osc_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def osc_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

OSCILLATOR_EXTREMES_REGISTRY_001_075 = {
    "osc_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_001_capitulation_signal},
    "osc_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_002_capitulation_signal},
    "osc_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_003_capitulation_signal},
    "osc_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_004_capitulation_signal},
    "osc_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_005_capitulation_signal},
    "osc_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_006_capitulation_signal},
    "osc_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_007_capitulation_signal},
    "osc_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_008_capitulation_signal},
    "osc_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_009_capitulation_signal},
    "osc_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_010_capitulation_signal},
    "osc_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_011_capitulation_signal},
    "osc_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_012_capitulation_signal},
    "osc_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_013_capitulation_signal},
    "osc_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_014_capitulation_signal},
    "osc_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_015_capitulation_signal},
    "osc_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_016_capitulation_signal},
    "osc_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_017_capitulation_signal},
    "osc_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_018_capitulation_signal},
    "osc_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_019_capitulation_signal},
    "osc_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_020_capitulation_signal},
    "osc_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_021_capitulation_signal},
    "osc_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_022_capitulation_signal},
    "osc_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_023_capitulation_signal},
    "osc_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_024_capitulation_signal},
    "osc_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_025_capitulation_signal},
    "osc_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_026_capitulation_signal},
    "osc_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_027_capitulation_signal},
    "osc_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_028_capitulation_signal},
    "osc_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_029_capitulation_signal},
    "osc_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_030_capitulation_signal},
    "osc_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_031_capitulation_signal},
    "osc_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_032_capitulation_signal},
    "osc_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_033_capitulation_signal},
    "osc_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_034_capitulation_signal},
    "osc_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_035_capitulation_signal},
    "osc_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_036_capitulation_signal},
    "osc_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_037_capitulation_signal},
    "osc_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_038_capitulation_signal},
    "osc_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_039_capitulation_signal},
    "osc_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_040_capitulation_signal},
    "osc_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_041_capitulation_signal},
    "osc_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_042_capitulation_signal},
    "osc_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_043_capitulation_signal},
    "osc_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_044_capitulation_signal},
    "osc_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_045_capitulation_signal},
    "osc_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_046_capitulation_signal},
    "osc_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_047_capitulation_signal},
    "osc_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_048_capitulation_signal},
    "osc_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_049_capitulation_signal},
    "osc_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_050_capitulation_signal},
    "osc_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_051_capitulation_signal},
    "osc_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_052_capitulation_signal},
    "osc_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_053_capitulation_signal},
    "osc_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_054_capitulation_signal},
    "osc_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_055_capitulation_signal},
    "osc_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_056_capitulation_signal},
    "osc_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_057_capitulation_signal},
    "osc_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_058_capitulation_signal},
    "osc_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_059_capitulation_signal},
    "osc_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_060_capitulation_signal},
    "osc_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_061_capitulation_signal},
    "osc_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_062_capitulation_signal},
    "osc_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_063_capitulation_signal},
    "osc_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_064_capitulation_signal},
    "osc_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_065_capitulation_signal},
    "osc_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_066_capitulation_signal},
    "osc_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_067_capitulation_signal},
    "osc_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_068_capitulation_signal},
    "osc_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_069_capitulation_signal},
    "osc_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_070_capitulation_signal},
    "osc_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_071_capitulation_signal},
    "osc_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_072_capitulation_signal},
    "osc_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_073_capitulation_signal},
    "osc_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_074_capitulation_signal},
    "osc_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": osc_075_capitulation_signal},
}
