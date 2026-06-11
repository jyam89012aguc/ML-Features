"""Generated capitulation features for 17_volume_climax: single-day extreme volume events.
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

def vcx_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vcx_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vcx_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vcx_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vcx_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vcx_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vcx_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vcx_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vcx_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vcx_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vcx_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vcx_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vcx_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vcx_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vcx_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vcx_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vcx_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vcx_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vcx_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vcx_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vcx_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vcx_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vcx_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vcx_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vcx_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vcx_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vcx_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vcx_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vcx_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vcx_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vcx_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vcx_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vcx_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vcx_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vcx_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vcx_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vcx_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vcx_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vcx_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vcx_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vcx_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vcx_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vcx_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vcx_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vcx_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vcx_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vcx_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vcx_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vcx_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vcx_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vcx_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vcx_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vcx_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vcx_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vcx_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vcx_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vcx_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vcx_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vcx_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vcx_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vcx_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_CLIMAX_REGISTRY_001_075 = {
    "vcx_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_001_capitulation_signal},
    "vcx_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_002_capitulation_signal},
    "vcx_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_003_capitulation_signal},
    "vcx_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_004_capitulation_signal},
    "vcx_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_005_capitulation_signal},
    "vcx_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_006_capitulation_signal},
    "vcx_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_007_capitulation_signal},
    "vcx_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_008_capitulation_signal},
    "vcx_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_009_capitulation_signal},
    "vcx_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_010_capitulation_signal},
    "vcx_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_011_capitulation_signal},
    "vcx_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_012_capitulation_signal},
    "vcx_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_013_capitulation_signal},
    "vcx_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_014_capitulation_signal},
    "vcx_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_015_capitulation_signal},
    "vcx_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_016_capitulation_signal},
    "vcx_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_017_capitulation_signal},
    "vcx_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_018_capitulation_signal},
    "vcx_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_019_capitulation_signal},
    "vcx_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_020_capitulation_signal},
    "vcx_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_021_capitulation_signal},
    "vcx_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_022_capitulation_signal},
    "vcx_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_023_capitulation_signal},
    "vcx_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_024_capitulation_signal},
    "vcx_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_025_capitulation_signal},
    "vcx_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_026_capitulation_signal},
    "vcx_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_027_capitulation_signal},
    "vcx_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_028_capitulation_signal},
    "vcx_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_029_capitulation_signal},
    "vcx_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_030_capitulation_signal},
    "vcx_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_031_capitulation_signal},
    "vcx_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_032_capitulation_signal},
    "vcx_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_033_capitulation_signal},
    "vcx_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_034_capitulation_signal},
    "vcx_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_035_capitulation_signal},
    "vcx_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_036_capitulation_signal},
    "vcx_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_037_capitulation_signal},
    "vcx_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_038_capitulation_signal},
    "vcx_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_039_capitulation_signal},
    "vcx_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_040_capitulation_signal},
    "vcx_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_041_capitulation_signal},
    "vcx_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_042_capitulation_signal},
    "vcx_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_043_capitulation_signal},
    "vcx_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_044_capitulation_signal},
    "vcx_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_045_capitulation_signal},
    "vcx_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_046_capitulation_signal},
    "vcx_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_047_capitulation_signal},
    "vcx_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_048_capitulation_signal},
    "vcx_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_049_capitulation_signal},
    "vcx_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_050_capitulation_signal},
    "vcx_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_051_capitulation_signal},
    "vcx_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_052_capitulation_signal},
    "vcx_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_053_capitulation_signal},
    "vcx_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_054_capitulation_signal},
    "vcx_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_055_capitulation_signal},
    "vcx_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_056_capitulation_signal},
    "vcx_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_057_capitulation_signal},
    "vcx_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_058_capitulation_signal},
    "vcx_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_059_capitulation_signal},
    "vcx_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_060_capitulation_signal},
    "vcx_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_061_capitulation_signal},
    "vcx_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_062_capitulation_signal},
    "vcx_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_063_capitulation_signal},
    "vcx_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_064_capitulation_signal},
    "vcx_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_065_capitulation_signal},
    "vcx_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_066_capitulation_signal},
    "vcx_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_067_capitulation_signal},
    "vcx_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_068_capitulation_signal},
    "vcx_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_069_capitulation_signal},
    "vcx_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_070_capitulation_signal},
    "vcx_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_071_capitulation_signal},
    "vcx_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_072_capitulation_signal},
    "vcx_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_073_capitulation_signal},
    "vcx_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_074_capitulation_signal},
    "vcx_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcx_075_capitulation_signal},
}
