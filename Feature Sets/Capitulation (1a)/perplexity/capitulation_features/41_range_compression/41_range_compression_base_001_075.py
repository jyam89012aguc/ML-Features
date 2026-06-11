"""Generated capitulation features for 41_range_compression: range collapse after expansion.
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

def rcp_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def rcp_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def rcp_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def rcp_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def rcp_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rcp_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def rcp_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def rcp_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def rcp_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def rcp_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def rcp_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def rcp_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def rcp_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def rcp_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def rcp_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def rcp_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def rcp_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def rcp_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def rcp_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rcp_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def rcp_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def rcp_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def rcp_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def rcp_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def rcp_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def rcp_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def rcp_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def rcp_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def rcp_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def rcp_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def rcp_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def rcp_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def rcp_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rcp_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def rcp_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def rcp_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def rcp_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def rcp_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def rcp_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def rcp_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def rcp_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def rcp_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def rcp_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def rcp_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def rcp_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def rcp_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def rcp_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rcp_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rcp_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def rcp_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def rcp_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def rcp_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def rcp_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def rcp_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def rcp_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rcp_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def rcp_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rcp_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def rcp_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def rcp_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def rcp_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

RANGE_COMPRESSION_REGISTRY_001_075 = {
    "rcp_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_001_capitulation_signal},
    "rcp_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_002_capitulation_signal},
    "rcp_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_003_capitulation_signal},
    "rcp_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_004_capitulation_signal},
    "rcp_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_005_capitulation_signal},
    "rcp_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_006_capitulation_signal},
    "rcp_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_007_capitulation_signal},
    "rcp_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_008_capitulation_signal},
    "rcp_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_009_capitulation_signal},
    "rcp_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_010_capitulation_signal},
    "rcp_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_011_capitulation_signal},
    "rcp_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_012_capitulation_signal},
    "rcp_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_013_capitulation_signal},
    "rcp_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_014_capitulation_signal},
    "rcp_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_015_capitulation_signal},
    "rcp_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_016_capitulation_signal},
    "rcp_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_017_capitulation_signal},
    "rcp_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_018_capitulation_signal},
    "rcp_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_019_capitulation_signal},
    "rcp_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_020_capitulation_signal},
    "rcp_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_021_capitulation_signal},
    "rcp_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_022_capitulation_signal},
    "rcp_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_023_capitulation_signal},
    "rcp_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_024_capitulation_signal},
    "rcp_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_025_capitulation_signal},
    "rcp_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_026_capitulation_signal},
    "rcp_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_027_capitulation_signal},
    "rcp_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_028_capitulation_signal},
    "rcp_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_029_capitulation_signal},
    "rcp_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_030_capitulation_signal},
    "rcp_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_031_capitulation_signal},
    "rcp_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_032_capitulation_signal},
    "rcp_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_033_capitulation_signal},
    "rcp_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_034_capitulation_signal},
    "rcp_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_035_capitulation_signal},
    "rcp_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_036_capitulation_signal},
    "rcp_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_037_capitulation_signal},
    "rcp_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_038_capitulation_signal},
    "rcp_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_039_capitulation_signal},
    "rcp_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_040_capitulation_signal},
    "rcp_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_041_capitulation_signal},
    "rcp_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_042_capitulation_signal},
    "rcp_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_043_capitulation_signal},
    "rcp_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_044_capitulation_signal},
    "rcp_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_045_capitulation_signal},
    "rcp_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_046_capitulation_signal},
    "rcp_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_047_capitulation_signal},
    "rcp_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_048_capitulation_signal},
    "rcp_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_049_capitulation_signal},
    "rcp_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_050_capitulation_signal},
    "rcp_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_051_capitulation_signal},
    "rcp_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_052_capitulation_signal},
    "rcp_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_053_capitulation_signal},
    "rcp_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_054_capitulation_signal},
    "rcp_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_055_capitulation_signal},
    "rcp_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_056_capitulation_signal},
    "rcp_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_057_capitulation_signal},
    "rcp_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_058_capitulation_signal},
    "rcp_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_059_capitulation_signal},
    "rcp_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_060_capitulation_signal},
    "rcp_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_061_capitulation_signal},
    "rcp_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_062_capitulation_signal},
    "rcp_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_063_capitulation_signal},
    "rcp_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_064_capitulation_signal},
    "rcp_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_065_capitulation_signal},
    "rcp_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_066_capitulation_signal},
    "rcp_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_067_capitulation_signal},
    "rcp_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_068_capitulation_signal},
    "rcp_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_069_capitulation_signal},
    "rcp_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_070_capitulation_signal},
    "rcp_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_071_capitulation_signal},
    "rcp_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_072_capitulation_signal},
    "rcp_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_073_capitulation_signal},
    "rcp_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_074_capitulation_signal},
    "rcp_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rcp_075_capitulation_signal},
}
