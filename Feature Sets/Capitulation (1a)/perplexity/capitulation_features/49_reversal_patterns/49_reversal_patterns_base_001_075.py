"""Generated capitulation features for 49_reversal_patterns: intraday reversal bars.
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

def rev_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def rev_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def rev_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def rev_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def rev_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rev_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def rev_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def rev_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def rev_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def rev_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def rev_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def rev_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def rev_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def rev_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def rev_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def rev_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def rev_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def rev_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def rev_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rev_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def rev_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def rev_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def rev_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def rev_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def rev_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def rev_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def rev_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def rev_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def rev_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def rev_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def rev_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def rev_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def rev_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rev_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def rev_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def rev_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def rev_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def rev_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def rev_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def rev_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def rev_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def rev_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def rev_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def rev_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def rev_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def rev_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def rev_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rev_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rev_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rev_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def rev_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def rev_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def rev_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def rev_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def rev_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def rev_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rev_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def rev_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rev_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def rev_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def rev_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def rev_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

REVERSAL_PATTERNS_REGISTRY_001_075 = {
    "rev_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_001_capitulation_signal},
    "rev_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_002_capitulation_signal},
    "rev_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_003_capitulation_signal},
    "rev_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_004_capitulation_signal},
    "rev_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_005_capitulation_signal},
    "rev_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_006_capitulation_signal},
    "rev_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_007_capitulation_signal},
    "rev_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_008_capitulation_signal},
    "rev_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_009_capitulation_signal},
    "rev_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_010_capitulation_signal},
    "rev_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_011_capitulation_signal},
    "rev_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_012_capitulation_signal},
    "rev_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_013_capitulation_signal},
    "rev_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_014_capitulation_signal},
    "rev_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_015_capitulation_signal},
    "rev_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_016_capitulation_signal},
    "rev_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_017_capitulation_signal},
    "rev_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_018_capitulation_signal},
    "rev_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_019_capitulation_signal},
    "rev_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_020_capitulation_signal},
    "rev_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_021_capitulation_signal},
    "rev_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_022_capitulation_signal},
    "rev_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_023_capitulation_signal},
    "rev_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_024_capitulation_signal},
    "rev_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_025_capitulation_signal},
    "rev_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_026_capitulation_signal},
    "rev_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_027_capitulation_signal},
    "rev_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_028_capitulation_signal},
    "rev_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_029_capitulation_signal},
    "rev_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_030_capitulation_signal},
    "rev_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_031_capitulation_signal},
    "rev_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_032_capitulation_signal},
    "rev_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_033_capitulation_signal},
    "rev_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_034_capitulation_signal},
    "rev_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_035_capitulation_signal},
    "rev_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_036_capitulation_signal},
    "rev_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_037_capitulation_signal},
    "rev_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_038_capitulation_signal},
    "rev_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_039_capitulation_signal},
    "rev_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_040_capitulation_signal},
    "rev_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_041_capitulation_signal},
    "rev_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_042_capitulation_signal},
    "rev_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_043_capitulation_signal},
    "rev_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_044_capitulation_signal},
    "rev_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_045_capitulation_signal},
    "rev_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_046_capitulation_signal},
    "rev_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_047_capitulation_signal},
    "rev_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_048_capitulation_signal},
    "rev_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_049_capitulation_signal},
    "rev_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_050_capitulation_signal},
    "rev_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_051_capitulation_signal},
    "rev_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_052_capitulation_signal},
    "rev_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_053_capitulation_signal},
    "rev_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_054_capitulation_signal},
    "rev_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_055_capitulation_signal},
    "rev_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_056_capitulation_signal},
    "rev_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_057_capitulation_signal},
    "rev_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_058_capitulation_signal},
    "rev_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_059_capitulation_signal},
    "rev_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_060_capitulation_signal},
    "rev_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_061_capitulation_signal},
    "rev_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_062_capitulation_signal},
    "rev_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_063_capitulation_signal},
    "rev_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_064_capitulation_signal},
    "rev_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_065_capitulation_signal},
    "rev_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_066_capitulation_signal},
    "rev_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_067_capitulation_signal},
    "rev_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_068_capitulation_signal},
    "rev_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_069_capitulation_signal},
    "rev_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_070_capitulation_signal},
    "rev_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_071_capitulation_signal},
    "rev_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_072_capitulation_signal},
    "rev_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_073_capitulation_signal},
    "rev_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_074_capitulation_signal},
    "rev_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rev_075_capitulation_signal},
}
