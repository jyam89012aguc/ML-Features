"""Generated capitulation features for 21_volume_concentration: share of volume in worst days.
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

def vcc_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vcc_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vcc_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vcc_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vcc_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vcc_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vcc_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vcc_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vcc_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vcc_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vcc_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vcc_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vcc_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vcc_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vcc_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vcc_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vcc_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vcc_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vcc_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vcc_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vcc_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vcc_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vcc_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vcc_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vcc_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vcc_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vcc_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vcc_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vcc_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vcc_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vcc_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vcc_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vcc_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vcc_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vcc_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vcc_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vcc_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vcc_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vcc_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vcc_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vcc_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vcc_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vcc_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vcc_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vcc_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vcc_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vcc_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vcc_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vcc_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcc_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vcc_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcc_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vcc_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vcc_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vcc_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_CONCENTRATION_REGISTRY_001_075 = {
    "vcc_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_001_capitulation_signal},
    "vcc_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_002_capitulation_signal},
    "vcc_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_003_capitulation_signal},
    "vcc_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_004_capitulation_signal},
    "vcc_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_005_capitulation_signal},
    "vcc_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_006_capitulation_signal},
    "vcc_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_007_capitulation_signal},
    "vcc_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_008_capitulation_signal},
    "vcc_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_009_capitulation_signal},
    "vcc_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_010_capitulation_signal},
    "vcc_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_011_capitulation_signal},
    "vcc_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_012_capitulation_signal},
    "vcc_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_013_capitulation_signal},
    "vcc_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_014_capitulation_signal},
    "vcc_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_015_capitulation_signal},
    "vcc_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_016_capitulation_signal},
    "vcc_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_017_capitulation_signal},
    "vcc_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_018_capitulation_signal},
    "vcc_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_019_capitulation_signal},
    "vcc_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_020_capitulation_signal},
    "vcc_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_021_capitulation_signal},
    "vcc_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_022_capitulation_signal},
    "vcc_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_023_capitulation_signal},
    "vcc_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_024_capitulation_signal},
    "vcc_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_025_capitulation_signal},
    "vcc_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_026_capitulation_signal},
    "vcc_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_027_capitulation_signal},
    "vcc_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_028_capitulation_signal},
    "vcc_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_029_capitulation_signal},
    "vcc_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_030_capitulation_signal},
    "vcc_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_031_capitulation_signal},
    "vcc_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_032_capitulation_signal},
    "vcc_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_033_capitulation_signal},
    "vcc_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_034_capitulation_signal},
    "vcc_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_035_capitulation_signal},
    "vcc_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_036_capitulation_signal},
    "vcc_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_037_capitulation_signal},
    "vcc_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_038_capitulation_signal},
    "vcc_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_039_capitulation_signal},
    "vcc_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_040_capitulation_signal},
    "vcc_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_041_capitulation_signal},
    "vcc_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_042_capitulation_signal},
    "vcc_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_043_capitulation_signal},
    "vcc_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_044_capitulation_signal},
    "vcc_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_045_capitulation_signal},
    "vcc_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_046_capitulation_signal},
    "vcc_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_047_capitulation_signal},
    "vcc_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_048_capitulation_signal},
    "vcc_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_049_capitulation_signal},
    "vcc_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_050_capitulation_signal},
    "vcc_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_051_capitulation_signal},
    "vcc_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_052_capitulation_signal},
    "vcc_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_053_capitulation_signal},
    "vcc_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_054_capitulation_signal},
    "vcc_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_055_capitulation_signal},
    "vcc_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_056_capitulation_signal},
    "vcc_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_057_capitulation_signal},
    "vcc_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_058_capitulation_signal},
    "vcc_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_059_capitulation_signal},
    "vcc_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_060_capitulation_signal},
    "vcc_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_061_capitulation_signal},
    "vcc_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_062_capitulation_signal},
    "vcc_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_063_capitulation_signal},
    "vcc_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_064_capitulation_signal},
    "vcc_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_065_capitulation_signal},
    "vcc_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_066_capitulation_signal},
    "vcc_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_067_capitulation_signal},
    "vcc_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_068_capitulation_signal},
    "vcc_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_069_capitulation_signal},
    "vcc_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_070_capitulation_signal},
    "vcc_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_071_capitulation_signal},
    "vcc_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_072_capitulation_signal},
    "vcc_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_073_capitulation_signal},
    "vcc_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_074_capitulation_signal},
    "vcc_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_075_capitulation_signal},
}
