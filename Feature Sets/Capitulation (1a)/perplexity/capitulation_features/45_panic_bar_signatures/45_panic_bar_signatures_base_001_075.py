"""Generated capitulation features for 45_panic_bar_signatures: wide-range/long-tail bars.
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

def pbs_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def pbs_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def pbs_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def pbs_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def pbs_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def pbs_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def pbs_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def pbs_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def pbs_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def pbs_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def pbs_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def pbs_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def pbs_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def pbs_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def pbs_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def pbs_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def pbs_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def pbs_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def pbs_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def pbs_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def pbs_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def pbs_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def pbs_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def pbs_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def pbs_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def pbs_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def pbs_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def pbs_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def pbs_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def pbs_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def pbs_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def pbs_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def pbs_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def pbs_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def pbs_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def pbs_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def pbs_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def pbs_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def pbs_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def pbs_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def pbs_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def pbs_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def pbs_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def pbs_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def pbs_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def pbs_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def pbs_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def pbs_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def pbs_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def pbs_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def pbs_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def pbs_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def pbs_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def pbs_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def pbs_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def pbs_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def pbs_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def pbs_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def pbs_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def pbs_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def pbs_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

PANIC_BAR_SIGNATURES_REGISTRY_001_075 = {
    "pbs_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_001_capitulation_signal},
    "pbs_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_002_capitulation_signal},
    "pbs_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_003_capitulation_signal},
    "pbs_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_004_capitulation_signal},
    "pbs_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_005_capitulation_signal},
    "pbs_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_006_capitulation_signal},
    "pbs_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_007_capitulation_signal},
    "pbs_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_008_capitulation_signal},
    "pbs_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_009_capitulation_signal},
    "pbs_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_010_capitulation_signal},
    "pbs_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_011_capitulation_signal},
    "pbs_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_012_capitulation_signal},
    "pbs_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_013_capitulation_signal},
    "pbs_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_014_capitulation_signal},
    "pbs_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_015_capitulation_signal},
    "pbs_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_016_capitulation_signal},
    "pbs_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_017_capitulation_signal},
    "pbs_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_018_capitulation_signal},
    "pbs_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_019_capitulation_signal},
    "pbs_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_020_capitulation_signal},
    "pbs_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_021_capitulation_signal},
    "pbs_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_022_capitulation_signal},
    "pbs_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_023_capitulation_signal},
    "pbs_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_024_capitulation_signal},
    "pbs_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_025_capitulation_signal},
    "pbs_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_026_capitulation_signal},
    "pbs_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_027_capitulation_signal},
    "pbs_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_028_capitulation_signal},
    "pbs_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_029_capitulation_signal},
    "pbs_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_030_capitulation_signal},
    "pbs_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_031_capitulation_signal},
    "pbs_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_032_capitulation_signal},
    "pbs_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_033_capitulation_signal},
    "pbs_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_034_capitulation_signal},
    "pbs_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_035_capitulation_signal},
    "pbs_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_036_capitulation_signal},
    "pbs_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_037_capitulation_signal},
    "pbs_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_038_capitulation_signal},
    "pbs_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_039_capitulation_signal},
    "pbs_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_040_capitulation_signal},
    "pbs_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_041_capitulation_signal},
    "pbs_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_042_capitulation_signal},
    "pbs_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_043_capitulation_signal},
    "pbs_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_044_capitulation_signal},
    "pbs_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_045_capitulation_signal},
    "pbs_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_046_capitulation_signal},
    "pbs_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_047_capitulation_signal},
    "pbs_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_048_capitulation_signal},
    "pbs_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_049_capitulation_signal},
    "pbs_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_050_capitulation_signal},
    "pbs_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_051_capitulation_signal},
    "pbs_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_052_capitulation_signal},
    "pbs_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_053_capitulation_signal},
    "pbs_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_054_capitulation_signal},
    "pbs_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_055_capitulation_signal},
    "pbs_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_056_capitulation_signal},
    "pbs_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_057_capitulation_signal},
    "pbs_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_058_capitulation_signal},
    "pbs_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_059_capitulation_signal},
    "pbs_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_060_capitulation_signal},
    "pbs_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_061_capitulation_signal},
    "pbs_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_062_capitulation_signal},
    "pbs_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_063_capitulation_signal},
    "pbs_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_064_capitulation_signal},
    "pbs_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_065_capitulation_signal},
    "pbs_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_066_capitulation_signal},
    "pbs_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_067_capitulation_signal},
    "pbs_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_068_capitulation_signal},
    "pbs_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_069_capitulation_signal},
    "pbs_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_070_capitulation_signal},
    "pbs_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_071_capitulation_signal},
    "pbs_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_072_capitulation_signal},
    "pbs_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_073_capitulation_signal},
    "pbs_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_074_capitulation_signal},
    "pbs_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": pbs_075_capitulation_signal},
}
