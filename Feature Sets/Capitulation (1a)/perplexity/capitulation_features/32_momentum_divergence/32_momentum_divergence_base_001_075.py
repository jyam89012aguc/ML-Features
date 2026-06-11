"""Generated capitulation features for 32_momentum_divergence: price new low without momentum new low.
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

def mdv_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def mdv_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def mdv_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def mdv_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def mdv_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mdv_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def mdv_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def mdv_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def mdv_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def mdv_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def mdv_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def mdv_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def mdv_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def mdv_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def mdv_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def mdv_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def mdv_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def mdv_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def mdv_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mdv_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def mdv_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def mdv_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def mdv_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def mdv_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def mdv_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def mdv_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def mdv_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def mdv_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def mdv_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def mdv_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def mdv_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def mdv_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def mdv_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mdv_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def mdv_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def mdv_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def mdv_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def mdv_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def mdv_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def mdv_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def mdv_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def mdv_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def mdv_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def mdv_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def mdv_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def mdv_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def mdv_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mdv_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mdv_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def mdv_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def mdv_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def mdv_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def mdv_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def mdv_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def mdv_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdv_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def mdv_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdv_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def mdv_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def mdv_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def mdv_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

MOMENTUM_DIVERGENCE_REGISTRY_001_075 = {
    "mdv_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_001_capitulation_signal},
    "mdv_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_002_capitulation_signal},
    "mdv_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_003_capitulation_signal},
    "mdv_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_004_capitulation_signal},
    "mdv_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_005_capitulation_signal},
    "mdv_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_006_capitulation_signal},
    "mdv_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_007_capitulation_signal},
    "mdv_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_008_capitulation_signal},
    "mdv_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_009_capitulation_signal},
    "mdv_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_010_capitulation_signal},
    "mdv_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_011_capitulation_signal},
    "mdv_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_012_capitulation_signal},
    "mdv_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_013_capitulation_signal},
    "mdv_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_014_capitulation_signal},
    "mdv_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_015_capitulation_signal},
    "mdv_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_016_capitulation_signal},
    "mdv_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_017_capitulation_signal},
    "mdv_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_018_capitulation_signal},
    "mdv_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_019_capitulation_signal},
    "mdv_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_020_capitulation_signal},
    "mdv_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_021_capitulation_signal},
    "mdv_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_022_capitulation_signal},
    "mdv_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_023_capitulation_signal},
    "mdv_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_024_capitulation_signal},
    "mdv_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_025_capitulation_signal},
    "mdv_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_026_capitulation_signal},
    "mdv_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_027_capitulation_signal},
    "mdv_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_028_capitulation_signal},
    "mdv_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_029_capitulation_signal},
    "mdv_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_030_capitulation_signal},
    "mdv_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_031_capitulation_signal},
    "mdv_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_032_capitulation_signal},
    "mdv_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_033_capitulation_signal},
    "mdv_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_034_capitulation_signal},
    "mdv_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_035_capitulation_signal},
    "mdv_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_036_capitulation_signal},
    "mdv_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_037_capitulation_signal},
    "mdv_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_038_capitulation_signal},
    "mdv_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_039_capitulation_signal},
    "mdv_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_040_capitulation_signal},
    "mdv_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_041_capitulation_signal},
    "mdv_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_042_capitulation_signal},
    "mdv_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_043_capitulation_signal},
    "mdv_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_044_capitulation_signal},
    "mdv_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_045_capitulation_signal},
    "mdv_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_046_capitulation_signal},
    "mdv_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_047_capitulation_signal},
    "mdv_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_048_capitulation_signal},
    "mdv_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_049_capitulation_signal},
    "mdv_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_050_capitulation_signal},
    "mdv_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_051_capitulation_signal},
    "mdv_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_052_capitulation_signal},
    "mdv_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_053_capitulation_signal},
    "mdv_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_054_capitulation_signal},
    "mdv_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_055_capitulation_signal},
    "mdv_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_056_capitulation_signal},
    "mdv_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_057_capitulation_signal},
    "mdv_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_058_capitulation_signal},
    "mdv_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_059_capitulation_signal},
    "mdv_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_060_capitulation_signal},
    "mdv_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_061_capitulation_signal},
    "mdv_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_062_capitulation_signal},
    "mdv_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_063_capitulation_signal},
    "mdv_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_064_capitulation_signal},
    "mdv_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_065_capitulation_signal},
    "mdv_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_066_capitulation_signal},
    "mdv_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_067_capitulation_signal},
    "mdv_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_068_capitulation_signal},
    "mdv_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_069_capitulation_signal},
    "mdv_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_070_capitulation_signal},
    "mdv_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_071_capitulation_signal},
    "mdv_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_072_capitulation_signal},
    "mdv_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_073_capitulation_signal},
    "mdv_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_074_capitulation_signal},
    "mdv_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdv_075_capitulation_signal},
}
