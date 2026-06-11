"""Generated capitulation features for 18_volume_dryup: volume collapse/exhaustion.
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

def vdry_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vdry_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vdry_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vdry_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vdry_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vdry_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vdry_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vdry_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vdry_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vdry_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vdry_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vdry_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vdry_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vdry_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vdry_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vdry_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vdry_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vdry_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vdry_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vdry_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vdry_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vdry_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vdry_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vdry_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vdry_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vdry_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vdry_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vdry_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vdry_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vdry_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vdry_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vdry_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vdry_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vdry_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vdry_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vdry_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vdry_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vdry_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vdry_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vdry_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vdry_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vdry_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vdry_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vdry_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vdry_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vdry_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vdry_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vdry_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vdry_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vdry_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vdry_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vdry_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vdry_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vdry_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vdry_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vdry_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vdry_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vdry_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vdry_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vdry_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vdry_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_DRYUP_REGISTRY_001_075 = {
    "vdry_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_001_capitulation_signal},
    "vdry_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_002_capitulation_signal},
    "vdry_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_003_capitulation_signal},
    "vdry_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_004_capitulation_signal},
    "vdry_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_005_capitulation_signal},
    "vdry_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_006_capitulation_signal},
    "vdry_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_007_capitulation_signal},
    "vdry_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_008_capitulation_signal},
    "vdry_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_009_capitulation_signal},
    "vdry_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_010_capitulation_signal},
    "vdry_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_011_capitulation_signal},
    "vdry_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_012_capitulation_signal},
    "vdry_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_013_capitulation_signal},
    "vdry_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_014_capitulation_signal},
    "vdry_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_015_capitulation_signal},
    "vdry_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_016_capitulation_signal},
    "vdry_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_017_capitulation_signal},
    "vdry_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_018_capitulation_signal},
    "vdry_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_019_capitulation_signal},
    "vdry_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_020_capitulation_signal},
    "vdry_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_021_capitulation_signal},
    "vdry_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_022_capitulation_signal},
    "vdry_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_023_capitulation_signal},
    "vdry_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_024_capitulation_signal},
    "vdry_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_025_capitulation_signal},
    "vdry_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_026_capitulation_signal},
    "vdry_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_027_capitulation_signal},
    "vdry_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_028_capitulation_signal},
    "vdry_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_029_capitulation_signal},
    "vdry_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_030_capitulation_signal},
    "vdry_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_031_capitulation_signal},
    "vdry_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_032_capitulation_signal},
    "vdry_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_033_capitulation_signal},
    "vdry_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_034_capitulation_signal},
    "vdry_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_035_capitulation_signal},
    "vdry_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_036_capitulation_signal},
    "vdry_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_037_capitulation_signal},
    "vdry_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_038_capitulation_signal},
    "vdry_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_039_capitulation_signal},
    "vdry_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_040_capitulation_signal},
    "vdry_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_041_capitulation_signal},
    "vdry_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_042_capitulation_signal},
    "vdry_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_043_capitulation_signal},
    "vdry_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_044_capitulation_signal},
    "vdry_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_045_capitulation_signal},
    "vdry_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_046_capitulation_signal},
    "vdry_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_047_capitulation_signal},
    "vdry_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_048_capitulation_signal},
    "vdry_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_049_capitulation_signal},
    "vdry_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_050_capitulation_signal},
    "vdry_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_051_capitulation_signal},
    "vdry_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_052_capitulation_signal},
    "vdry_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_053_capitulation_signal},
    "vdry_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_054_capitulation_signal},
    "vdry_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_055_capitulation_signal},
    "vdry_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_056_capitulation_signal},
    "vdry_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_057_capitulation_signal},
    "vdry_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_058_capitulation_signal},
    "vdry_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_059_capitulation_signal},
    "vdry_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_060_capitulation_signal},
    "vdry_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_061_capitulation_signal},
    "vdry_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_062_capitulation_signal},
    "vdry_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_063_capitulation_signal},
    "vdry_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_064_capitulation_signal},
    "vdry_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_065_capitulation_signal},
    "vdry_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_066_capitulation_signal},
    "vdry_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_067_capitulation_signal},
    "vdry_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_068_capitulation_signal},
    "vdry_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_069_capitulation_signal},
    "vdry_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_070_capitulation_signal},
    "vdry_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_071_capitulation_signal},
    "vdry_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_072_capitulation_signal},
    "vdry_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_073_capitulation_signal},
    "vdry_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_074_capitulation_signal},
    "vdry_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vdry_075_capitulation_signal},
}
