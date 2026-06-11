"""Generated capitulation features for 33_trend_breakdown: moving-average trend loss.
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

def tbd_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def tbd_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def tbd_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def tbd_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def tbd_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tbd_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def tbd_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def tbd_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def tbd_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def tbd_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def tbd_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def tbd_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def tbd_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def tbd_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def tbd_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def tbd_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def tbd_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def tbd_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def tbd_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tbd_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def tbd_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def tbd_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def tbd_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def tbd_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def tbd_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def tbd_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def tbd_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def tbd_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def tbd_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def tbd_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def tbd_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def tbd_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def tbd_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tbd_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def tbd_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def tbd_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def tbd_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def tbd_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def tbd_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def tbd_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def tbd_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def tbd_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def tbd_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def tbd_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def tbd_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def tbd_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def tbd_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tbd_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def tbd_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def tbd_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def tbd_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def tbd_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def tbd_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def tbd_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def tbd_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tbd_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def tbd_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tbd_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def tbd_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def tbd_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def tbd_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

TREND_BREAKDOWN_REGISTRY_001_075 = {
    "tbd_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_001_capitulation_signal},
    "tbd_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_002_capitulation_signal},
    "tbd_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_003_capitulation_signal},
    "tbd_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_004_capitulation_signal},
    "tbd_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_005_capitulation_signal},
    "tbd_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_006_capitulation_signal},
    "tbd_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_007_capitulation_signal},
    "tbd_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_008_capitulation_signal},
    "tbd_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_009_capitulation_signal},
    "tbd_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_010_capitulation_signal},
    "tbd_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_011_capitulation_signal},
    "tbd_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_012_capitulation_signal},
    "tbd_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_013_capitulation_signal},
    "tbd_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_014_capitulation_signal},
    "tbd_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_015_capitulation_signal},
    "tbd_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_016_capitulation_signal},
    "tbd_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_017_capitulation_signal},
    "tbd_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_018_capitulation_signal},
    "tbd_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_019_capitulation_signal},
    "tbd_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_020_capitulation_signal},
    "tbd_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_021_capitulation_signal},
    "tbd_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_022_capitulation_signal},
    "tbd_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_023_capitulation_signal},
    "tbd_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_024_capitulation_signal},
    "tbd_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_025_capitulation_signal},
    "tbd_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_026_capitulation_signal},
    "tbd_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_027_capitulation_signal},
    "tbd_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_028_capitulation_signal},
    "tbd_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_029_capitulation_signal},
    "tbd_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_030_capitulation_signal},
    "tbd_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_031_capitulation_signal},
    "tbd_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_032_capitulation_signal},
    "tbd_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_033_capitulation_signal},
    "tbd_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_034_capitulation_signal},
    "tbd_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_035_capitulation_signal},
    "tbd_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_036_capitulation_signal},
    "tbd_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_037_capitulation_signal},
    "tbd_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_038_capitulation_signal},
    "tbd_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_039_capitulation_signal},
    "tbd_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_040_capitulation_signal},
    "tbd_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_041_capitulation_signal},
    "tbd_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_042_capitulation_signal},
    "tbd_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_043_capitulation_signal},
    "tbd_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_044_capitulation_signal},
    "tbd_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_045_capitulation_signal},
    "tbd_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_046_capitulation_signal},
    "tbd_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_047_capitulation_signal},
    "tbd_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_048_capitulation_signal},
    "tbd_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_049_capitulation_signal},
    "tbd_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_050_capitulation_signal},
    "tbd_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_051_capitulation_signal},
    "tbd_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_052_capitulation_signal},
    "tbd_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_053_capitulation_signal},
    "tbd_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_054_capitulation_signal},
    "tbd_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_055_capitulation_signal},
    "tbd_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_056_capitulation_signal},
    "tbd_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_057_capitulation_signal},
    "tbd_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_058_capitulation_signal},
    "tbd_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_059_capitulation_signal},
    "tbd_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_060_capitulation_signal},
    "tbd_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_061_capitulation_signal},
    "tbd_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_062_capitulation_signal},
    "tbd_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_063_capitulation_signal},
    "tbd_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_064_capitulation_signal},
    "tbd_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_065_capitulation_signal},
    "tbd_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_066_capitulation_signal},
    "tbd_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_067_capitulation_signal},
    "tbd_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_068_capitulation_signal},
    "tbd_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_069_capitulation_signal},
    "tbd_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_070_capitulation_signal},
    "tbd_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_071_capitulation_signal},
    "tbd_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_072_capitulation_signal},
    "tbd_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_073_capitulation_signal},
    "tbd_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_074_capitulation_signal},
    "tbd_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tbd_075_capitulation_signal},
}
