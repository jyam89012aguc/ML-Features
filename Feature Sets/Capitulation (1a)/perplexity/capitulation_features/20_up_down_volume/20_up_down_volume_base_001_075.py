"""Generated capitulation features for 20_up_down_volume: down-day vs up-day volume.
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

def udv_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def udv_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def udv_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def udv_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def udv_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def udv_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def udv_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def udv_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def udv_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def udv_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def udv_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def udv_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def udv_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def udv_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def udv_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def udv_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def udv_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def udv_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def udv_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def udv_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def udv_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def udv_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def udv_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def udv_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def udv_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def udv_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def udv_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def udv_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def udv_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def udv_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def udv_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def udv_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def udv_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def udv_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def udv_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def udv_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def udv_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def udv_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def udv_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def udv_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def udv_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def udv_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def udv_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def udv_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def udv_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def udv_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def udv_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def udv_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def udv_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def udv_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def udv_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def udv_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def udv_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def udv_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def udv_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def udv_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def udv_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def udv_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def udv_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def udv_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def udv_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def udv_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

UP_DOWN_VOLUME_REGISTRY_001_075 = {
    "udv_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_001_capitulation_signal},
    "udv_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_002_capitulation_signal},
    "udv_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_003_capitulation_signal},
    "udv_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_004_capitulation_signal},
    "udv_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_005_capitulation_signal},
    "udv_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_006_capitulation_signal},
    "udv_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_007_capitulation_signal},
    "udv_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_008_capitulation_signal},
    "udv_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_009_capitulation_signal},
    "udv_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_010_capitulation_signal},
    "udv_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_011_capitulation_signal},
    "udv_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_012_capitulation_signal},
    "udv_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_013_capitulation_signal},
    "udv_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_014_capitulation_signal},
    "udv_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_015_capitulation_signal},
    "udv_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_016_capitulation_signal},
    "udv_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_017_capitulation_signal},
    "udv_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_018_capitulation_signal},
    "udv_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_019_capitulation_signal},
    "udv_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_020_capitulation_signal},
    "udv_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_021_capitulation_signal},
    "udv_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_022_capitulation_signal},
    "udv_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_023_capitulation_signal},
    "udv_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_024_capitulation_signal},
    "udv_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_025_capitulation_signal},
    "udv_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_026_capitulation_signal},
    "udv_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_027_capitulation_signal},
    "udv_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_028_capitulation_signal},
    "udv_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_029_capitulation_signal},
    "udv_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_030_capitulation_signal},
    "udv_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_031_capitulation_signal},
    "udv_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_032_capitulation_signal},
    "udv_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_033_capitulation_signal},
    "udv_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_034_capitulation_signal},
    "udv_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_035_capitulation_signal},
    "udv_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_036_capitulation_signal},
    "udv_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_037_capitulation_signal},
    "udv_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_038_capitulation_signal},
    "udv_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_039_capitulation_signal},
    "udv_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_040_capitulation_signal},
    "udv_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_041_capitulation_signal},
    "udv_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_042_capitulation_signal},
    "udv_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_043_capitulation_signal},
    "udv_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_044_capitulation_signal},
    "udv_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_045_capitulation_signal},
    "udv_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_046_capitulation_signal},
    "udv_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_047_capitulation_signal},
    "udv_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_048_capitulation_signal},
    "udv_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_049_capitulation_signal},
    "udv_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_050_capitulation_signal},
    "udv_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_051_capitulation_signal},
    "udv_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_052_capitulation_signal},
    "udv_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_053_capitulation_signal},
    "udv_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_054_capitulation_signal},
    "udv_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_055_capitulation_signal},
    "udv_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_056_capitulation_signal},
    "udv_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_057_capitulation_signal},
    "udv_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_058_capitulation_signal},
    "udv_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_059_capitulation_signal},
    "udv_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_060_capitulation_signal},
    "udv_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_061_capitulation_signal},
    "udv_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_062_capitulation_signal},
    "udv_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_063_capitulation_signal},
    "udv_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_064_capitulation_signal},
    "udv_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_065_capitulation_signal},
    "udv_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_066_capitulation_signal},
    "udv_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_067_capitulation_signal},
    "udv_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_068_capitulation_signal},
    "udv_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_069_capitulation_signal},
    "udv_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_070_capitulation_signal},
    "udv_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_071_capitulation_signal},
    "udv_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_072_capitulation_signal},
    "udv_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_073_capitulation_signal},
    "udv_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_074_capitulation_signal},
    "udv_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": udv_075_capitulation_signal},
}
