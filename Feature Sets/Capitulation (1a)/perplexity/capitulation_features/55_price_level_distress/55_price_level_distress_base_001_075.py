"""Generated capitulation features for 55_price_level_distress: sub-dollar/five-dollar distress.
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

def pld_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def pld_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def pld_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def pld_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def pld_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def pld_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def pld_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def pld_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def pld_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def pld_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def pld_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def pld_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def pld_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def pld_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def pld_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def pld_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def pld_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def pld_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def pld_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def pld_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def pld_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def pld_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def pld_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def pld_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def pld_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def pld_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def pld_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def pld_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def pld_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def pld_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def pld_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def pld_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def pld_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def pld_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def pld_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def pld_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def pld_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def pld_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def pld_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def pld_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def pld_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def pld_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def pld_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def pld_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def pld_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def pld_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def pld_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def pld_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pld_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def pld_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def pld_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def pld_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def pld_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def pld_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def pld_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def pld_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pld_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def pld_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pld_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def pld_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def pld_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def pld_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

PRICE_LEVEL_DISTRESS_REGISTRY_001_075 = {
    "pld_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_001_capitulation_signal},
    "pld_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_002_capitulation_signal},
    "pld_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_003_capitulation_signal},
    "pld_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_004_capitulation_signal},
    "pld_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_005_capitulation_signal},
    "pld_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_006_capitulation_signal},
    "pld_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_007_capitulation_signal},
    "pld_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_008_capitulation_signal},
    "pld_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_009_capitulation_signal},
    "pld_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_010_capitulation_signal},
    "pld_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_011_capitulation_signal},
    "pld_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_012_capitulation_signal},
    "pld_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_013_capitulation_signal},
    "pld_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_014_capitulation_signal},
    "pld_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_015_capitulation_signal},
    "pld_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_016_capitulation_signal},
    "pld_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_017_capitulation_signal},
    "pld_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_018_capitulation_signal},
    "pld_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_019_capitulation_signal},
    "pld_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_020_capitulation_signal},
    "pld_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_021_capitulation_signal},
    "pld_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_022_capitulation_signal},
    "pld_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_023_capitulation_signal},
    "pld_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_024_capitulation_signal},
    "pld_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_025_capitulation_signal},
    "pld_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_026_capitulation_signal},
    "pld_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_027_capitulation_signal},
    "pld_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_028_capitulation_signal},
    "pld_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_029_capitulation_signal},
    "pld_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_030_capitulation_signal},
    "pld_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_031_capitulation_signal},
    "pld_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_032_capitulation_signal},
    "pld_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_033_capitulation_signal},
    "pld_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_034_capitulation_signal},
    "pld_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_035_capitulation_signal},
    "pld_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_036_capitulation_signal},
    "pld_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_037_capitulation_signal},
    "pld_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_038_capitulation_signal},
    "pld_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_039_capitulation_signal},
    "pld_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_040_capitulation_signal},
    "pld_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_041_capitulation_signal},
    "pld_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_042_capitulation_signal},
    "pld_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_043_capitulation_signal},
    "pld_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_044_capitulation_signal},
    "pld_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_045_capitulation_signal},
    "pld_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_046_capitulation_signal},
    "pld_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_047_capitulation_signal},
    "pld_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_048_capitulation_signal},
    "pld_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_049_capitulation_signal},
    "pld_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_050_capitulation_signal},
    "pld_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_051_capitulation_signal},
    "pld_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_052_capitulation_signal},
    "pld_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_053_capitulation_signal},
    "pld_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_054_capitulation_signal},
    "pld_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_055_capitulation_signal},
    "pld_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_056_capitulation_signal},
    "pld_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_057_capitulation_signal},
    "pld_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_058_capitulation_signal},
    "pld_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_059_capitulation_signal},
    "pld_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_060_capitulation_signal},
    "pld_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_061_capitulation_signal},
    "pld_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_062_capitulation_signal},
    "pld_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_063_capitulation_signal},
    "pld_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_064_capitulation_signal},
    "pld_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_065_capitulation_signal},
    "pld_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_066_capitulation_signal},
    "pld_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_067_capitulation_signal},
    "pld_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_068_capitulation_signal},
    "pld_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_069_capitulation_signal},
    "pld_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_070_capitulation_signal},
    "pld_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_071_capitulation_signal},
    "pld_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_072_capitulation_signal},
    "pld_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_073_capitulation_signal},
    "pld_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_074_capitulation_signal},
    "pld_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pld_075_capitulation_signal},
}
