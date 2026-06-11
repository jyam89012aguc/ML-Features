"""Generated capitulation features for 02_drawdown_duration: time in drawdown, days since high.
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

def ddur_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def ddur_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def ddur_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def ddur_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def ddur_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def ddur_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def ddur_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def ddur_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def ddur_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def ddur_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def ddur_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def ddur_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def ddur_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def ddur_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def ddur_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def ddur_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def ddur_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def ddur_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def ddur_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def ddur_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def ddur_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def ddur_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def ddur_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def ddur_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def ddur_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def ddur_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def ddur_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def ddur_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def ddur_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def ddur_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def ddur_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def ddur_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def ddur_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def ddur_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def ddur_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def ddur_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def ddur_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def ddur_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def ddur_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def ddur_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def ddur_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def ddur_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def ddur_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def ddur_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def ddur_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def ddur_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def ddur_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def ddur_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ddur_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def ddur_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def ddur_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def ddur_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def ddur_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def ddur_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def ddur_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def ddur_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def ddur_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def ddur_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def ddur_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def ddur_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def ddur_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DRAWDOWN_DURATION_REGISTRY_001_075 = {
    "ddur_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_001_capitulation_signal},
    "ddur_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_002_capitulation_signal},
    "ddur_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_003_capitulation_signal},
    "ddur_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_004_capitulation_signal},
    "ddur_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_005_capitulation_signal},
    "ddur_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_006_capitulation_signal},
    "ddur_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_007_capitulation_signal},
    "ddur_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_008_capitulation_signal},
    "ddur_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_009_capitulation_signal},
    "ddur_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_010_capitulation_signal},
    "ddur_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_011_capitulation_signal},
    "ddur_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_012_capitulation_signal},
    "ddur_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_013_capitulation_signal},
    "ddur_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_014_capitulation_signal},
    "ddur_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_015_capitulation_signal},
    "ddur_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_016_capitulation_signal},
    "ddur_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_017_capitulation_signal},
    "ddur_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_018_capitulation_signal},
    "ddur_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_019_capitulation_signal},
    "ddur_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_020_capitulation_signal},
    "ddur_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_021_capitulation_signal},
    "ddur_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_022_capitulation_signal},
    "ddur_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_023_capitulation_signal},
    "ddur_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_024_capitulation_signal},
    "ddur_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_025_capitulation_signal},
    "ddur_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_026_capitulation_signal},
    "ddur_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_027_capitulation_signal},
    "ddur_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_028_capitulation_signal},
    "ddur_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_029_capitulation_signal},
    "ddur_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_030_capitulation_signal},
    "ddur_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_031_capitulation_signal},
    "ddur_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_032_capitulation_signal},
    "ddur_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_033_capitulation_signal},
    "ddur_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_034_capitulation_signal},
    "ddur_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_035_capitulation_signal},
    "ddur_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_036_capitulation_signal},
    "ddur_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_037_capitulation_signal},
    "ddur_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_038_capitulation_signal},
    "ddur_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_039_capitulation_signal},
    "ddur_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_040_capitulation_signal},
    "ddur_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_041_capitulation_signal},
    "ddur_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_042_capitulation_signal},
    "ddur_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_043_capitulation_signal},
    "ddur_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_044_capitulation_signal},
    "ddur_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_045_capitulation_signal},
    "ddur_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_046_capitulation_signal},
    "ddur_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_047_capitulation_signal},
    "ddur_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_048_capitulation_signal},
    "ddur_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_049_capitulation_signal},
    "ddur_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_050_capitulation_signal},
    "ddur_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_051_capitulation_signal},
    "ddur_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_052_capitulation_signal},
    "ddur_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_053_capitulation_signal},
    "ddur_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_054_capitulation_signal},
    "ddur_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_055_capitulation_signal},
    "ddur_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_056_capitulation_signal},
    "ddur_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_057_capitulation_signal},
    "ddur_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_058_capitulation_signal},
    "ddur_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_059_capitulation_signal},
    "ddur_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_060_capitulation_signal},
    "ddur_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_061_capitulation_signal},
    "ddur_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_062_capitulation_signal},
    "ddur_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_063_capitulation_signal},
    "ddur_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_064_capitulation_signal},
    "ddur_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_065_capitulation_signal},
    "ddur_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_066_capitulation_signal},
    "ddur_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_067_capitulation_signal},
    "ddur_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_068_capitulation_signal},
    "ddur_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_069_capitulation_signal},
    "ddur_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_070_capitulation_signal},
    "ddur_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_071_capitulation_signal},
    "ddur_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_072_capitulation_signal},
    "ddur_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_073_capitulation_signal},
    "ddur_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_074_capitulation_signal},
    "ddur_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": ddur_075_capitulation_signal},
}
