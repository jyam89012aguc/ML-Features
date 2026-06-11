"""Generated capitulation features for 23_dollar_volume_shock: dollar-volume spikes.
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

def dvs_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def dvs_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def dvs_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def dvs_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def dvs_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def dvs_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def dvs_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def dvs_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def dvs_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def dvs_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def dvs_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def dvs_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def dvs_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def dvs_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def dvs_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def dvs_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def dvs_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def dvs_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def dvs_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def dvs_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def dvs_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def dvs_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def dvs_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def dvs_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def dvs_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def dvs_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def dvs_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def dvs_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def dvs_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def dvs_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def dvs_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def dvs_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def dvs_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def dvs_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def dvs_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def dvs_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def dvs_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def dvs_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def dvs_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def dvs_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def dvs_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def dvs_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def dvs_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def dvs_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def dvs_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def dvs_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def dvs_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def dvs_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dvs_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def dvs_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def dvs_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def dvs_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def dvs_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def dvs_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def dvs_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def dvs_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def dvs_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def dvs_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def dvs_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def dvs_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def dvs_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

DOLLAR_VOLUME_SHOCK_REGISTRY_001_075 = {
    "dvs_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_001_capitulation_signal},
    "dvs_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_002_capitulation_signal},
    "dvs_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_003_capitulation_signal},
    "dvs_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_004_capitulation_signal},
    "dvs_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_005_capitulation_signal},
    "dvs_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_006_capitulation_signal},
    "dvs_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_007_capitulation_signal},
    "dvs_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_008_capitulation_signal},
    "dvs_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_009_capitulation_signal},
    "dvs_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_010_capitulation_signal},
    "dvs_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_011_capitulation_signal},
    "dvs_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_012_capitulation_signal},
    "dvs_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_013_capitulation_signal},
    "dvs_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_014_capitulation_signal},
    "dvs_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_015_capitulation_signal},
    "dvs_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_016_capitulation_signal},
    "dvs_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_017_capitulation_signal},
    "dvs_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_018_capitulation_signal},
    "dvs_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_019_capitulation_signal},
    "dvs_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_020_capitulation_signal},
    "dvs_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_021_capitulation_signal},
    "dvs_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_022_capitulation_signal},
    "dvs_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_023_capitulation_signal},
    "dvs_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_024_capitulation_signal},
    "dvs_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_025_capitulation_signal},
    "dvs_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_026_capitulation_signal},
    "dvs_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_027_capitulation_signal},
    "dvs_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_028_capitulation_signal},
    "dvs_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_029_capitulation_signal},
    "dvs_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_030_capitulation_signal},
    "dvs_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_031_capitulation_signal},
    "dvs_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_032_capitulation_signal},
    "dvs_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_033_capitulation_signal},
    "dvs_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_034_capitulation_signal},
    "dvs_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_035_capitulation_signal},
    "dvs_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_036_capitulation_signal},
    "dvs_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_037_capitulation_signal},
    "dvs_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_038_capitulation_signal},
    "dvs_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_039_capitulation_signal},
    "dvs_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_040_capitulation_signal},
    "dvs_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_041_capitulation_signal},
    "dvs_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_042_capitulation_signal},
    "dvs_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_043_capitulation_signal},
    "dvs_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_044_capitulation_signal},
    "dvs_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_045_capitulation_signal},
    "dvs_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_046_capitulation_signal},
    "dvs_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_047_capitulation_signal},
    "dvs_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_048_capitulation_signal},
    "dvs_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_049_capitulation_signal},
    "dvs_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_050_capitulation_signal},
    "dvs_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_051_capitulation_signal},
    "dvs_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_052_capitulation_signal},
    "dvs_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_053_capitulation_signal},
    "dvs_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_054_capitulation_signal},
    "dvs_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_055_capitulation_signal},
    "dvs_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_056_capitulation_signal},
    "dvs_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_057_capitulation_signal},
    "dvs_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_058_capitulation_signal},
    "dvs_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_059_capitulation_signal},
    "dvs_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_060_capitulation_signal},
    "dvs_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_061_capitulation_signal},
    "dvs_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_062_capitulation_signal},
    "dvs_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_063_capitulation_signal},
    "dvs_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_064_capitulation_signal},
    "dvs_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_065_capitulation_signal},
    "dvs_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_066_capitulation_signal},
    "dvs_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_067_capitulation_signal},
    "dvs_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_068_capitulation_signal},
    "dvs_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_069_capitulation_signal},
    "dvs_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_070_capitulation_signal},
    "dvs_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_071_capitulation_signal},
    "dvs_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_072_capitulation_signal},
    "dvs_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_073_capitulation_signal},
    "dvs_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_074_capitulation_signal},
    "dvs_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": dvs_075_capitulation_signal},
}
