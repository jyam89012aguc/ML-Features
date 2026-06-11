"""Generated capitulation features for 24_volume_distribution: volume distribution shape.
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

def vds_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vds_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vds_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vds_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vds_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vds_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vds_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vds_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vds_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vds_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vds_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vds_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vds_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vds_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vds_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vds_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vds_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vds_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vds_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vds_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vds_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vds_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vds_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vds_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vds_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vds_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vds_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vds_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vds_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vds_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vds_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vds_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vds_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vds_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vds_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vds_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vds_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vds_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vds_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vds_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vds_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vds_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vds_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vds_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vds_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vds_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vds_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vds_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vds_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vds_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vds_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vds_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vds_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vds_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vds_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vds_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vds_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vds_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vds_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vds_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vds_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vds_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_DISTRIBUTION_REGISTRY_001_075 = {
    "vds_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_001_capitulation_signal},
    "vds_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_002_capitulation_signal},
    "vds_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_003_capitulation_signal},
    "vds_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_004_capitulation_signal},
    "vds_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_005_capitulation_signal},
    "vds_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_006_capitulation_signal},
    "vds_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_007_capitulation_signal},
    "vds_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_008_capitulation_signal},
    "vds_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_009_capitulation_signal},
    "vds_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_010_capitulation_signal},
    "vds_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_011_capitulation_signal},
    "vds_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_012_capitulation_signal},
    "vds_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_013_capitulation_signal},
    "vds_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_014_capitulation_signal},
    "vds_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_015_capitulation_signal},
    "vds_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_016_capitulation_signal},
    "vds_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_017_capitulation_signal},
    "vds_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_018_capitulation_signal},
    "vds_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_019_capitulation_signal},
    "vds_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_020_capitulation_signal},
    "vds_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_021_capitulation_signal},
    "vds_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_022_capitulation_signal},
    "vds_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_023_capitulation_signal},
    "vds_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_024_capitulation_signal},
    "vds_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_025_capitulation_signal},
    "vds_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_026_capitulation_signal},
    "vds_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_027_capitulation_signal},
    "vds_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_028_capitulation_signal},
    "vds_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_029_capitulation_signal},
    "vds_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_030_capitulation_signal},
    "vds_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_031_capitulation_signal},
    "vds_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_032_capitulation_signal},
    "vds_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_033_capitulation_signal},
    "vds_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_034_capitulation_signal},
    "vds_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_035_capitulation_signal},
    "vds_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_036_capitulation_signal},
    "vds_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_037_capitulation_signal},
    "vds_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_038_capitulation_signal},
    "vds_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_039_capitulation_signal},
    "vds_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_040_capitulation_signal},
    "vds_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_041_capitulation_signal},
    "vds_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_042_capitulation_signal},
    "vds_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_043_capitulation_signal},
    "vds_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_044_capitulation_signal},
    "vds_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_045_capitulation_signal},
    "vds_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_046_capitulation_signal},
    "vds_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_047_capitulation_signal},
    "vds_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_048_capitulation_signal},
    "vds_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_049_capitulation_signal},
    "vds_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_050_capitulation_signal},
    "vds_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_051_capitulation_signal},
    "vds_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_052_capitulation_signal},
    "vds_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_053_capitulation_signal},
    "vds_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_054_capitulation_signal},
    "vds_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_055_capitulation_signal},
    "vds_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_056_capitulation_signal},
    "vds_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_057_capitulation_signal},
    "vds_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_058_capitulation_signal},
    "vds_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_059_capitulation_signal},
    "vds_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_060_capitulation_signal},
    "vds_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_061_capitulation_signal},
    "vds_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_062_capitulation_signal},
    "vds_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_063_capitulation_signal},
    "vds_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_064_capitulation_signal},
    "vds_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_065_capitulation_signal},
    "vds_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_066_capitulation_signal},
    "vds_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_067_capitulation_signal},
    "vds_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_068_capitulation_signal},
    "vds_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_069_capitulation_signal},
    "vds_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_070_capitulation_signal},
    "vds_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_071_capitulation_signal},
    "vds_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_072_capitulation_signal},
    "vds_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_073_capitulation_signal},
    "vds_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_074_capitulation_signal},
    "vds_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vds_075_capitulation_signal},
}
