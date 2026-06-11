"""Generated capitulation features for 19_volume_trend: directional drift in volume.
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

def vtr_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vtr_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vtr_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vtr_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vtr_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vtr_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vtr_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vtr_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vtr_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vtr_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vtr_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vtr_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vtr_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vtr_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vtr_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vtr_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vtr_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vtr_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vtr_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vtr_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vtr_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vtr_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vtr_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vtr_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vtr_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vtr_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vtr_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vtr_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vtr_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vtr_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vtr_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vtr_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vtr_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vtr_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vtr_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vtr_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vtr_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vtr_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vtr_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vtr_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vtr_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vtr_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vtr_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vtr_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vtr_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vtr_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vtr_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vtr_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vtr_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vtr_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vtr_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vtr_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vtr_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vtr_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vtr_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vtr_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vtr_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vtr_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vtr_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vtr_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vtr_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_TREND_REGISTRY_001_075 = {
    "vtr_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_001_capitulation_signal},
    "vtr_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_002_capitulation_signal},
    "vtr_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_003_capitulation_signal},
    "vtr_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_004_capitulation_signal},
    "vtr_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_005_capitulation_signal},
    "vtr_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_006_capitulation_signal},
    "vtr_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_007_capitulation_signal},
    "vtr_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_008_capitulation_signal},
    "vtr_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_009_capitulation_signal},
    "vtr_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_010_capitulation_signal},
    "vtr_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_011_capitulation_signal},
    "vtr_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_012_capitulation_signal},
    "vtr_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_013_capitulation_signal},
    "vtr_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_014_capitulation_signal},
    "vtr_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_015_capitulation_signal},
    "vtr_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_016_capitulation_signal},
    "vtr_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_017_capitulation_signal},
    "vtr_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_018_capitulation_signal},
    "vtr_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_019_capitulation_signal},
    "vtr_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_020_capitulation_signal},
    "vtr_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_021_capitulation_signal},
    "vtr_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_022_capitulation_signal},
    "vtr_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_023_capitulation_signal},
    "vtr_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_024_capitulation_signal},
    "vtr_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_025_capitulation_signal},
    "vtr_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_026_capitulation_signal},
    "vtr_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_027_capitulation_signal},
    "vtr_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_028_capitulation_signal},
    "vtr_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_029_capitulation_signal},
    "vtr_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_030_capitulation_signal},
    "vtr_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_031_capitulation_signal},
    "vtr_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_032_capitulation_signal},
    "vtr_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_033_capitulation_signal},
    "vtr_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_034_capitulation_signal},
    "vtr_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_035_capitulation_signal},
    "vtr_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_036_capitulation_signal},
    "vtr_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_037_capitulation_signal},
    "vtr_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_038_capitulation_signal},
    "vtr_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_039_capitulation_signal},
    "vtr_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_040_capitulation_signal},
    "vtr_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_041_capitulation_signal},
    "vtr_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_042_capitulation_signal},
    "vtr_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_043_capitulation_signal},
    "vtr_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_044_capitulation_signal},
    "vtr_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_045_capitulation_signal},
    "vtr_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_046_capitulation_signal},
    "vtr_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_047_capitulation_signal},
    "vtr_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_048_capitulation_signal},
    "vtr_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_049_capitulation_signal},
    "vtr_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_050_capitulation_signal},
    "vtr_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_051_capitulation_signal},
    "vtr_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_052_capitulation_signal},
    "vtr_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_053_capitulation_signal},
    "vtr_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_054_capitulation_signal},
    "vtr_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_055_capitulation_signal},
    "vtr_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_056_capitulation_signal},
    "vtr_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_057_capitulation_signal},
    "vtr_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_058_capitulation_signal},
    "vtr_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_059_capitulation_signal},
    "vtr_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_060_capitulation_signal},
    "vtr_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_061_capitulation_signal},
    "vtr_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_062_capitulation_signal},
    "vtr_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_063_capitulation_signal},
    "vtr_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_064_capitulation_signal},
    "vtr_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_065_capitulation_signal},
    "vtr_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_066_capitulation_signal},
    "vtr_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_067_capitulation_signal},
    "vtr_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_068_capitulation_signal},
    "vtr_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_069_capitulation_signal},
    "vtr_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_070_capitulation_signal},
    "vtr_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_071_capitulation_signal},
    "vtr_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_072_capitulation_signal},
    "vtr_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_073_capitulation_signal},
    "vtr_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_074_capitulation_signal},
    "vtr_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vtr_075_capitulation_signal},
}
