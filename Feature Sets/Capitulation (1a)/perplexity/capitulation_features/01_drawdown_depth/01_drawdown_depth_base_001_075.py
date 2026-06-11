"""Generated capitulation features for 01_drawdown_depth: decline magnitude vs trailing highs.
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

def dd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DRAWDOWN_DEPTH_REGISTRY_001_075 = {
    "dd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_001_capitulation_signal},
    "dd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_002_capitulation_signal},
    "dd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_003_capitulation_signal},
    "dd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_004_capitulation_signal},
    "dd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_005_capitulation_signal},
    "dd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_006_capitulation_signal},
    "dd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_007_capitulation_signal},
    "dd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_008_capitulation_signal},
    "dd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_009_capitulation_signal},
    "dd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_010_capitulation_signal},
    "dd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_011_capitulation_signal},
    "dd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_012_capitulation_signal},
    "dd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_013_capitulation_signal},
    "dd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_014_capitulation_signal},
    "dd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_015_capitulation_signal},
    "dd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_016_capitulation_signal},
    "dd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_017_capitulation_signal},
    "dd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_018_capitulation_signal},
    "dd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_019_capitulation_signal},
    "dd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_020_capitulation_signal},
    "dd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_021_capitulation_signal},
    "dd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_022_capitulation_signal},
    "dd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_023_capitulation_signal},
    "dd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_024_capitulation_signal},
    "dd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_025_capitulation_signal},
    "dd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_026_capitulation_signal},
    "dd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_027_capitulation_signal},
    "dd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_028_capitulation_signal},
    "dd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_029_capitulation_signal},
    "dd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_030_capitulation_signal},
    "dd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_031_capitulation_signal},
    "dd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_032_capitulation_signal},
    "dd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_033_capitulation_signal},
    "dd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_034_capitulation_signal},
    "dd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_035_capitulation_signal},
    "dd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_036_capitulation_signal},
    "dd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_037_capitulation_signal},
    "dd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_038_capitulation_signal},
    "dd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_039_capitulation_signal},
    "dd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_040_capitulation_signal},
    "dd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_041_capitulation_signal},
    "dd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_042_capitulation_signal},
    "dd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_043_capitulation_signal},
    "dd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_044_capitulation_signal},
    "dd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_045_capitulation_signal},
    "dd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_046_capitulation_signal},
    "dd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_047_capitulation_signal},
    "dd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_048_capitulation_signal},
    "dd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_049_capitulation_signal},
    "dd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_050_capitulation_signal},
    "dd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_051_capitulation_signal},
    "dd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_052_capitulation_signal},
    "dd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_053_capitulation_signal},
    "dd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_054_capitulation_signal},
    "dd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_055_capitulation_signal},
    "dd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_056_capitulation_signal},
    "dd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_057_capitulation_signal},
    "dd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_058_capitulation_signal},
    "dd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_059_capitulation_signal},
    "dd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_060_capitulation_signal},
    "dd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_061_capitulation_signal},
    "dd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_062_capitulation_signal},
    "dd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_063_capitulation_signal},
    "dd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_064_capitulation_signal},
    "dd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_065_capitulation_signal},
    "dd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_066_capitulation_signal},
    "dd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_067_capitulation_signal},
    "dd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_068_capitulation_signal},
    "dd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_069_capitulation_signal},
    "dd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_070_capitulation_signal},
    "dd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_071_capitulation_signal},
    "dd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_072_capitulation_signal},
    "dd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_073_capitulation_signal},
    "dd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_074_capitulation_signal},
    "dd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dd_075_capitulation_signal},
}
