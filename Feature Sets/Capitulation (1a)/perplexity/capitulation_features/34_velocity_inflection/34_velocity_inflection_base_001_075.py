"""Generated capitulation features for 34_velocity_inflection: sign change in price velocity.
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

def vif_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vif_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vif_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vif_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vif_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vif_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vif_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vif_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vif_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vif_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vif_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vif_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vif_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vif_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vif_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vif_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vif_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vif_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vif_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vif_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vif_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vif_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vif_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vif_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vif_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vif_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vif_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vif_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vif_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vif_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vif_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vif_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vif_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vif_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vif_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vif_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vif_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vif_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vif_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vif_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vif_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vif_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vif_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vif_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vif_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vif_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vif_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vif_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vif_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vif_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vif_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vif_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vif_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vif_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vif_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vif_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vif_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vif_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vif_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vif_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vif_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vif_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VELOCITY_INFLECTION_REGISTRY_001_075 = {
    "vif_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_001_capitulation_signal},
    "vif_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_002_capitulation_signal},
    "vif_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_003_capitulation_signal},
    "vif_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_004_capitulation_signal},
    "vif_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_005_capitulation_signal},
    "vif_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_006_capitulation_signal},
    "vif_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_007_capitulation_signal},
    "vif_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_008_capitulation_signal},
    "vif_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_009_capitulation_signal},
    "vif_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_010_capitulation_signal},
    "vif_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_011_capitulation_signal},
    "vif_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_012_capitulation_signal},
    "vif_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_013_capitulation_signal},
    "vif_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_014_capitulation_signal},
    "vif_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_015_capitulation_signal},
    "vif_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_016_capitulation_signal},
    "vif_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_017_capitulation_signal},
    "vif_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_018_capitulation_signal},
    "vif_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_019_capitulation_signal},
    "vif_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_020_capitulation_signal},
    "vif_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_021_capitulation_signal},
    "vif_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_022_capitulation_signal},
    "vif_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_023_capitulation_signal},
    "vif_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_024_capitulation_signal},
    "vif_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_025_capitulation_signal},
    "vif_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_026_capitulation_signal},
    "vif_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_027_capitulation_signal},
    "vif_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_028_capitulation_signal},
    "vif_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_029_capitulation_signal},
    "vif_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_030_capitulation_signal},
    "vif_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_031_capitulation_signal},
    "vif_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_032_capitulation_signal},
    "vif_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_033_capitulation_signal},
    "vif_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_034_capitulation_signal},
    "vif_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_035_capitulation_signal},
    "vif_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_036_capitulation_signal},
    "vif_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_037_capitulation_signal},
    "vif_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_038_capitulation_signal},
    "vif_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_039_capitulation_signal},
    "vif_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_040_capitulation_signal},
    "vif_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_041_capitulation_signal},
    "vif_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_042_capitulation_signal},
    "vif_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_043_capitulation_signal},
    "vif_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_044_capitulation_signal},
    "vif_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_045_capitulation_signal},
    "vif_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_046_capitulation_signal},
    "vif_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_047_capitulation_signal},
    "vif_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_048_capitulation_signal},
    "vif_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_049_capitulation_signal},
    "vif_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_050_capitulation_signal},
    "vif_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_051_capitulation_signal},
    "vif_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_052_capitulation_signal},
    "vif_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_053_capitulation_signal},
    "vif_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_054_capitulation_signal},
    "vif_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_055_capitulation_signal},
    "vif_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_056_capitulation_signal},
    "vif_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_057_capitulation_signal},
    "vif_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_058_capitulation_signal},
    "vif_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_059_capitulation_signal},
    "vif_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_060_capitulation_signal},
    "vif_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_061_capitulation_signal},
    "vif_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_062_capitulation_signal},
    "vif_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_063_capitulation_signal},
    "vif_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_064_capitulation_signal},
    "vif_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_065_capitulation_signal},
    "vif_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_066_capitulation_signal},
    "vif_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_067_capitulation_signal},
    "vif_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_068_capitulation_signal},
    "vif_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_069_capitulation_signal},
    "vif_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_070_capitulation_signal},
    "vif_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_071_capitulation_signal},
    "vif_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_072_capitulation_signal},
    "vif_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_073_capitulation_signal},
    "vif_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_074_capitulation_signal},
    "vif_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vif_075_capitulation_signal},
}
