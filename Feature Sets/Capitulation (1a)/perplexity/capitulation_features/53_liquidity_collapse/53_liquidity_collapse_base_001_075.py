"""Generated capitulation features for 53_liquidity_collapse: illiquidity spikes.
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

def lqc_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def lqc_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def lqc_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def lqc_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def lqc_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def lqc_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def lqc_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def lqc_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def lqc_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def lqc_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def lqc_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def lqc_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def lqc_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def lqc_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def lqc_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def lqc_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def lqc_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def lqc_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def lqc_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def lqc_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def lqc_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def lqc_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def lqc_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def lqc_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def lqc_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def lqc_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def lqc_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def lqc_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def lqc_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def lqc_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def lqc_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def lqc_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def lqc_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def lqc_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def lqc_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def lqc_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def lqc_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def lqc_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def lqc_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def lqc_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def lqc_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def lqc_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def lqc_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def lqc_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def lqc_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def lqc_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def lqc_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def lqc_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lqc_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def lqc_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def lqc_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def lqc_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def lqc_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def lqc_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def lqc_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def lqc_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def lqc_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def lqc_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def lqc_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def lqc_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def lqc_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

LIQUIDITY_COLLAPSE_REGISTRY_001_075 = {
    "lqc_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_001_capitulation_signal},
    "lqc_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_002_capitulation_signal},
    "lqc_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_003_capitulation_signal},
    "lqc_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_004_capitulation_signal},
    "lqc_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_005_capitulation_signal},
    "lqc_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_006_capitulation_signal},
    "lqc_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_007_capitulation_signal},
    "lqc_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_008_capitulation_signal},
    "lqc_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_009_capitulation_signal},
    "lqc_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_010_capitulation_signal},
    "lqc_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_011_capitulation_signal},
    "lqc_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_012_capitulation_signal},
    "lqc_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_013_capitulation_signal},
    "lqc_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_014_capitulation_signal},
    "lqc_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_015_capitulation_signal},
    "lqc_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_016_capitulation_signal},
    "lqc_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_017_capitulation_signal},
    "lqc_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_018_capitulation_signal},
    "lqc_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_019_capitulation_signal},
    "lqc_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_020_capitulation_signal},
    "lqc_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_021_capitulation_signal},
    "lqc_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_022_capitulation_signal},
    "lqc_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_023_capitulation_signal},
    "lqc_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_024_capitulation_signal},
    "lqc_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_025_capitulation_signal},
    "lqc_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_026_capitulation_signal},
    "lqc_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_027_capitulation_signal},
    "lqc_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_028_capitulation_signal},
    "lqc_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_029_capitulation_signal},
    "lqc_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_030_capitulation_signal},
    "lqc_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_031_capitulation_signal},
    "lqc_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_032_capitulation_signal},
    "lqc_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_033_capitulation_signal},
    "lqc_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_034_capitulation_signal},
    "lqc_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_035_capitulation_signal},
    "lqc_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_036_capitulation_signal},
    "lqc_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_037_capitulation_signal},
    "lqc_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_038_capitulation_signal},
    "lqc_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_039_capitulation_signal},
    "lqc_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_040_capitulation_signal},
    "lqc_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_041_capitulation_signal},
    "lqc_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_042_capitulation_signal},
    "lqc_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_043_capitulation_signal},
    "lqc_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_044_capitulation_signal},
    "lqc_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_045_capitulation_signal},
    "lqc_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_046_capitulation_signal},
    "lqc_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_047_capitulation_signal},
    "lqc_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_048_capitulation_signal},
    "lqc_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_049_capitulation_signal},
    "lqc_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_050_capitulation_signal},
    "lqc_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_051_capitulation_signal},
    "lqc_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_052_capitulation_signal},
    "lqc_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_053_capitulation_signal},
    "lqc_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_054_capitulation_signal},
    "lqc_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_055_capitulation_signal},
    "lqc_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_056_capitulation_signal},
    "lqc_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_057_capitulation_signal},
    "lqc_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_058_capitulation_signal},
    "lqc_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_059_capitulation_signal},
    "lqc_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_060_capitulation_signal},
    "lqc_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_061_capitulation_signal},
    "lqc_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_062_capitulation_signal},
    "lqc_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_063_capitulation_signal},
    "lqc_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_064_capitulation_signal},
    "lqc_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_065_capitulation_signal},
    "lqc_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_066_capitulation_signal},
    "lqc_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_067_capitulation_signal},
    "lqc_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_068_capitulation_signal},
    "lqc_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_069_capitulation_signal},
    "lqc_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_070_capitulation_signal},
    "lqc_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_071_capitulation_signal},
    "lqc_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_072_capitulation_signal},
    "lqc_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_073_capitulation_signal},
    "lqc_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_074_capitulation_signal},
    "lqc_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lqc_075_capitulation_signal},
}
