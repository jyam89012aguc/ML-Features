"""Generated capitulation features for 07_peak_to_trough: peak-trough ratios.
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

def ptt_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def ptt_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def ptt_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def ptt_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def ptt_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ptt_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def ptt_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def ptt_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def ptt_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def ptt_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def ptt_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def ptt_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def ptt_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def ptt_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def ptt_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def ptt_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def ptt_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def ptt_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def ptt_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ptt_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def ptt_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def ptt_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def ptt_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def ptt_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def ptt_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def ptt_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def ptt_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def ptt_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def ptt_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def ptt_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def ptt_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def ptt_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def ptt_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ptt_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def ptt_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def ptt_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def ptt_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def ptt_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def ptt_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def ptt_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def ptt_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def ptt_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def ptt_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def ptt_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def ptt_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def ptt_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def ptt_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ptt_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ptt_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def ptt_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def ptt_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def ptt_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def ptt_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def ptt_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def ptt_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ptt_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def ptt_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ptt_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def ptt_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def ptt_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def ptt_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

PEAK_TO_TROUGH_REGISTRY_001_075 = {
    "ptt_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_001_capitulation_signal},
    "ptt_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_002_capitulation_signal},
    "ptt_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_003_capitulation_signal},
    "ptt_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_004_capitulation_signal},
    "ptt_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_005_capitulation_signal},
    "ptt_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_006_capitulation_signal},
    "ptt_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_007_capitulation_signal},
    "ptt_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_008_capitulation_signal},
    "ptt_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_009_capitulation_signal},
    "ptt_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_010_capitulation_signal},
    "ptt_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_011_capitulation_signal},
    "ptt_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_012_capitulation_signal},
    "ptt_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_013_capitulation_signal},
    "ptt_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_014_capitulation_signal},
    "ptt_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_015_capitulation_signal},
    "ptt_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_016_capitulation_signal},
    "ptt_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_017_capitulation_signal},
    "ptt_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_018_capitulation_signal},
    "ptt_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_019_capitulation_signal},
    "ptt_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_020_capitulation_signal},
    "ptt_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_021_capitulation_signal},
    "ptt_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_022_capitulation_signal},
    "ptt_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_023_capitulation_signal},
    "ptt_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_024_capitulation_signal},
    "ptt_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_025_capitulation_signal},
    "ptt_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_026_capitulation_signal},
    "ptt_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_027_capitulation_signal},
    "ptt_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_028_capitulation_signal},
    "ptt_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_029_capitulation_signal},
    "ptt_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_030_capitulation_signal},
    "ptt_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_031_capitulation_signal},
    "ptt_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_032_capitulation_signal},
    "ptt_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_033_capitulation_signal},
    "ptt_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_034_capitulation_signal},
    "ptt_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_035_capitulation_signal},
    "ptt_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_036_capitulation_signal},
    "ptt_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_037_capitulation_signal},
    "ptt_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_038_capitulation_signal},
    "ptt_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_039_capitulation_signal},
    "ptt_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_040_capitulation_signal},
    "ptt_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_041_capitulation_signal},
    "ptt_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_042_capitulation_signal},
    "ptt_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_043_capitulation_signal},
    "ptt_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_044_capitulation_signal},
    "ptt_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_045_capitulation_signal},
    "ptt_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_046_capitulation_signal},
    "ptt_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_047_capitulation_signal},
    "ptt_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_048_capitulation_signal},
    "ptt_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_049_capitulation_signal},
    "ptt_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_050_capitulation_signal},
    "ptt_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_051_capitulation_signal},
    "ptt_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_052_capitulation_signal},
    "ptt_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_053_capitulation_signal},
    "ptt_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_054_capitulation_signal},
    "ptt_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_055_capitulation_signal},
    "ptt_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_056_capitulation_signal},
    "ptt_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_057_capitulation_signal},
    "ptt_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_058_capitulation_signal},
    "ptt_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_059_capitulation_signal},
    "ptt_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_060_capitulation_signal},
    "ptt_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_061_capitulation_signal},
    "ptt_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_062_capitulation_signal},
    "ptt_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_063_capitulation_signal},
    "ptt_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_064_capitulation_signal},
    "ptt_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_065_capitulation_signal},
    "ptt_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_066_capitulation_signal},
    "ptt_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_067_capitulation_signal},
    "ptt_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_068_capitulation_signal},
    "ptt_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_069_capitulation_signal},
    "ptt_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_070_capitulation_signal},
    "ptt_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_071_capitulation_signal},
    "ptt_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_072_capitulation_signal},
    "ptt_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_073_capitulation_signal},
    "ptt_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_074_capitulation_signal},
    "ptt_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ptt_075_capitulation_signal},
}
