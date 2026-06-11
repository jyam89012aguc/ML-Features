"""Generated capitulation features for 51_shadow_wick_analysis: wick ratios.
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

def swk_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def swk_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def swk_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def swk_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def swk_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def swk_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def swk_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def swk_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def swk_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def swk_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def swk_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def swk_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def swk_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def swk_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def swk_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def swk_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def swk_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def swk_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def swk_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def swk_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def swk_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def swk_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def swk_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def swk_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def swk_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def swk_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def swk_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def swk_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def swk_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def swk_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def swk_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def swk_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def swk_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def swk_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def swk_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def swk_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def swk_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def swk_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def swk_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def swk_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def swk_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def swk_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def swk_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def swk_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def swk_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def swk_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def swk_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def swk_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def swk_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def swk_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def swk_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def swk_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def swk_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def swk_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def swk_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def swk_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def swk_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def swk_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def swk_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def swk_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def swk_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def swk_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

SHADOW_WICK_ANALYSIS_REGISTRY_001_075 = {
    "swk_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_001_capitulation_signal},
    "swk_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_002_capitulation_signal},
    "swk_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_003_capitulation_signal},
    "swk_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_004_capitulation_signal},
    "swk_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_005_capitulation_signal},
    "swk_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_006_capitulation_signal},
    "swk_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_007_capitulation_signal},
    "swk_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_008_capitulation_signal},
    "swk_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_009_capitulation_signal},
    "swk_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_010_capitulation_signal},
    "swk_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_011_capitulation_signal},
    "swk_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_012_capitulation_signal},
    "swk_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_013_capitulation_signal},
    "swk_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_014_capitulation_signal},
    "swk_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_015_capitulation_signal},
    "swk_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_016_capitulation_signal},
    "swk_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_017_capitulation_signal},
    "swk_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_018_capitulation_signal},
    "swk_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_019_capitulation_signal},
    "swk_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_020_capitulation_signal},
    "swk_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_021_capitulation_signal},
    "swk_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_022_capitulation_signal},
    "swk_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_023_capitulation_signal},
    "swk_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_024_capitulation_signal},
    "swk_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_025_capitulation_signal},
    "swk_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_026_capitulation_signal},
    "swk_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_027_capitulation_signal},
    "swk_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_028_capitulation_signal},
    "swk_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_029_capitulation_signal},
    "swk_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_030_capitulation_signal},
    "swk_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_031_capitulation_signal},
    "swk_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_032_capitulation_signal},
    "swk_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_033_capitulation_signal},
    "swk_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_034_capitulation_signal},
    "swk_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_035_capitulation_signal},
    "swk_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_036_capitulation_signal},
    "swk_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_037_capitulation_signal},
    "swk_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_038_capitulation_signal},
    "swk_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_039_capitulation_signal},
    "swk_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_040_capitulation_signal},
    "swk_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_041_capitulation_signal},
    "swk_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_042_capitulation_signal},
    "swk_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_043_capitulation_signal},
    "swk_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_044_capitulation_signal},
    "swk_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_045_capitulation_signal},
    "swk_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_046_capitulation_signal},
    "swk_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_047_capitulation_signal},
    "swk_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_048_capitulation_signal},
    "swk_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_049_capitulation_signal},
    "swk_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_050_capitulation_signal},
    "swk_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_051_capitulation_signal},
    "swk_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_052_capitulation_signal},
    "swk_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_053_capitulation_signal},
    "swk_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_054_capitulation_signal},
    "swk_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_055_capitulation_signal},
    "swk_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_056_capitulation_signal},
    "swk_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_057_capitulation_signal},
    "swk_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_058_capitulation_signal},
    "swk_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_059_capitulation_signal},
    "swk_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_060_capitulation_signal},
    "swk_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_061_capitulation_signal},
    "swk_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_062_capitulation_signal},
    "swk_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_063_capitulation_signal},
    "swk_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_064_capitulation_signal},
    "swk_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_065_capitulation_signal},
    "swk_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_066_capitulation_signal},
    "swk_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_067_capitulation_signal},
    "swk_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_068_capitulation_signal},
    "swk_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_069_capitulation_signal},
    "swk_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_070_capitulation_signal},
    "swk_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_071_capitulation_signal},
    "swk_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_072_capitulation_signal},
    "swk_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_073_capitulation_signal},
    "swk_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_074_capitulation_signal},
    "swk_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": swk_075_capitulation_signal},
}
