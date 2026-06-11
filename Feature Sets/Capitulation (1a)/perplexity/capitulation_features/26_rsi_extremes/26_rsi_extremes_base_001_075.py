"""Generated capitulation features for 26_rsi_extremes: oversold readings.
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

def rsi_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def rsi_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def rsi_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def rsi_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def rsi_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def rsi_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def rsi_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def rsi_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def rsi_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def rsi_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def rsi_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def rsi_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def rsi_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def rsi_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def rsi_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def rsi_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def rsi_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def rsi_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def rsi_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def rsi_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def rsi_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def rsi_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def rsi_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def rsi_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def rsi_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def rsi_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def rsi_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def rsi_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def rsi_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def rsi_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def rsi_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def rsi_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def rsi_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def rsi_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def rsi_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def rsi_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def rsi_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def rsi_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def rsi_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def rsi_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def rsi_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def rsi_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def rsi_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def rsi_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def rsi_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def rsi_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def rsi_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def rsi_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def rsi_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def rsi_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def rsi_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def rsi_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def rsi_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def rsi_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def rsi_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def rsi_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def rsi_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def rsi_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def rsi_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def rsi_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def rsi_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

RSI_EXTREMES_REGISTRY_001_075 = {
    "rsi_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_001_capitulation_signal},
    "rsi_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_002_capitulation_signal},
    "rsi_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_003_capitulation_signal},
    "rsi_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_004_capitulation_signal},
    "rsi_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_005_capitulation_signal},
    "rsi_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_006_capitulation_signal},
    "rsi_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_007_capitulation_signal},
    "rsi_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_008_capitulation_signal},
    "rsi_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_009_capitulation_signal},
    "rsi_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_010_capitulation_signal},
    "rsi_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_011_capitulation_signal},
    "rsi_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_012_capitulation_signal},
    "rsi_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_013_capitulation_signal},
    "rsi_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_014_capitulation_signal},
    "rsi_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_015_capitulation_signal},
    "rsi_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_016_capitulation_signal},
    "rsi_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_017_capitulation_signal},
    "rsi_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_018_capitulation_signal},
    "rsi_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_019_capitulation_signal},
    "rsi_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_020_capitulation_signal},
    "rsi_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_021_capitulation_signal},
    "rsi_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_022_capitulation_signal},
    "rsi_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_023_capitulation_signal},
    "rsi_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_024_capitulation_signal},
    "rsi_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_025_capitulation_signal},
    "rsi_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_026_capitulation_signal},
    "rsi_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_027_capitulation_signal},
    "rsi_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_028_capitulation_signal},
    "rsi_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_029_capitulation_signal},
    "rsi_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_030_capitulation_signal},
    "rsi_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_031_capitulation_signal},
    "rsi_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_032_capitulation_signal},
    "rsi_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_033_capitulation_signal},
    "rsi_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_034_capitulation_signal},
    "rsi_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_035_capitulation_signal},
    "rsi_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_036_capitulation_signal},
    "rsi_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_037_capitulation_signal},
    "rsi_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_038_capitulation_signal},
    "rsi_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_039_capitulation_signal},
    "rsi_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_040_capitulation_signal},
    "rsi_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_041_capitulation_signal},
    "rsi_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_042_capitulation_signal},
    "rsi_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_043_capitulation_signal},
    "rsi_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_044_capitulation_signal},
    "rsi_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_045_capitulation_signal},
    "rsi_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_046_capitulation_signal},
    "rsi_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_047_capitulation_signal},
    "rsi_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_048_capitulation_signal},
    "rsi_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_049_capitulation_signal},
    "rsi_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_050_capitulation_signal},
    "rsi_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_051_capitulation_signal},
    "rsi_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_052_capitulation_signal},
    "rsi_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_053_capitulation_signal},
    "rsi_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_054_capitulation_signal},
    "rsi_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_055_capitulation_signal},
    "rsi_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_056_capitulation_signal},
    "rsi_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_057_capitulation_signal},
    "rsi_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_058_capitulation_signal},
    "rsi_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_059_capitulation_signal},
    "rsi_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_060_capitulation_signal},
    "rsi_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_061_capitulation_signal},
    "rsi_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_062_capitulation_signal},
    "rsi_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_063_capitulation_signal},
    "rsi_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_064_capitulation_signal},
    "rsi_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_065_capitulation_signal},
    "rsi_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_066_capitulation_signal},
    "rsi_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_067_capitulation_signal},
    "rsi_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_068_capitulation_signal},
    "rsi_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_069_capitulation_signal},
    "rsi_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_070_capitulation_signal},
    "rsi_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_071_capitulation_signal},
    "rsi_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_072_capitulation_signal},
    "rsi_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_073_capitulation_signal},
    "rsi_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_074_capitulation_signal},
    "rsi_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": rsi_075_capitulation_signal},
}
