"""Generated capitulation features for 47_gap_down_clustering: clustered down gaps.
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

def gdc_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def gdc_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def gdc_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def gdc_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def gdc_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def gdc_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def gdc_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def gdc_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def gdc_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def gdc_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def gdc_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def gdc_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def gdc_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def gdc_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def gdc_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def gdc_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def gdc_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def gdc_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def gdc_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def gdc_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def gdc_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def gdc_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def gdc_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def gdc_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def gdc_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def gdc_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def gdc_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def gdc_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def gdc_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def gdc_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def gdc_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def gdc_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def gdc_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def gdc_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def gdc_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def gdc_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def gdc_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def gdc_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def gdc_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def gdc_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def gdc_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def gdc_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def gdc_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def gdc_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def gdc_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def gdc_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def gdc_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def gdc_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def gdc_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def gdc_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def gdc_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def gdc_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def gdc_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def gdc_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def gdc_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def gdc_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def gdc_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def gdc_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def gdc_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def gdc_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def gdc_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

GAP_DOWN_CLUSTERING_REGISTRY_001_075 = {
    "gdc_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_001_capitulation_signal},
    "gdc_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_002_capitulation_signal},
    "gdc_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_003_capitulation_signal},
    "gdc_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_004_capitulation_signal},
    "gdc_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_005_capitulation_signal},
    "gdc_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_006_capitulation_signal},
    "gdc_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_007_capitulation_signal},
    "gdc_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_008_capitulation_signal},
    "gdc_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_009_capitulation_signal},
    "gdc_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_010_capitulation_signal},
    "gdc_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_011_capitulation_signal},
    "gdc_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_012_capitulation_signal},
    "gdc_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_013_capitulation_signal},
    "gdc_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_014_capitulation_signal},
    "gdc_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_015_capitulation_signal},
    "gdc_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_016_capitulation_signal},
    "gdc_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_017_capitulation_signal},
    "gdc_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_018_capitulation_signal},
    "gdc_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_019_capitulation_signal},
    "gdc_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_020_capitulation_signal},
    "gdc_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_021_capitulation_signal},
    "gdc_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_022_capitulation_signal},
    "gdc_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_023_capitulation_signal},
    "gdc_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_024_capitulation_signal},
    "gdc_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_025_capitulation_signal},
    "gdc_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_026_capitulation_signal},
    "gdc_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_027_capitulation_signal},
    "gdc_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_028_capitulation_signal},
    "gdc_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_029_capitulation_signal},
    "gdc_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_030_capitulation_signal},
    "gdc_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_031_capitulation_signal},
    "gdc_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_032_capitulation_signal},
    "gdc_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_033_capitulation_signal},
    "gdc_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_034_capitulation_signal},
    "gdc_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_035_capitulation_signal},
    "gdc_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_036_capitulation_signal},
    "gdc_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_037_capitulation_signal},
    "gdc_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_038_capitulation_signal},
    "gdc_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_039_capitulation_signal},
    "gdc_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_040_capitulation_signal},
    "gdc_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_041_capitulation_signal},
    "gdc_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_042_capitulation_signal},
    "gdc_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_043_capitulation_signal},
    "gdc_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_044_capitulation_signal},
    "gdc_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_045_capitulation_signal},
    "gdc_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_046_capitulation_signal},
    "gdc_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_047_capitulation_signal},
    "gdc_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_048_capitulation_signal},
    "gdc_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_049_capitulation_signal},
    "gdc_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_050_capitulation_signal},
    "gdc_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_051_capitulation_signal},
    "gdc_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_052_capitulation_signal},
    "gdc_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_053_capitulation_signal},
    "gdc_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_054_capitulation_signal},
    "gdc_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_055_capitulation_signal},
    "gdc_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_056_capitulation_signal},
    "gdc_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_057_capitulation_signal},
    "gdc_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_058_capitulation_signal},
    "gdc_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_059_capitulation_signal},
    "gdc_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_060_capitulation_signal},
    "gdc_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_061_capitulation_signal},
    "gdc_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_062_capitulation_signal},
    "gdc_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_063_capitulation_signal},
    "gdc_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_064_capitulation_signal},
    "gdc_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_065_capitulation_signal},
    "gdc_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_066_capitulation_signal},
    "gdc_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_067_capitulation_signal},
    "gdc_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_068_capitulation_signal},
    "gdc_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_069_capitulation_signal},
    "gdc_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_070_capitulation_signal},
    "gdc_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_071_capitulation_signal},
    "gdc_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_072_capitulation_signal},
    "gdc_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_073_capitulation_signal},
    "gdc_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_074_capitulation_signal},
    "gdc_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": gdc_075_capitulation_signal},
}
