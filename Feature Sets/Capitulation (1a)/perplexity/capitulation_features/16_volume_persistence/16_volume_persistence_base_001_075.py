"""Generated capitulation features for 16_volume_persistence: sustained elevated volume.
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

def vp_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vp_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vp_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vp_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vp_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vp_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vp_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vp_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vp_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vp_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vp_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vp_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vp_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vp_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vp_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vp_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vp_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vp_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vp_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vp_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vp_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vp_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vp_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vp_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vp_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vp_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vp_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vp_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vp_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vp_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vp_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vp_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vp_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vp_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vp_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vp_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vp_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vp_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vp_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vp_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vp_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vp_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vp_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vp_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vp_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vp_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vp_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vp_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vp_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vp_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vp_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vp_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vp_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vp_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vp_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vp_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vp_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vp_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vp_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vp_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vp_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vp_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_PERSISTENCE_REGISTRY_001_075 = {
    "vp_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_001_capitulation_signal},
    "vp_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_002_capitulation_signal},
    "vp_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_003_capitulation_signal},
    "vp_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_004_capitulation_signal},
    "vp_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_005_capitulation_signal},
    "vp_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_006_capitulation_signal},
    "vp_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_007_capitulation_signal},
    "vp_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_008_capitulation_signal},
    "vp_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_009_capitulation_signal},
    "vp_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_010_capitulation_signal},
    "vp_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_011_capitulation_signal},
    "vp_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_012_capitulation_signal},
    "vp_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_013_capitulation_signal},
    "vp_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_014_capitulation_signal},
    "vp_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_015_capitulation_signal},
    "vp_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_016_capitulation_signal},
    "vp_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_017_capitulation_signal},
    "vp_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_018_capitulation_signal},
    "vp_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_019_capitulation_signal},
    "vp_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_020_capitulation_signal},
    "vp_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_021_capitulation_signal},
    "vp_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_022_capitulation_signal},
    "vp_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_023_capitulation_signal},
    "vp_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_024_capitulation_signal},
    "vp_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_025_capitulation_signal},
    "vp_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_026_capitulation_signal},
    "vp_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_027_capitulation_signal},
    "vp_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_028_capitulation_signal},
    "vp_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_029_capitulation_signal},
    "vp_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_030_capitulation_signal},
    "vp_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_031_capitulation_signal},
    "vp_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_032_capitulation_signal},
    "vp_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_033_capitulation_signal},
    "vp_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_034_capitulation_signal},
    "vp_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_035_capitulation_signal},
    "vp_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_036_capitulation_signal},
    "vp_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_037_capitulation_signal},
    "vp_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_038_capitulation_signal},
    "vp_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_039_capitulation_signal},
    "vp_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_040_capitulation_signal},
    "vp_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_041_capitulation_signal},
    "vp_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_042_capitulation_signal},
    "vp_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_043_capitulation_signal},
    "vp_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_044_capitulation_signal},
    "vp_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_045_capitulation_signal},
    "vp_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_046_capitulation_signal},
    "vp_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_047_capitulation_signal},
    "vp_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_048_capitulation_signal},
    "vp_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_049_capitulation_signal},
    "vp_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_050_capitulation_signal},
    "vp_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_051_capitulation_signal},
    "vp_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_052_capitulation_signal},
    "vp_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_053_capitulation_signal},
    "vp_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_054_capitulation_signal},
    "vp_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_055_capitulation_signal},
    "vp_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_056_capitulation_signal},
    "vp_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_057_capitulation_signal},
    "vp_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_058_capitulation_signal},
    "vp_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_059_capitulation_signal},
    "vp_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_060_capitulation_signal},
    "vp_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_061_capitulation_signal},
    "vp_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_062_capitulation_signal},
    "vp_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_063_capitulation_signal},
    "vp_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_064_capitulation_signal},
    "vp_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_065_capitulation_signal},
    "vp_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_066_capitulation_signal},
    "vp_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_067_capitulation_signal},
    "vp_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_068_capitulation_signal},
    "vp_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_069_capitulation_signal},
    "vp_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_070_capitulation_signal},
    "vp_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_071_capitulation_signal},
    "vp_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_072_capitulation_signal},
    "vp_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_073_capitulation_signal},
    "vp_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_074_capitulation_signal},
    "vp_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vp_075_capitulation_signal},
}
