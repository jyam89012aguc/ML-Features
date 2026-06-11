"""Generated capitulation features for 57_spread_proxy: spread illiquidity proxy.
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

def spr_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def spr_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def spr_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def spr_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def spr_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def spr_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def spr_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def spr_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def spr_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def spr_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def spr_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def spr_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def spr_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def spr_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def spr_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def spr_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def spr_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def spr_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def spr_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def spr_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def spr_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def spr_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def spr_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def spr_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def spr_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def spr_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def spr_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def spr_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def spr_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def spr_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def spr_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def spr_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def spr_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def spr_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def spr_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def spr_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def spr_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def spr_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def spr_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def spr_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def spr_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def spr_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def spr_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def spr_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def spr_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def spr_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def spr_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def spr_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def spr_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def spr_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def spr_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def spr_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def spr_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def spr_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def spr_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def spr_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def spr_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def spr_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def spr_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def spr_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def spr_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def spr_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

SPREAD_PROXY_REGISTRY_001_075 = {
    "spr_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_001_capitulation_signal},
    "spr_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_002_capitulation_signal},
    "spr_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_003_capitulation_signal},
    "spr_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_004_capitulation_signal},
    "spr_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_005_capitulation_signal},
    "spr_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_006_capitulation_signal},
    "spr_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_007_capitulation_signal},
    "spr_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_008_capitulation_signal},
    "spr_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_009_capitulation_signal},
    "spr_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_010_capitulation_signal},
    "spr_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_011_capitulation_signal},
    "spr_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_012_capitulation_signal},
    "spr_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_013_capitulation_signal},
    "spr_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_014_capitulation_signal},
    "spr_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_015_capitulation_signal},
    "spr_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_016_capitulation_signal},
    "spr_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_017_capitulation_signal},
    "spr_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_018_capitulation_signal},
    "spr_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_019_capitulation_signal},
    "spr_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_020_capitulation_signal},
    "spr_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_021_capitulation_signal},
    "spr_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_022_capitulation_signal},
    "spr_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_023_capitulation_signal},
    "spr_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_024_capitulation_signal},
    "spr_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_025_capitulation_signal},
    "spr_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_026_capitulation_signal},
    "spr_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_027_capitulation_signal},
    "spr_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_028_capitulation_signal},
    "spr_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_029_capitulation_signal},
    "spr_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_030_capitulation_signal},
    "spr_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_031_capitulation_signal},
    "spr_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_032_capitulation_signal},
    "spr_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_033_capitulation_signal},
    "spr_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_034_capitulation_signal},
    "spr_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_035_capitulation_signal},
    "spr_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_036_capitulation_signal},
    "spr_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_037_capitulation_signal},
    "spr_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_038_capitulation_signal},
    "spr_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_039_capitulation_signal},
    "spr_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_040_capitulation_signal},
    "spr_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_041_capitulation_signal},
    "spr_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_042_capitulation_signal},
    "spr_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_043_capitulation_signal},
    "spr_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_044_capitulation_signal},
    "spr_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_045_capitulation_signal},
    "spr_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_046_capitulation_signal},
    "spr_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_047_capitulation_signal},
    "spr_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_048_capitulation_signal},
    "spr_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_049_capitulation_signal},
    "spr_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_050_capitulation_signal},
    "spr_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_051_capitulation_signal},
    "spr_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_052_capitulation_signal},
    "spr_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_053_capitulation_signal},
    "spr_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_054_capitulation_signal},
    "spr_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_055_capitulation_signal},
    "spr_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_056_capitulation_signal},
    "spr_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_057_capitulation_signal},
    "spr_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_058_capitulation_signal},
    "spr_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_059_capitulation_signal},
    "spr_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_060_capitulation_signal},
    "spr_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_061_capitulation_signal},
    "spr_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_062_capitulation_signal},
    "spr_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_063_capitulation_signal},
    "spr_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_064_capitulation_signal},
    "spr_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_065_capitulation_signal},
    "spr_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_066_capitulation_signal},
    "spr_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_067_capitulation_signal},
    "spr_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_068_capitulation_signal},
    "spr_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_069_capitulation_signal},
    "spr_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_070_capitulation_signal},
    "spr_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_071_capitulation_signal},
    "spr_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_072_capitulation_signal},
    "spr_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_073_capitulation_signal},
    "spr_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_074_capitulation_signal},
    "spr_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": spr_075_capitulation_signal},
}
