"""Generated capitulation features for 59_market_impact_proxy: return per dollar-volume.
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

def mip_001_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(10, min_periods=max(3, 10//4)).min()) - 1.0

def mip_002_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21)

def mip_003_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 42)

def mip_004_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(63, min_periods=max(3, 63//4)).median())

def mip_005_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(21, min_periods=max(3, 21//4)).mean()

def mip_006_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_007_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(504, min_periods=max(3, 504//4)).mean()

def mip_008_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).skew()

def mip_009_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(1008, min_periods=max(3, 1008//4)).kurt()

def mip_010_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1260, min_periods=max(3, 1260//4)).median())

def mip_011_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 5)

def mip_012_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 10)

def mip_013_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(126, min_periods=max(3, 126//4)).mean(), _s(close).rolling(21, min_periods=max(3, 21//4)).mean()) - 1.0

def mip_014_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_015_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_016_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(42) - _s(close).pct_change(126)

def mip_017_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_018_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).max()) - 1.0

def mip_019_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(756, min_periods=max(3, 756//4)).min()) - 1.0

def mip_020_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(1008)

def mip_021_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1260)

def mip_022_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(5, min_periods=max(3, 5//4)).median())

def mip_023_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(126, min_periods=max(3, 126//4)).mean()

def mip_024_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_025_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(42, min_periods=max(3, 42//4)).mean()

def mip_026_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(63, min_periods=max(3, 63//4)).skew()

def mip_027_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(126, min_periods=max(3, 126//4)).kurt()

def mip_028_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(252, min_periods=max(3, 252//4)).median())

def mip_029_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 504)

def mip_030_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 756)

def mip_031_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(42, min_periods=max(3, 42//4)).mean(), _s(close).rolling(1008, min_periods=max(3, 1008//4)).mean()) - 1.0

def mip_032_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_033_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_034_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(252) - _s(close).pct_change(10)

def mip_035_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_036_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(42, min_periods=max(3, 42//4)).max()) - 1.0

def mip_037_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(63, min_periods=max(3, 63//4)).min()) - 1.0

def mip_038_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(126)

def mip_039_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 252)

def mip_040_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(504, min_periods=max(3, 504//4)).median())

def mip_041_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(42, min_periods=max(3, 42//4)).mean()

def mip_042_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_043_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(1260, min_periods=max(3, 1260//4)).mean()

def mip_044_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(5, min_periods=max(3, 5//4)).skew()

def mip_045_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(10, min_periods=max(3, 10//4)).kurt()

def mip_046_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(21, min_periods=max(3, 21//4)).median())

def mip_047_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 42)

def mip_048_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 63)

def mip_049_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(252, min_periods=max(3, 252//4)).mean(), _s(close).rolling(126, min_periods=max(3, 126//4)).mean()) - 1.0

def mip_050_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_051_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_052_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(63) - _s(close).pct_change(756)

def mip_053_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_054_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(1260, min_periods=max(3, 1260//4)).max()) - 1.0

def mip_055_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(5, min_periods=max(3, 5//4)).min()) - 1.0

def mip_056_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(10)

def mip_057_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 21)

def mip_058_capitulation_signal(close, high, low, open, volume):
    return _div(volume, volume.rolling(42, min_periods=max(3, 42//4)).median())

def mip_059_capitulation_signal(close, high, low, open, volume):
    return _div(_true_range(high, low, close), close).rolling(252, min_periods=max(3, 252//4)).mean()

def mip_060_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close) - _s(open), (_s(high) - _s(low)).replace(0, np.nan))

def mip_061_capitulation_signal(close, high, low, open, volume):
    return (_s(close).pct_change() < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mip_062_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(504, min_periods=max(3, 504//4)).skew()

def mip_063_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change().rolling(756, min_periods=max(3, 756//4)).kurt()

def mip_064_capitulation_signal(close, high, low, open, volume):
    return _div(_s(volume) * _s(close), (_s(volume) * _s(close)).rolling(1008, min_periods=max(3, 1008//4)).median())

def mip_065_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(close), 1260)

def mip_066_capitulation_signal(close, high, low, open, volume):
    return _rank(_s(volume), 5)

def mip_067_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).rolling(63, min_periods=max(3, 63//4)).mean(), _s(close).rolling(10, min_periods=max(3, 10//4)).mean()) - 1.0

def mip_068_capitulation_signal(close, high, low, open, volume):
    return _div((_s(high) - _s(close)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_069_capitulation_signal(close, high, low, open, volume):
    return _div((_s(close) - _s(low)), (_s(high) - _s(low)).replace(0, np.nan))

def mip_070_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(21) - _s(close).pct_change(63)

def mip_071_capitulation_signal(close, high, low, open, volume):
    return _div(_s(close).pct_change().abs(), _div(_s(volume) * _s(close), 1.0))

def mip_072_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(252, min_periods=max(3, 252//4)).max()) - 1.0

def mip_073_capitulation_signal(close, high, low, open, volume):
    return _div(close, close.rolling(504, min_periods=max(3, 504//4)).min()) - 1.0

def mip_074_capitulation_signal(close, high, low, open, volume):
    return _s(close).pct_change(756)

def mip_075_capitulation_signal(close, high, low, open, volume):
    return _z(_s(close).pct_change(), 1008)

MARKET_IMPACT_PROXY_REGISTRY_001_075 = {
    "mip_001_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_001_capitulation_signal},
    "mip_002_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_002_capitulation_signal},
    "mip_003_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_003_capitulation_signal},
    "mip_004_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_004_capitulation_signal},
    "mip_005_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_005_capitulation_signal},
    "mip_006_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_006_capitulation_signal},
    "mip_007_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_007_capitulation_signal},
    "mip_008_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_008_capitulation_signal},
    "mip_009_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_009_capitulation_signal},
    "mip_010_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_010_capitulation_signal},
    "mip_011_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_011_capitulation_signal},
    "mip_012_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_012_capitulation_signal},
    "mip_013_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_013_capitulation_signal},
    "mip_014_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_014_capitulation_signal},
    "mip_015_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_015_capitulation_signal},
    "mip_016_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_016_capitulation_signal},
    "mip_017_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_017_capitulation_signal},
    "mip_018_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_018_capitulation_signal},
    "mip_019_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_019_capitulation_signal},
    "mip_020_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_020_capitulation_signal},
    "mip_021_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_021_capitulation_signal},
    "mip_022_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_022_capitulation_signal},
    "mip_023_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_023_capitulation_signal},
    "mip_024_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_024_capitulation_signal},
    "mip_025_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_025_capitulation_signal},
    "mip_026_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_026_capitulation_signal},
    "mip_027_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_027_capitulation_signal},
    "mip_028_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_028_capitulation_signal},
    "mip_029_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_029_capitulation_signal},
    "mip_030_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_030_capitulation_signal},
    "mip_031_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_031_capitulation_signal},
    "mip_032_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_032_capitulation_signal},
    "mip_033_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_033_capitulation_signal},
    "mip_034_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_034_capitulation_signal},
    "mip_035_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_035_capitulation_signal},
    "mip_036_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_036_capitulation_signal},
    "mip_037_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_037_capitulation_signal},
    "mip_038_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_038_capitulation_signal},
    "mip_039_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_039_capitulation_signal},
    "mip_040_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_040_capitulation_signal},
    "mip_041_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_041_capitulation_signal},
    "mip_042_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_042_capitulation_signal},
    "mip_043_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_043_capitulation_signal},
    "mip_044_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_044_capitulation_signal},
    "mip_045_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_045_capitulation_signal},
    "mip_046_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_046_capitulation_signal},
    "mip_047_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_047_capitulation_signal},
    "mip_048_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_048_capitulation_signal},
    "mip_049_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_049_capitulation_signal},
    "mip_050_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_050_capitulation_signal},
    "mip_051_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_051_capitulation_signal},
    "mip_052_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_052_capitulation_signal},
    "mip_053_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_053_capitulation_signal},
    "mip_054_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_054_capitulation_signal},
    "mip_055_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_055_capitulation_signal},
    "mip_056_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_056_capitulation_signal},
    "mip_057_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_057_capitulation_signal},
    "mip_058_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_058_capitulation_signal},
    "mip_059_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_059_capitulation_signal},
    "mip_060_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_060_capitulation_signal},
    "mip_061_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_061_capitulation_signal},
    "mip_062_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_062_capitulation_signal},
    "mip_063_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_063_capitulation_signal},
    "mip_064_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_064_capitulation_signal},
    "mip_065_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_065_capitulation_signal},
    "mip_066_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_066_capitulation_signal},
    "mip_067_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_067_capitulation_signal},
    "mip_068_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_068_capitulation_signal},
    "mip_069_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_069_capitulation_signal},
    "mip_070_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_070_capitulation_signal},
    "mip_071_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_071_capitulation_signal},
    "mip_072_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_072_capitulation_signal},
    "mip_073_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_073_capitulation_signal},
    "mip_074_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_074_capitulation_signal},
    "mip_075_capitulation_signal": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": mip_075_capitulation_signal},
}
