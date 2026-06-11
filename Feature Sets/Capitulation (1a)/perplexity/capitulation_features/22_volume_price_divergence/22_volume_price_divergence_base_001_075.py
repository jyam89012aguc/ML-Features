"""Generated capitulation features for 22_volume_price_divergence: volume rising while price falls.
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

def vpd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vpd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vpd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vpd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vpd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vpd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vpd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vpd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vpd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vpd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vpd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vpd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vpd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vpd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vpd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vpd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vpd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vpd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vpd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vpd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vpd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vpd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vpd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vpd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vpd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vpd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vpd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vpd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vpd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vpd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vpd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vpd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vpd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vpd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vpd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vpd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vpd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vpd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vpd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vpd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vpd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vpd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vpd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vpd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vpd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vpd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vpd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vpd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vpd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vpd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vpd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vpd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vpd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vpd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vpd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vpd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vpd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vpd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vpd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vpd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vpd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_PRICE_DIVERGENCE_REGISTRY_001_075 = {
    "vpd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_001_capitulation_signal},
    "vpd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_002_capitulation_signal},
    "vpd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_003_capitulation_signal},
    "vpd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_004_capitulation_signal},
    "vpd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_005_capitulation_signal},
    "vpd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_006_capitulation_signal},
    "vpd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_007_capitulation_signal},
    "vpd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_008_capitulation_signal},
    "vpd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_009_capitulation_signal},
    "vpd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_010_capitulation_signal},
    "vpd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_011_capitulation_signal},
    "vpd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_012_capitulation_signal},
    "vpd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_013_capitulation_signal},
    "vpd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_014_capitulation_signal},
    "vpd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_015_capitulation_signal},
    "vpd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_016_capitulation_signal},
    "vpd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_017_capitulation_signal},
    "vpd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_018_capitulation_signal},
    "vpd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_019_capitulation_signal},
    "vpd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_020_capitulation_signal},
    "vpd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_021_capitulation_signal},
    "vpd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_022_capitulation_signal},
    "vpd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_023_capitulation_signal},
    "vpd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_024_capitulation_signal},
    "vpd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_025_capitulation_signal},
    "vpd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_026_capitulation_signal},
    "vpd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_027_capitulation_signal},
    "vpd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_028_capitulation_signal},
    "vpd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_029_capitulation_signal},
    "vpd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_030_capitulation_signal},
    "vpd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_031_capitulation_signal},
    "vpd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_032_capitulation_signal},
    "vpd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_033_capitulation_signal},
    "vpd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_034_capitulation_signal},
    "vpd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_035_capitulation_signal},
    "vpd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_036_capitulation_signal},
    "vpd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_037_capitulation_signal},
    "vpd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_038_capitulation_signal},
    "vpd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_039_capitulation_signal},
    "vpd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_040_capitulation_signal},
    "vpd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_041_capitulation_signal},
    "vpd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_042_capitulation_signal},
    "vpd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_043_capitulation_signal},
    "vpd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_044_capitulation_signal},
    "vpd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_045_capitulation_signal},
    "vpd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_046_capitulation_signal},
    "vpd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_047_capitulation_signal},
    "vpd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_048_capitulation_signal},
    "vpd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_049_capitulation_signal},
    "vpd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_050_capitulation_signal},
    "vpd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_051_capitulation_signal},
    "vpd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_052_capitulation_signal},
    "vpd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_053_capitulation_signal},
    "vpd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_054_capitulation_signal},
    "vpd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_055_capitulation_signal},
    "vpd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_056_capitulation_signal},
    "vpd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_057_capitulation_signal},
    "vpd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_058_capitulation_signal},
    "vpd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_059_capitulation_signal},
    "vpd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_060_capitulation_signal},
    "vpd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_061_capitulation_signal},
    "vpd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_062_capitulation_signal},
    "vpd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_063_capitulation_signal},
    "vpd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_064_capitulation_signal},
    "vpd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_065_capitulation_signal},
    "vpd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_066_capitulation_signal},
    "vpd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_067_capitulation_signal},
    "vpd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_068_capitulation_signal},
    "vpd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_069_capitulation_signal},
    "vpd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_070_capitulation_signal},
    "vpd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_071_capitulation_signal},
    "vpd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_072_capitulation_signal},
    "vpd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_073_capitulation_signal},
    "vpd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_074_capitulation_signal},
    "vpd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vpd_075_capitulation_signal},
}
