"""Generated capitulation features for 52_bar_morphology: candlestick body/range stats.
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

def bmf_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def bmf_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def bmf_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def bmf_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def bmf_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def bmf_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def bmf_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def bmf_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def bmf_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def bmf_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def bmf_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def bmf_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def bmf_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def bmf_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def bmf_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def bmf_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def bmf_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def bmf_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def bmf_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def bmf_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def bmf_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def bmf_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def bmf_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def bmf_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def bmf_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def bmf_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def bmf_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def bmf_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def bmf_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def bmf_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def bmf_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def bmf_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def bmf_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def bmf_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def bmf_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def bmf_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def bmf_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def bmf_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def bmf_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def bmf_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def bmf_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def bmf_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def bmf_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def bmf_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def bmf_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def bmf_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def bmf_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def bmf_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def bmf_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def bmf_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def bmf_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def bmf_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def bmf_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def bmf_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def bmf_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def bmf_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def bmf_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def bmf_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def bmf_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def bmf_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def bmf_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

BAR_MORPHOLOGY_REGISTRY_001_075 = {
    "bmf_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_001_capitulation_signal},
    "bmf_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_002_capitulation_signal},
    "bmf_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_003_capitulation_signal},
    "bmf_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_004_capitulation_signal},
    "bmf_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_005_capitulation_signal},
    "bmf_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_006_capitulation_signal},
    "bmf_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_007_capitulation_signal},
    "bmf_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_008_capitulation_signal},
    "bmf_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_009_capitulation_signal},
    "bmf_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_010_capitulation_signal},
    "bmf_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_011_capitulation_signal},
    "bmf_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_012_capitulation_signal},
    "bmf_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_013_capitulation_signal},
    "bmf_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_014_capitulation_signal},
    "bmf_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_015_capitulation_signal},
    "bmf_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_016_capitulation_signal},
    "bmf_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_017_capitulation_signal},
    "bmf_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_018_capitulation_signal},
    "bmf_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_019_capitulation_signal},
    "bmf_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_020_capitulation_signal},
    "bmf_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_021_capitulation_signal},
    "bmf_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_022_capitulation_signal},
    "bmf_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_023_capitulation_signal},
    "bmf_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_024_capitulation_signal},
    "bmf_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_025_capitulation_signal},
    "bmf_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_026_capitulation_signal},
    "bmf_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_027_capitulation_signal},
    "bmf_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_028_capitulation_signal},
    "bmf_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_029_capitulation_signal},
    "bmf_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_030_capitulation_signal},
    "bmf_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_031_capitulation_signal},
    "bmf_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_032_capitulation_signal},
    "bmf_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_033_capitulation_signal},
    "bmf_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_034_capitulation_signal},
    "bmf_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_035_capitulation_signal},
    "bmf_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_036_capitulation_signal},
    "bmf_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_037_capitulation_signal},
    "bmf_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_038_capitulation_signal},
    "bmf_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_039_capitulation_signal},
    "bmf_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_040_capitulation_signal},
    "bmf_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_041_capitulation_signal},
    "bmf_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_042_capitulation_signal},
    "bmf_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_043_capitulation_signal},
    "bmf_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_044_capitulation_signal},
    "bmf_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_045_capitulation_signal},
    "bmf_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_046_capitulation_signal},
    "bmf_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_047_capitulation_signal},
    "bmf_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_048_capitulation_signal},
    "bmf_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_049_capitulation_signal},
    "bmf_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_050_capitulation_signal},
    "bmf_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_051_capitulation_signal},
    "bmf_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_052_capitulation_signal},
    "bmf_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_053_capitulation_signal},
    "bmf_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_054_capitulation_signal},
    "bmf_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_055_capitulation_signal},
    "bmf_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_056_capitulation_signal},
    "bmf_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_057_capitulation_signal},
    "bmf_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_058_capitulation_signal},
    "bmf_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_059_capitulation_signal},
    "bmf_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_060_capitulation_signal},
    "bmf_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_061_capitulation_signal},
    "bmf_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_062_capitulation_signal},
    "bmf_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_063_capitulation_signal},
    "bmf_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_064_capitulation_signal},
    "bmf_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_065_capitulation_signal},
    "bmf_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_066_capitulation_signal},
    "bmf_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_067_capitulation_signal},
    "bmf_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_068_capitulation_signal},
    "bmf_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_069_capitulation_signal},
    "bmf_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_070_capitulation_signal},
    "bmf_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_071_capitulation_signal},
    "bmf_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_072_capitulation_signal},
    "bmf_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_073_capitulation_signal},
    "bmf_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_074_capitulation_signal},
    "bmf_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": bmf_075_capitulation_signal},
}
