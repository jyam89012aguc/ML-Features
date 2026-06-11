"""Generated capitulation features for 29_consecutive_loss: loss streaks.
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

def ccl_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def ccl_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def ccl_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def ccl_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def ccl_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ccl_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def ccl_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def ccl_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def ccl_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def ccl_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def ccl_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def ccl_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def ccl_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def ccl_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def ccl_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def ccl_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def ccl_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def ccl_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def ccl_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ccl_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def ccl_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def ccl_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def ccl_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def ccl_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def ccl_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def ccl_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def ccl_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def ccl_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def ccl_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def ccl_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def ccl_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def ccl_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def ccl_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ccl_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def ccl_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def ccl_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def ccl_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def ccl_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def ccl_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def ccl_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def ccl_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def ccl_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def ccl_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def ccl_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def ccl_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def ccl_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def ccl_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ccl_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ccl_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def ccl_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def ccl_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def ccl_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def ccl_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def ccl_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def ccl_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ccl_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def ccl_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ccl_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def ccl_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def ccl_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def ccl_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

CONSECUTIVE_LOSS_REGISTRY_001_075 = {
    "ccl_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_001_capitulation_signal},
    "ccl_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_002_capitulation_signal},
    "ccl_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_003_capitulation_signal},
    "ccl_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_004_capitulation_signal},
    "ccl_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_005_capitulation_signal},
    "ccl_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_006_capitulation_signal},
    "ccl_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_007_capitulation_signal},
    "ccl_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_008_capitulation_signal},
    "ccl_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_009_capitulation_signal},
    "ccl_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_010_capitulation_signal},
    "ccl_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_011_capitulation_signal},
    "ccl_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_012_capitulation_signal},
    "ccl_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_013_capitulation_signal},
    "ccl_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_014_capitulation_signal},
    "ccl_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_015_capitulation_signal},
    "ccl_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_016_capitulation_signal},
    "ccl_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_017_capitulation_signal},
    "ccl_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_018_capitulation_signal},
    "ccl_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_019_capitulation_signal},
    "ccl_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_020_capitulation_signal},
    "ccl_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_021_capitulation_signal},
    "ccl_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_022_capitulation_signal},
    "ccl_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_023_capitulation_signal},
    "ccl_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_024_capitulation_signal},
    "ccl_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_025_capitulation_signal},
    "ccl_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_026_capitulation_signal},
    "ccl_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_027_capitulation_signal},
    "ccl_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_028_capitulation_signal},
    "ccl_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_029_capitulation_signal},
    "ccl_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_030_capitulation_signal},
    "ccl_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_031_capitulation_signal},
    "ccl_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_032_capitulation_signal},
    "ccl_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_033_capitulation_signal},
    "ccl_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_034_capitulation_signal},
    "ccl_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_035_capitulation_signal},
    "ccl_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_036_capitulation_signal},
    "ccl_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_037_capitulation_signal},
    "ccl_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_038_capitulation_signal},
    "ccl_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_039_capitulation_signal},
    "ccl_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_040_capitulation_signal},
    "ccl_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_041_capitulation_signal},
    "ccl_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_042_capitulation_signal},
    "ccl_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_043_capitulation_signal},
    "ccl_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_044_capitulation_signal},
    "ccl_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_045_capitulation_signal},
    "ccl_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_046_capitulation_signal},
    "ccl_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_047_capitulation_signal},
    "ccl_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_048_capitulation_signal},
    "ccl_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_049_capitulation_signal},
    "ccl_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_050_capitulation_signal},
    "ccl_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_051_capitulation_signal},
    "ccl_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_052_capitulation_signal},
    "ccl_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_053_capitulation_signal},
    "ccl_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_054_capitulation_signal},
    "ccl_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_055_capitulation_signal},
    "ccl_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_056_capitulation_signal},
    "ccl_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_057_capitulation_signal},
    "ccl_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_058_capitulation_signal},
    "ccl_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_059_capitulation_signal},
    "ccl_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_060_capitulation_signal},
    "ccl_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_061_capitulation_signal},
    "ccl_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_062_capitulation_signal},
    "ccl_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_063_capitulation_signal},
    "ccl_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_064_capitulation_signal},
    "ccl_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_065_capitulation_signal},
    "ccl_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_066_capitulation_signal},
    "ccl_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_067_capitulation_signal},
    "ccl_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_068_capitulation_signal},
    "ccl_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_069_capitulation_signal},
    "ccl_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_070_capitulation_signal},
    "ccl_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_071_capitulation_signal},
    "ccl_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_072_capitulation_signal},
    "ccl_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_073_capitulation_signal},
    "ccl_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_074_capitulation_signal},
    "ccl_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ccl_075_capitulation_signal},
}
