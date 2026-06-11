"""Generated capitulation features for 15_volume_blowoff: volume spikes vs trailing median.
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

def vb_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vb_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vb_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vb_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vb_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vb_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vb_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vb_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vb_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vb_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vb_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vb_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vb_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vb_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vb_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vb_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vb_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vb_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vb_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vb_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vb_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vb_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vb_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vb_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vb_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vb_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vb_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vb_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vb_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vb_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vb_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vb_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vb_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vb_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vb_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vb_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vb_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vb_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vb_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vb_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vb_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vb_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vb_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vb_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vb_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vb_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vb_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vb_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vb_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vb_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vb_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vb_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vb_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vb_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vb_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vb_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vb_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vb_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vb_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vb_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vb_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vb_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLUME_BLOWOFF_REGISTRY_001_075 = {
    "vb_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_001_capitulation_signal},
    "vb_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_002_capitulation_signal},
    "vb_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_003_capitulation_signal},
    "vb_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_004_capitulation_signal},
    "vb_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_005_capitulation_signal},
    "vb_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_006_capitulation_signal},
    "vb_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_007_capitulation_signal},
    "vb_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_008_capitulation_signal},
    "vb_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_009_capitulation_signal},
    "vb_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_010_capitulation_signal},
    "vb_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_011_capitulation_signal},
    "vb_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_012_capitulation_signal},
    "vb_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_013_capitulation_signal},
    "vb_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_014_capitulation_signal},
    "vb_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_015_capitulation_signal},
    "vb_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_016_capitulation_signal},
    "vb_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_017_capitulation_signal},
    "vb_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_018_capitulation_signal},
    "vb_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_019_capitulation_signal},
    "vb_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_020_capitulation_signal},
    "vb_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_021_capitulation_signal},
    "vb_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_022_capitulation_signal},
    "vb_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_023_capitulation_signal},
    "vb_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_024_capitulation_signal},
    "vb_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_025_capitulation_signal},
    "vb_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_026_capitulation_signal},
    "vb_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_027_capitulation_signal},
    "vb_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_028_capitulation_signal},
    "vb_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_029_capitulation_signal},
    "vb_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_030_capitulation_signal},
    "vb_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_031_capitulation_signal},
    "vb_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_032_capitulation_signal},
    "vb_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_033_capitulation_signal},
    "vb_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_034_capitulation_signal},
    "vb_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_035_capitulation_signal},
    "vb_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_036_capitulation_signal},
    "vb_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_037_capitulation_signal},
    "vb_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_038_capitulation_signal},
    "vb_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_039_capitulation_signal},
    "vb_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_040_capitulation_signal},
    "vb_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_041_capitulation_signal},
    "vb_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_042_capitulation_signal},
    "vb_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_043_capitulation_signal},
    "vb_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_044_capitulation_signal},
    "vb_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_045_capitulation_signal},
    "vb_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_046_capitulation_signal},
    "vb_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_047_capitulation_signal},
    "vb_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_048_capitulation_signal},
    "vb_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_049_capitulation_signal},
    "vb_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_050_capitulation_signal},
    "vb_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_051_capitulation_signal},
    "vb_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_052_capitulation_signal},
    "vb_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_053_capitulation_signal},
    "vb_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_054_capitulation_signal},
    "vb_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_055_capitulation_signal},
    "vb_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_056_capitulation_signal},
    "vb_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_057_capitulation_signal},
    "vb_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_058_capitulation_signal},
    "vb_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_059_capitulation_signal},
    "vb_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_060_capitulation_signal},
    "vb_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_061_capitulation_signal},
    "vb_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_062_capitulation_signal},
    "vb_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_063_capitulation_signal},
    "vb_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_064_capitulation_signal},
    "vb_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_065_capitulation_signal},
    "vb_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_066_capitulation_signal},
    "vb_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_067_capitulation_signal},
    "vb_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_068_capitulation_signal},
    "vb_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_069_capitulation_signal},
    "vb_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_070_capitulation_signal},
    "vb_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_071_capitulation_signal},
    "vb_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_072_capitulation_signal},
    "vb_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_073_capitulation_signal},
    "vb_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_074_capitulation_signal},
    "vb_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vb_075_capitulation_signal},
}
