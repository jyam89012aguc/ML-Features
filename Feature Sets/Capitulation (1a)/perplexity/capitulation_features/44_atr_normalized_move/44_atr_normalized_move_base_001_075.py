"""Generated capitulation features for 44_atr_normalized_move: moves measured in ATR units.
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

def atr_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def atr_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def atr_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def atr_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def atr_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def atr_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def atr_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def atr_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def atr_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def atr_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def atr_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def atr_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def atr_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def atr_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def atr_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def atr_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def atr_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def atr_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def atr_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def atr_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def atr_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def atr_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def atr_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def atr_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def atr_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def atr_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def atr_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def atr_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def atr_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def atr_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def atr_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def atr_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def atr_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def atr_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def atr_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def atr_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def atr_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def atr_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def atr_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def atr_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def atr_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def atr_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def atr_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def atr_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def atr_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def atr_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def atr_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def atr_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def atr_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def atr_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def atr_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def atr_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def atr_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def atr_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def atr_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def atr_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def atr_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def atr_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def atr_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def atr_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def atr_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def atr_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

ATR_NORMALIZED_MOVE_REGISTRY_001_075 = {
    "atr_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_001_capitulation_signal},
    "atr_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_002_capitulation_signal},
    "atr_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_003_capitulation_signal},
    "atr_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_004_capitulation_signal},
    "atr_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_005_capitulation_signal},
    "atr_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_006_capitulation_signal},
    "atr_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_007_capitulation_signal},
    "atr_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_008_capitulation_signal},
    "atr_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_009_capitulation_signal},
    "atr_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_010_capitulation_signal},
    "atr_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_011_capitulation_signal},
    "atr_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_012_capitulation_signal},
    "atr_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_013_capitulation_signal},
    "atr_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_014_capitulation_signal},
    "atr_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_015_capitulation_signal},
    "atr_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_016_capitulation_signal},
    "atr_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_017_capitulation_signal},
    "atr_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_018_capitulation_signal},
    "atr_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_019_capitulation_signal},
    "atr_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_020_capitulation_signal},
    "atr_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_021_capitulation_signal},
    "atr_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_022_capitulation_signal},
    "atr_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_023_capitulation_signal},
    "atr_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_024_capitulation_signal},
    "atr_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_025_capitulation_signal},
    "atr_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_026_capitulation_signal},
    "atr_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_027_capitulation_signal},
    "atr_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_028_capitulation_signal},
    "atr_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_029_capitulation_signal},
    "atr_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_030_capitulation_signal},
    "atr_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_031_capitulation_signal},
    "atr_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_032_capitulation_signal},
    "atr_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_033_capitulation_signal},
    "atr_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_034_capitulation_signal},
    "atr_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_035_capitulation_signal},
    "atr_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_036_capitulation_signal},
    "atr_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_037_capitulation_signal},
    "atr_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_038_capitulation_signal},
    "atr_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_039_capitulation_signal},
    "atr_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_040_capitulation_signal},
    "atr_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_041_capitulation_signal},
    "atr_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_042_capitulation_signal},
    "atr_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_043_capitulation_signal},
    "atr_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_044_capitulation_signal},
    "atr_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_045_capitulation_signal},
    "atr_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_046_capitulation_signal},
    "atr_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_047_capitulation_signal},
    "atr_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_048_capitulation_signal},
    "atr_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_049_capitulation_signal},
    "atr_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_050_capitulation_signal},
    "atr_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_051_capitulation_signal},
    "atr_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_052_capitulation_signal},
    "atr_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_053_capitulation_signal},
    "atr_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_054_capitulation_signal},
    "atr_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_055_capitulation_signal},
    "atr_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_056_capitulation_signal},
    "atr_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_057_capitulation_signal},
    "atr_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_058_capitulation_signal},
    "atr_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_059_capitulation_signal},
    "atr_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_060_capitulation_signal},
    "atr_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_061_capitulation_signal},
    "atr_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_062_capitulation_signal},
    "atr_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_063_capitulation_signal},
    "atr_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_064_capitulation_signal},
    "atr_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_065_capitulation_signal},
    "atr_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_066_capitulation_signal},
    "atr_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_067_capitulation_signal},
    "atr_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_068_capitulation_signal},
    "atr_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_069_capitulation_signal},
    "atr_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_070_capitulation_signal},
    "atr_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_071_capitulation_signal},
    "atr_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_072_capitulation_signal},
    "atr_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_073_capitulation_signal},
    "atr_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_074_capitulation_signal},
    "atr_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": atr_075_capitulation_signal},
}
