"""Generated capitulation features for 06_low_proximity: closeness to trailing min, new-low frequency.
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

def lp_3d_001_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_002_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_003_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_004_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_005_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_006_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_007_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_008_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_009_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_010_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_011_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_012_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_013_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_014_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_015_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_016_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_017_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_018_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_019_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_020_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_021_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_022_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_023_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_024_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_025_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_001_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)) - (_s(high).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff()

def lp_3d_002_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(10)).diff(), 10)
    return d2 - d2.rolling(10, min_periods=max(3, 10//4)).mean()

def lp_3d_003_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(4)

def lp_3d_004_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)).diff(8)
    return _z(d2.diff(), 42)

def lp_3d_005_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).diff(12)) - (_s(close).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff()

def lp_3d_006_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(high).pct_change(126)).abs(), 126)
    return d2 - d2.rolling(126, min_periods=max(3, 126//4)).mean()

def lp_3d_007_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(252)) - (_s(low).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff(50)

def lp_3d_008_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(5)).diff(), 5)
    return _z(d2.diff(), 5)

def lp_3d_009_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_010_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)).diff(4)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_011_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).diff(8)) - (_s(high).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff(8)

def lp_3d_012_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(low).pct_change(63)).abs(), 63)
    return _z(d2.diff(), 63)

def lp_3d_013_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_014_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(252)).diff(), 252)
    return d2 - d2.rolling(252, min_periods=max(3, 252//4)).mean()

def lp_3d_015_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(1)

def lp_3d_016_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)).diff(2)
    return _z(d2.diff(), 10)

def lp_3d_017_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).diff(4)) - (_s(low).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff()

def lp_3d_018_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(open).pct_change(42)).abs(), 42)
    return d2 - d2.rolling(42, min_periods=max(3, 42//4)).mean()

def lp_3d_019_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(63)) - (_s(volume).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff(12)

def lp_3d_020_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(126)).diff(), 126)
    return _z(d2.diff(), 126)

def lp_3d_021_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_022_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(5)).diff(1)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_023_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).diff(2)) - (_s(open).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff(2)

def lp_3d_024_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(volume).pct_change(21)).abs(), 21)
    return _z(d2.diff(), 21)

def lp_3d_025_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)) - (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_026_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_027_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_028_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(252)).diff(50)
    return _z(d2.diff(), 252)

def lp_3d_029_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).diff(1)) - (_s(volume).diff(1)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff()

def lp_3d_030_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(close).pct_change(10)).abs(), 10)
    return d2 - d2.rolling(10, min_periods=max(3, 10//4)).mean()

def lp_3d_031_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(21)) - (_s(high).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff(4)

def lp_3d_032_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(42)).diff(), 42)
    return _z(d2.diff(), 42)

def lp_3d_033_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_034_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)).diff(25)
    return d2 - d2.rolling(126, min_periods=max(3, 126//4)).mean()

def lp_3d_035_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).diff(50)) - (_s(close).diff(50)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff(50)

def lp_3d_036_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(high).pct_change(5)).abs(), 5)
    return _z(d2.diff(), 5)

def lp_3d_037_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_038_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_039_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_040_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(63)).diff(12)
    return _z(d2.diff(), 63)

def lp_3d_041_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).diff(25)) - (_s(high).diff(25)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_042_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(low).pct_change(252)).abs(), 252)
    return d2 - d2.rolling(252, min_periods=max(3, 252//4)).mean()

def lp_3d_043_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(5)) - (_s(open).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff(1)

def lp_3d_044_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(10)).diff(), 10)
    return _z(d2.diff(), 10)

def lp_3d_045_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_046_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)).diff(8)
    return d2 - d2.rolling(42, min_periods=max(3, 42//4)).mean()

def lp_3d_047_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).diff(12)) - (_s(low).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff(12)

def lp_3d_048_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(open).pct_change(126)).abs(), 126)
    return _z(d2.diff(), 126)

def lp_3d_049_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(252)) - (_s(volume).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff()

def lp_3d_050_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_051_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_052_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(21)).diff(4)
    return _z(d2.diff(), 21)

def lp_3d_053_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).diff(8)) - (_s(open).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_054_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(volume).pct_change(63)).abs(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_055_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff(25)

def lp_3d_056_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(252)).diff(), 252)
    return _z(d2.diff(), 252)

def lp_3d_057_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_058_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)).diff(2)
    return d2 - d2.rolling(10, min_periods=max(3, 10//4)).mean()

def lp_3d_059_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).diff(4)) - (_s(volume).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff(4)

def lp_3d_060_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(close).pct_change(42)).abs(), 42)
    return _z(d2.diff(), 42)

def lp_3d_061_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(63)) - (_s(high).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff()

def lp_3d_062_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(126)).diff(), 126)
    return d2 - d2.rolling(126, min_periods=max(3, 126//4)).mean()

def lp_3d_063_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(50)

def lp_3d_064_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(5)).diff(1)
    return _z(d2.diff(), 5)

def lp_3d_065_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).diff(2)) - (_s(close).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_066_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(high).pct_change(21)).abs(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_067_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)) - (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff(8)

def lp_3d_068_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(63)).diff(), 63)
    return _z(d2.diff(), 63)

def lp_3d_069_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_070_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(252)).diff(50)
    return d2 - d2.rolling(252, min_periods=max(3, 252//4)).mean()

def lp_3d_071_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).diff(1)) - (_s(high).diff(1)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff(1)

def lp_3d_072_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(low).pct_change(10)).abs(), 10)
    return _z(d2.diff(), 10)

def lp_3d_073_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(21)) - (_s(open).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff()

def lp_3d_074_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(42)).diff(), 42)
    return d2 - d2.rolling(42, min_periods=max(3, 42//4)).mean()

def lp_3d_075_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(12)

def lp_3d_076_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)).diff(25)
    return _z(d2.diff(), 126)

def lp_3d_077_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).diff(50)) - (_s(low).diff(50)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff()

def lp_3d_078_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(open).pct_change(5)).abs(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_079_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff(2)

def lp_3d_080_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(21)).diff(), 21)
    return _z(d2.diff(), 21)

def lp_3d_081_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_082_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(63)).diff(12)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_083_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).diff(25)) - (_s(open).diff(25)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff(25)

def lp_3d_084_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(volume).pct_change(252)).abs(), 252)
    return _z(d2.diff(), 252)

def lp_3d_085_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(5)) - (_s(close).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff()

def lp_3d_086_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(10)).diff(), 10)
    return d2 - d2.rolling(10, min_periods=max(3, 10//4)).mean()

def lp_3d_087_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(4)

def lp_3d_088_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)).diff(8)
    return _z(d2.diff(), 42)

def lp_3d_089_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).diff(12)) - (_s(volume).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff()

def lp_3d_090_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(close).pct_change(126)).abs(), 126)
    return d2 - d2.rolling(126, min_periods=max(3, 126//4)).mean()

def lp_3d_091_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(252)) - (_s(high).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff(50)

def lp_3d_092_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(5)).diff(), 5)
    return _z(d2.diff(), 5)

def lp_3d_093_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_094_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(21)).diff(4)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_095_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).diff(8)) - (_s(close).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff(8)

def lp_3d_096_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(high).pct_change(63)).abs(), 63)
    return _z(d2.diff(), 63)

def lp_3d_097_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)) - (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_098_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(252)).diff(), 252)
    return d2 - d2.rolling(252, min_periods=max(3, 252//4)).mean()

def lp_3d_099_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(1)

def lp_3d_100_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)).diff(2)
    return _z(d2.diff(), 10)

def lp_3d_101_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).diff(4)) - (_s(high).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff()

def lp_3d_102_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(low).pct_change(42)).abs(), 42)
    return d2 - d2.rolling(42, min_periods=max(3, 42//4)).mean()

def lp_3d_103_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(63)) - (_s(open).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff(12)

def lp_3d_104_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(126)).diff(), 126)
    return _z(d2.diff(), 126)

def lp_3d_105_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_106_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)).diff(1)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_107_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).diff(2)) - (_s(low).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff(2)

def lp_3d_108_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(open).pct_change(21)).abs(), 21)
    return _z(d2.diff(), 21)

def lp_3d_109_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_110_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_111_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_112_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(252)).diff(50)
    return _z(d2.diff(), 252)

def lp_3d_113_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).diff(1)) - (_s(open).diff(1)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff()

def lp_3d_114_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(volume).pct_change(10)).abs(), 10)
    return d2 - d2.rolling(10, min_periods=max(3, 10//4)).mean()

def lp_3d_115_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)) - (_s(close).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff(4)

def lp_3d_116_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(42)).diff(), 42)
    return _z(d2.diff(), 42)

def lp_3d_117_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_118_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)).diff(25)
    return d2 - d2.rolling(126, min_periods=max(3, 126//4)).mean()

def lp_3d_119_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).diff(50)) - (_s(volume).diff(50)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff(50)

def lp_3d_120_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(close).pct_change(5)).abs(), 5)
    return _z(d2.diff(), 5)

def lp_3d_121_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)) - (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_122_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_123_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_124_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(63)).diff(12)
    return _z(d2.diff(), 63)

def lp_3d_125_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).diff(25)) - (_s(close).diff(25)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_126_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(high).pct_change(252)).abs(), 252)
    return d2 - d2.rolling(252, min_periods=max(3, 252//4)).mean()

def lp_3d_127_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(5)) - (_s(low).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()
    return d2.diff(1)

def lp_3d_128_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(10)).diff(), 10)
    return _z(d2.diff(), 10)

def lp_3d_129_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_130_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)).diff(8)
    return d2 - d2.rolling(42, min_periods=max(3, 42//4)).mean()

def lp_3d_131_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).diff(12)) - (_s(high).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff(12)

def lp_3d_132_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(low).pct_change(126)).abs(), 126)
    return _z(d2.diff(), 126)

def lp_3d_133_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(252)) - (_s(open).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()
    return d2.diff()

def lp_3d_134_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_135_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_136_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(21)).diff(4)
    return _z(d2.diff(), 21)

def lp_3d_137_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).diff(8)) - (_s(low).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_138_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(open).pct_change(63)).abs(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_139_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)) - (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff(25)

def lp_3d_140_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(252)).diff(), 252)
    return _z(d2.diff(), 252)

def lp_3d_141_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff()

def lp_3d_142_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)).diff(2)
    return d2 - d2.rolling(10, min_periods=max(3, 10//4)).mean()

def lp_3d_143_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).diff(4)) - (_s(open).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()
    return d2.diff(4)

def lp_3d_144_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(volume).pct_change(42)).abs(), 42)
    return _z(d2.diff(), 42)

def lp_3d_145_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(63)) - (_s(close).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()
    return d2.diff()

def lp_3d_146_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(126)).diff(), 126)
    return d2 - d2.rolling(126, min_periods=max(3, 126//4)).mean()

def lp_3d_147_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(50)

def lp_3d_148_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(5)).diff(1)
    return _z(d2.diff(), 5)

def lp_3d_149_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).diff(2)) - (_s(volume).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_150_exhaustion_inflection(close, high, low, open, volume):
    d2 = _rank((_s(close).pct_change(21)).abs(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_001_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_002_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_003_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_004_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_005_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_006_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_007_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_008_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_009_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_010_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_011_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_012_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_013_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_014_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_015_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_016_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_017_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_018_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_019_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_020_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_021_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_022_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_023_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_024_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_025_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_026_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_027_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_028_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_029_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_030_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_031_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_032_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_033_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)) - (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_034_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_035_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_036_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_037_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)) - (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_038_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_039_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_040_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_041_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)) - (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_042_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_043_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_044_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_045_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)) - (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_046_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_047_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_048_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_049_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)) - (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_050_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_051_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_052_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_053_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)) - (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_054_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_055_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_056_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_057_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)) - (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_058_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_059_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_060_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_061_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_062_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_063_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_064_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_065_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_066_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_067_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_068_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_069_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_070_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_071_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_072_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_073_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_074_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_075_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_076_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_077_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_078_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_079_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_080_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_081_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_082_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_083_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_084_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_085_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_086_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_087_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_088_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_089_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_090_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_091_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_092_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_093_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)) - (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_094_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_095_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_096_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_097_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)) - (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_098_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_099_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_100_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_101_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)) - (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_102_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_103_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_104_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_105_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)) - (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_106_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_107_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_108_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_109_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)) - (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_110_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_111_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_112_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_113_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)) - (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_114_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_115_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_116_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_117_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)) - (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_118_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_119_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_120_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_121_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_122_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_123_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_124_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_125_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_126_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_127_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_128_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_129_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_130_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_131_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_132_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_133_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_134_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(open).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_135_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_136_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_137_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_138_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(low).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

def lp_3d_139_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(2)

def lp_3d_140_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(21)).diff(4)
    return d2.diff(4)

def lp_3d_141_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()
    return d2.diff()

def lp_3d_142_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(high).pct_change(63)).diff(), 63)
    return d2 - d2.rolling(63, min_periods=max(3, 63//4)).mean()

def lp_3d_143_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(25)

def lp_3d_144_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(5)).diff(1)
    return d2.diff(1)

def lp_3d_145_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()
    return d2.diff()

def lp_3d_146_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(volume).pct_change(21)).diff(), 21)
    return d2 - d2.rolling(21, min_periods=max(3, 21//4)).mean()

def lp_3d_147_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)
    return d2.diff(8)

def lp_3d_148_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(low).pct_change(63)).diff(12)
    return d2.diff(12)

def lp_3d_149_exhaustion_inflection(close, high, low, open, volume):
    d2 = (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()
    return d2.diff()

def lp_3d_150_exhaustion_inflection(close, high, low, open, volume):
    d2 = _z((_s(close).pct_change(5)).diff(), 5)
    return d2 - d2.rolling(5, min_periods=max(3, 5//4)).mean()

LOW_PROXIMITY_REGISTRY_3RD_DERIVATIVES = {
    "lp_3d_001_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_001_exhaustion_inflection},
    "lp_3d_002_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_002_exhaustion_inflection},
    "lp_3d_003_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_003_exhaustion_inflection},
    "lp_3d_004_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_004_exhaustion_inflection},
    "lp_3d_005_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_005_exhaustion_inflection},
    "lp_3d_006_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_006_exhaustion_inflection},
    "lp_3d_007_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_007_exhaustion_inflection},
    "lp_3d_008_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_008_exhaustion_inflection},
    "lp_3d_009_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_009_exhaustion_inflection},
    "lp_3d_010_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_010_exhaustion_inflection},
    "lp_3d_011_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_011_exhaustion_inflection},
    "lp_3d_012_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_012_exhaustion_inflection},
    "lp_3d_013_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_013_exhaustion_inflection},
    "lp_3d_014_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_014_exhaustion_inflection},
    "lp_3d_015_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_015_exhaustion_inflection},
    "lp_3d_016_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_016_exhaustion_inflection},
    "lp_3d_017_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_017_exhaustion_inflection},
    "lp_3d_018_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_018_exhaustion_inflection},
    "lp_3d_019_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_019_exhaustion_inflection},
    "lp_3d_020_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_020_exhaustion_inflection},
    "lp_3d_021_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_021_exhaustion_inflection},
    "lp_3d_022_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_022_exhaustion_inflection},
    "lp_3d_023_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_023_exhaustion_inflection},
    "lp_3d_024_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_024_exhaustion_inflection},
    "lp_3d_025_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_025_exhaustion_inflection},
    "lp_3d_026_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_026_exhaustion_inflection},
    "lp_3d_027_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_027_exhaustion_inflection},
    "lp_3d_028_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_028_exhaustion_inflection},
    "lp_3d_029_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_029_exhaustion_inflection},
    "lp_3d_030_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_030_exhaustion_inflection},
    "lp_3d_031_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_031_exhaustion_inflection},
    "lp_3d_032_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_032_exhaustion_inflection},
    "lp_3d_033_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_033_exhaustion_inflection},
    "lp_3d_034_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_034_exhaustion_inflection},
    "lp_3d_035_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_035_exhaustion_inflection},
    "lp_3d_036_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_036_exhaustion_inflection},
    "lp_3d_037_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_037_exhaustion_inflection},
    "lp_3d_038_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_038_exhaustion_inflection},
    "lp_3d_039_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_039_exhaustion_inflection},
    "lp_3d_040_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_040_exhaustion_inflection},
    "lp_3d_041_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_041_exhaustion_inflection},
    "lp_3d_042_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_042_exhaustion_inflection},
    "lp_3d_043_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_043_exhaustion_inflection},
    "lp_3d_044_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_044_exhaustion_inflection},
    "lp_3d_045_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_045_exhaustion_inflection},
    "lp_3d_046_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_046_exhaustion_inflection},
    "lp_3d_047_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_047_exhaustion_inflection},
    "lp_3d_048_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_048_exhaustion_inflection},
    "lp_3d_049_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_049_exhaustion_inflection},
    "lp_3d_050_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_050_exhaustion_inflection},
    "lp_3d_051_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_051_exhaustion_inflection},
    "lp_3d_052_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_052_exhaustion_inflection},
    "lp_3d_053_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_053_exhaustion_inflection},
    "lp_3d_054_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_054_exhaustion_inflection},
    "lp_3d_055_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_055_exhaustion_inflection},
    "lp_3d_056_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_056_exhaustion_inflection},
    "lp_3d_057_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_057_exhaustion_inflection},
    "lp_3d_058_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_058_exhaustion_inflection},
    "lp_3d_059_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_059_exhaustion_inflection},
    "lp_3d_060_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_060_exhaustion_inflection},
    "lp_3d_061_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_061_exhaustion_inflection},
    "lp_3d_062_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_062_exhaustion_inflection},
    "lp_3d_063_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_063_exhaustion_inflection},
    "lp_3d_064_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_064_exhaustion_inflection},
    "lp_3d_065_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_065_exhaustion_inflection},
    "lp_3d_066_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_066_exhaustion_inflection},
    "lp_3d_067_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_067_exhaustion_inflection},
    "lp_3d_068_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_068_exhaustion_inflection},
    "lp_3d_069_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_069_exhaustion_inflection},
    "lp_3d_070_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_070_exhaustion_inflection},
    "lp_3d_071_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_071_exhaustion_inflection},
    "lp_3d_072_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_072_exhaustion_inflection},
    "lp_3d_073_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_073_exhaustion_inflection},
    "lp_3d_074_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_074_exhaustion_inflection},
    "lp_3d_075_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_075_exhaustion_inflection},
    "lp_3d_076_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_076_exhaustion_inflection},
    "lp_3d_077_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_077_exhaustion_inflection},
    "lp_3d_078_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_078_exhaustion_inflection},
    "lp_3d_079_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_079_exhaustion_inflection},
    "lp_3d_080_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_080_exhaustion_inflection},
    "lp_3d_081_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_081_exhaustion_inflection},
    "lp_3d_082_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_082_exhaustion_inflection},
    "lp_3d_083_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_083_exhaustion_inflection},
    "lp_3d_084_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_084_exhaustion_inflection},
    "lp_3d_085_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_085_exhaustion_inflection},
    "lp_3d_086_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_086_exhaustion_inflection},
    "lp_3d_087_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_087_exhaustion_inflection},
    "lp_3d_088_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_088_exhaustion_inflection},
    "lp_3d_089_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_089_exhaustion_inflection},
    "lp_3d_090_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_090_exhaustion_inflection},
    "lp_3d_091_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_091_exhaustion_inflection},
    "lp_3d_092_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_092_exhaustion_inflection},
    "lp_3d_093_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_093_exhaustion_inflection},
    "lp_3d_094_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_094_exhaustion_inflection},
    "lp_3d_095_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_095_exhaustion_inflection},
    "lp_3d_096_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_096_exhaustion_inflection},
    "lp_3d_097_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_097_exhaustion_inflection},
    "lp_3d_098_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_098_exhaustion_inflection},
    "lp_3d_099_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_099_exhaustion_inflection},
    "lp_3d_100_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_100_exhaustion_inflection},
    "lp_3d_101_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_101_exhaustion_inflection},
    "lp_3d_102_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_102_exhaustion_inflection},
    "lp_3d_103_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_103_exhaustion_inflection},
    "lp_3d_104_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_104_exhaustion_inflection},
    "lp_3d_105_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_105_exhaustion_inflection},
    "lp_3d_106_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_106_exhaustion_inflection},
    "lp_3d_107_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_107_exhaustion_inflection},
    "lp_3d_108_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_108_exhaustion_inflection},
    "lp_3d_109_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_109_exhaustion_inflection},
    "lp_3d_110_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_110_exhaustion_inflection},
    "lp_3d_111_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_111_exhaustion_inflection},
    "lp_3d_112_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_112_exhaustion_inflection},
    "lp_3d_113_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_113_exhaustion_inflection},
    "lp_3d_114_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_114_exhaustion_inflection},
    "lp_3d_115_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_115_exhaustion_inflection},
    "lp_3d_116_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_116_exhaustion_inflection},
    "lp_3d_117_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_117_exhaustion_inflection},
    "lp_3d_118_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_118_exhaustion_inflection},
    "lp_3d_119_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_119_exhaustion_inflection},
    "lp_3d_120_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_120_exhaustion_inflection},
    "lp_3d_121_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_121_exhaustion_inflection},
    "lp_3d_122_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_122_exhaustion_inflection},
    "lp_3d_123_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_123_exhaustion_inflection},
    "lp_3d_124_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_124_exhaustion_inflection},
    "lp_3d_125_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_125_exhaustion_inflection},
    "lp_3d_126_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_126_exhaustion_inflection},
    "lp_3d_127_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_127_exhaustion_inflection},
    "lp_3d_128_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_128_exhaustion_inflection},
    "lp_3d_129_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_129_exhaustion_inflection},
    "lp_3d_130_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_130_exhaustion_inflection},
    "lp_3d_131_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_131_exhaustion_inflection},
    "lp_3d_132_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_132_exhaustion_inflection},
    "lp_3d_133_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_133_exhaustion_inflection},
    "lp_3d_134_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_134_exhaustion_inflection},
    "lp_3d_135_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_135_exhaustion_inflection},
    "lp_3d_136_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_136_exhaustion_inflection},
    "lp_3d_137_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_137_exhaustion_inflection},
    "lp_3d_138_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_138_exhaustion_inflection},
    "lp_3d_139_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_139_exhaustion_inflection},
    "lp_3d_140_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_140_exhaustion_inflection},
    "lp_3d_141_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_141_exhaustion_inflection},
    "lp_3d_142_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_142_exhaustion_inflection},
    "lp_3d_143_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_143_exhaustion_inflection},
    "lp_3d_144_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_144_exhaustion_inflection},
    "lp_3d_145_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_145_exhaustion_inflection},
    "lp_3d_146_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_146_exhaustion_inflection},
    "lp_3d_147_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_147_exhaustion_inflection},
    "lp_3d_148_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_148_exhaustion_inflection},
    "lp_3d_149_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_149_exhaustion_inflection},
    "lp_3d_150_exhaustion_inflection": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": lp_3d_150_exhaustion_inflection},
}
