"""Generated capitulation features for 38_volatility_regime: volatility regime shift.
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

def vrg_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def vrg_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def vrg_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def vrg_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def vrg_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def vrg_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def vrg_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def vrg_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def vrg_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def vrg_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def vrg_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def vrg_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def vrg_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def vrg_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def vrg_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def vrg_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def vrg_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def vrg_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def vrg_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def vrg_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def vrg_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def vrg_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def vrg_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def vrg_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def vrg_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def vrg_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def vrg_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def vrg_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def vrg_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def vrg_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def vrg_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def vrg_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def vrg_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def vrg_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def vrg_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def vrg_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def vrg_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def vrg_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def vrg_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def vrg_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def vrg_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def vrg_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def vrg_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def vrg_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def vrg_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def vrg_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def vrg_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def vrg_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def vrg_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def vrg_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def vrg_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def vrg_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def vrg_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def vrg_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def vrg_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def vrg_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def vrg_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def vrg_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def vrg_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def vrg_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def vrg_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

VOLATILITY_REGIME_REGISTRY_001_075 = {
    "vrg_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_001_capitulation_signal},
    "vrg_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_002_capitulation_signal},
    "vrg_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_003_capitulation_signal},
    "vrg_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_004_capitulation_signal},
    "vrg_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_005_capitulation_signal},
    "vrg_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_006_capitulation_signal},
    "vrg_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_007_capitulation_signal},
    "vrg_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_008_capitulation_signal},
    "vrg_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_009_capitulation_signal},
    "vrg_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_010_capitulation_signal},
    "vrg_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_011_capitulation_signal},
    "vrg_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_012_capitulation_signal},
    "vrg_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_013_capitulation_signal},
    "vrg_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_014_capitulation_signal},
    "vrg_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_015_capitulation_signal},
    "vrg_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_016_capitulation_signal},
    "vrg_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_017_capitulation_signal},
    "vrg_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_018_capitulation_signal},
    "vrg_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_019_capitulation_signal},
    "vrg_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_020_capitulation_signal},
    "vrg_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_021_capitulation_signal},
    "vrg_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_022_capitulation_signal},
    "vrg_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_023_capitulation_signal},
    "vrg_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_024_capitulation_signal},
    "vrg_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_025_capitulation_signal},
    "vrg_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_026_capitulation_signal},
    "vrg_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_027_capitulation_signal},
    "vrg_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_028_capitulation_signal},
    "vrg_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_029_capitulation_signal},
    "vrg_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_030_capitulation_signal},
    "vrg_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_031_capitulation_signal},
    "vrg_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_032_capitulation_signal},
    "vrg_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_033_capitulation_signal},
    "vrg_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_034_capitulation_signal},
    "vrg_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_035_capitulation_signal},
    "vrg_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_036_capitulation_signal},
    "vrg_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_037_capitulation_signal},
    "vrg_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_038_capitulation_signal},
    "vrg_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_039_capitulation_signal},
    "vrg_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_040_capitulation_signal},
    "vrg_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_041_capitulation_signal},
    "vrg_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_042_capitulation_signal},
    "vrg_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_043_capitulation_signal},
    "vrg_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_044_capitulation_signal},
    "vrg_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_045_capitulation_signal},
    "vrg_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_046_capitulation_signal},
    "vrg_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_047_capitulation_signal},
    "vrg_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_048_capitulation_signal},
    "vrg_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_049_capitulation_signal},
    "vrg_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_050_capitulation_signal},
    "vrg_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_051_capitulation_signal},
    "vrg_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_052_capitulation_signal},
    "vrg_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_053_capitulation_signal},
    "vrg_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_054_capitulation_signal},
    "vrg_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_055_capitulation_signal},
    "vrg_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_056_capitulation_signal},
    "vrg_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_057_capitulation_signal},
    "vrg_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_058_capitulation_signal},
    "vrg_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_059_capitulation_signal},
    "vrg_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_060_capitulation_signal},
    "vrg_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_061_capitulation_signal},
    "vrg_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_062_capitulation_signal},
    "vrg_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_063_capitulation_signal},
    "vrg_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_064_capitulation_signal},
    "vrg_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_065_capitulation_signal},
    "vrg_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_066_capitulation_signal},
    "vrg_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_067_capitulation_signal},
    "vrg_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_068_capitulation_signal},
    "vrg_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_069_capitulation_signal},
    "vrg_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_070_capitulation_signal},
    "vrg_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_071_capitulation_signal},
    "vrg_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_072_capitulation_signal},
    "vrg_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_073_capitulation_signal},
    "vrg_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_074_capitulation_signal},
    "vrg_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vrg_075_capitulation_signal},
}
