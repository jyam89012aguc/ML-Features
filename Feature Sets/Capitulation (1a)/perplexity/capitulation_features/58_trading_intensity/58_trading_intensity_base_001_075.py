"""Generated capitulation features for 58_trading_intensity: trade-frequency proxies.
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

def tin_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def tin_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def tin_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def tin_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def tin_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def tin_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def tin_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def tin_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def tin_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def tin_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def tin_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def tin_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def tin_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def tin_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def tin_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def tin_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def tin_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def tin_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def tin_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def tin_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def tin_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def tin_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def tin_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def tin_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def tin_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def tin_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def tin_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def tin_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def tin_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def tin_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def tin_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def tin_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def tin_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def tin_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def tin_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def tin_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def tin_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def tin_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def tin_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def tin_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def tin_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def tin_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def tin_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def tin_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def tin_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def tin_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def tin_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def tin_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def tin_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def tin_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def tin_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def tin_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def tin_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def tin_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def tin_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def tin_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def tin_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def tin_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def tin_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def tin_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def tin_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def tin_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

TRADING_INTENSITY_REGISTRY_001_075 = {
    "tin_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_001_capitulation_signal},
    "tin_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_002_capitulation_signal},
    "tin_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_003_capitulation_signal},
    "tin_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_004_capitulation_signal},
    "tin_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_005_capitulation_signal},
    "tin_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_006_capitulation_signal},
    "tin_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_007_capitulation_signal},
    "tin_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_008_capitulation_signal},
    "tin_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_009_capitulation_signal},
    "tin_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_010_capitulation_signal},
    "tin_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_011_capitulation_signal},
    "tin_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_012_capitulation_signal},
    "tin_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_013_capitulation_signal},
    "tin_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_014_capitulation_signal},
    "tin_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_015_capitulation_signal},
    "tin_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_016_capitulation_signal},
    "tin_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_017_capitulation_signal},
    "tin_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_018_capitulation_signal},
    "tin_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_019_capitulation_signal},
    "tin_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_020_capitulation_signal},
    "tin_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_021_capitulation_signal},
    "tin_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_022_capitulation_signal},
    "tin_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_023_capitulation_signal},
    "tin_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_024_capitulation_signal},
    "tin_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_025_capitulation_signal},
    "tin_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_026_capitulation_signal},
    "tin_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_027_capitulation_signal},
    "tin_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_028_capitulation_signal},
    "tin_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_029_capitulation_signal},
    "tin_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_030_capitulation_signal},
    "tin_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_031_capitulation_signal},
    "tin_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_032_capitulation_signal},
    "tin_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_033_capitulation_signal},
    "tin_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_034_capitulation_signal},
    "tin_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_035_capitulation_signal},
    "tin_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_036_capitulation_signal},
    "tin_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_037_capitulation_signal},
    "tin_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_038_capitulation_signal},
    "tin_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_039_capitulation_signal},
    "tin_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_040_capitulation_signal},
    "tin_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_041_capitulation_signal},
    "tin_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_042_capitulation_signal},
    "tin_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_043_capitulation_signal},
    "tin_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_044_capitulation_signal},
    "tin_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_045_capitulation_signal},
    "tin_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_046_capitulation_signal},
    "tin_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_047_capitulation_signal},
    "tin_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_048_capitulation_signal},
    "tin_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_049_capitulation_signal},
    "tin_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_050_capitulation_signal},
    "tin_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_051_capitulation_signal},
    "tin_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_052_capitulation_signal},
    "tin_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_053_capitulation_signal},
    "tin_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_054_capitulation_signal},
    "tin_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_055_capitulation_signal},
    "tin_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_056_capitulation_signal},
    "tin_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_057_capitulation_signal},
    "tin_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_058_capitulation_signal},
    "tin_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_059_capitulation_signal},
    "tin_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_060_capitulation_signal},
    "tin_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_061_capitulation_signal},
    "tin_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_062_capitulation_signal},
    "tin_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_063_capitulation_signal},
    "tin_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_064_capitulation_signal},
    "tin_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_065_capitulation_signal},
    "tin_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_066_capitulation_signal},
    "tin_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_067_capitulation_signal},
    "tin_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_068_capitulation_signal},
    "tin_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_069_capitulation_signal},
    "tin_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_070_capitulation_signal},
    "tin_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_071_capitulation_signal},
    "tin_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_072_capitulation_signal},
    "tin_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_073_capitulation_signal},
    "tin_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_074_capitulation_signal},
    "tin_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": tin_075_capitulation_signal},
}
