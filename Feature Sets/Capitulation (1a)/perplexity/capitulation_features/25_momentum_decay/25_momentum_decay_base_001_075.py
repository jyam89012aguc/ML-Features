"""Generated capitulation features for 25_momentum_decay: trailing return decay.
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

def mdc_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def mdc_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def mdc_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def mdc_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def mdc_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mdc_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def mdc_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def mdc_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def mdc_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def mdc_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def mdc_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def mdc_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def mdc_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def mdc_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def mdc_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def mdc_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def mdc_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def mdc_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def mdc_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mdc_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def mdc_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def mdc_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def mdc_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def mdc_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def mdc_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def mdc_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def mdc_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def mdc_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def mdc_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def mdc_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def mdc_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def mdc_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def mdc_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mdc_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def mdc_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def mdc_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def mdc_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def mdc_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def mdc_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def mdc_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def mdc_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def mdc_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def mdc_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def mdc_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def mdc_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def mdc_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def mdc_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mdc_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mdc_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def mdc_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def mdc_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def mdc_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def mdc_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def mdc_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def mdc_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mdc_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def mdc_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mdc_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def mdc_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def mdc_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def mdc_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

MOMENTUM_DECAY_REGISTRY_001_075 = {
    "mdc_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_001_capitulation_signal},
    "mdc_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_002_capitulation_signal},
    "mdc_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_003_capitulation_signal},
    "mdc_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_004_capitulation_signal},
    "mdc_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_005_capitulation_signal},
    "mdc_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_006_capitulation_signal},
    "mdc_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_007_capitulation_signal},
    "mdc_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_008_capitulation_signal},
    "mdc_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_009_capitulation_signal},
    "mdc_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_010_capitulation_signal},
    "mdc_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_011_capitulation_signal},
    "mdc_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_012_capitulation_signal},
    "mdc_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_013_capitulation_signal},
    "mdc_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_014_capitulation_signal},
    "mdc_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_015_capitulation_signal},
    "mdc_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_016_capitulation_signal},
    "mdc_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_017_capitulation_signal},
    "mdc_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_018_capitulation_signal},
    "mdc_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_019_capitulation_signal},
    "mdc_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_020_capitulation_signal},
    "mdc_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_021_capitulation_signal},
    "mdc_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_022_capitulation_signal},
    "mdc_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_023_capitulation_signal},
    "mdc_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_024_capitulation_signal},
    "mdc_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_025_capitulation_signal},
    "mdc_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_026_capitulation_signal},
    "mdc_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_027_capitulation_signal},
    "mdc_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_028_capitulation_signal},
    "mdc_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_029_capitulation_signal},
    "mdc_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_030_capitulation_signal},
    "mdc_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_031_capitulation_signal},
    "mdc_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_032_capitulation_signal},
    "mdc_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_033_capitulation_signal},
    "mdc_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_034_capitulation_signal},
    "mdc_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_035_capitulation_signal},
    "mdc_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_036_capitulation_signal},
    "mdc_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_037_capitulation_signal},
    "mdc_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_038_capitulation_signal},
    "mdc_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_039_capitulation_signal},
    "mdc_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_040_capitulation_signal},
    "mdc_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_041_capitulation_signal},
    "mdc_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_042_capitulation_signal},
    "mdc_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_043_capitulation_signal},
    "mdc_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_044_capitulation_signal},
    "mdc_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_045_capitulation_signal},
    "mdc_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_046_capitulation_signal},
    "mdc_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_047_capitulation_signal},
    "mdc_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_048_capitulation_signal},
    "mdc_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_049_capitulation_signal},
    "mdc_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_050_capitulation_signal},
    "mdc_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_051_capitulation_signal},
    "mdc_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_052_capitulation_signal},
    "mdc_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_053_capitulation_signal},
    "mdc_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_054_capitulation_signal},
    "mdc_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_055_capitulation_signal},
    "mdc_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_056_capitulation_signal},
    "mdc_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_057_capitulation_signal},
    "mdc_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_058_capitulation_signal},
    "mdc_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_059_capitulation_signal},
    "mdc_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_060_capitulation_signal},
    "mdc_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_061_capitulation_signal},
    "mdc_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_062_capitulation_signal},
    "mdc_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_063_capitulation_signal},
    "mdc_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_064_capitulation_signal},
    "mdc_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_065_capitulation_signal},
    "mdc_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_066_capitulation_signal},
    "mdc_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_067_capitulation_signal},
    "mdc_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_068_capitulation_signal},
    "mdc_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_069_capitulation_signal},
    "mdc_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_070_capitulation_signal},
    "mdc_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_071_capitulation_signal},
    "mdc_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_072_capitulation_signal},
    "mdc_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_073_capitulation_signal},
    "mdc_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_074_capitulation_signal},
    "mdc_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mdc_075_capitulation_signal},
}
