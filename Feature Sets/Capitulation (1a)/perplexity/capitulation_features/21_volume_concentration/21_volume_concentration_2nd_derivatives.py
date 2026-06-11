"""Generated capitulation features for 21_volume_concentration: share of volume in worst days.
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

def vcc_2d_001_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_002_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(21)).diff(), 21)

def vcc_2d_003_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_004_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(63)).diff(12)

def vcc_2d_005_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_006_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(5)).diff(), 5)

def vcc_2d_007_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_008_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(21)).diff(4)

def vcc_2d_009_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_010_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(63)).diff(), 63)

def vcc_2d_011_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_012_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)).diff(1)

def vcc_2d_013_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_014_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(21)).diff(), 21)

def vcc_2d_015_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_016_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(63)).diff(12)

def vcc_2d_017_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_018_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(5)).diff(), 5)

def vcc_2d_019_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_020_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)).diff(4)

def vcc_2d_021_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_022_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(63)).diff(), 63)

def vcc_2d_023_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_024_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(5)).diff(1)

def vcc_2d_025_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_001_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)) - (_s(high).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_002_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(10)).diff(), 10)

def vcc_2d_003_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_004_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)).diff(8)

def vcc_2d_005_distress_acceleration(close, high, low, open, volume):
    return (_s(close).diff(12)) - (_s(close).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_006_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(high).pct_change(126)).abs(), 126)

def vcc_2d_007_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(252)) - (_s(low).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_008_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(5)).diff(), 5)

def vcc_2d_009_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_010_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)).diff(4)

def vcc_2d_011_distress_acceleration(close, high, low, open, volume):
    return (_s(high).diff(8)) - (_s(high).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_012_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(low).pct_change(63)).abs(), 63)

def vcc_2d_013_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_014_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(252)).diff(), 252)

def vcc_2d_015_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_016_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)).diff(2)

def vcc_2d_017_distress_acceleration(close, high, low, open, volume):
    return (_s(low).diff(4)) - (_s(low).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_018_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(open).pct_change(42)).abs(), 42)

def vcc_2d_019_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(63)) - (_s(volume).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_020_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(126)).diff(), 126)

def vcc_2d_021_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_022_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(5)).diff(1)

def vcc_2d_023_distress_acceleration(close, high, low, open, volume):
    return (_s(open).diff(2)) - (_s(open).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_024_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(volume).pct_change(21)).abs(), 21)

def vcc_2d_025_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)) - (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_026_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(63)).diff(), 63)

def vcc_2d_027_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_028_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(252)).diff(50)

def vcc_2d_029_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).diff(1)) - (_s(volume).diff(1)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_030_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(close).pct_change(10)).abs(), 10)

def vcc_2d_031_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(21)) - (_s(high).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_032_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(42)).diff(), 42)

def vcc_2d_033_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_034_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)).diff(25)

def vcc_2d_035_distress_acceleration(close, high, low, open, volume):
    return (_s(close).diff(50)) - (_s(close).diff(50)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_036_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(high).pct_change(5)).abs(), 5)

def vcc_2d_037_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_038_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(21)).diff(), 21)

def vcc_2d_039_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_040_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(63)).diff(12)

def vcc_2d_041_distress_acceleration(close, high, low, open, volume):
    return (_s(high).diff(25)) - (_s(high).diff(25)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_042_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(low).pct_change(252)).abs(), 252)

def vcc_2d_043_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(5)) - (_s(open).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_044_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(10)).diff(), 10)

def vcc_2d_045_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_046_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)).diff(8)

def vcc_2d_047_distress_acceleration(close, high, low, open, volume):
    return (_s(low).diff(12)) - (_s(low).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_048_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(open).pct_change(126)).abs(), 126)

def vcc_2d_049_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(252)) - (_s(volume).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_050_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(5)).diff(), 5)

def vcc_2d_051_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_052_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(21)).diff(4)

def vcc_2d_053_distress_acceleration(close, high, low, open, volume):
    return (_s(open).diff(8)) - (_s(open).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_054_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(volume).pct_change(63)).abs(), 63)

def vcc_2d_055_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_056_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(252)).diff(), 252)

def vcc_2d_057_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_058_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)).diff(2)

def vcc_2d_059_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).diff(4)) - (_s(volume).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_060_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(close).pct_change(42)).abs(), 42)

def vcc_2d_061_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(63)) - (_s(high).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_062_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(126)).diff(), 126)

def vcc_2d_063_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_064_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(5)).diff(1)

def vcc_2d_065_distress_acceleration(close, high, low, open, volume):
    return (_s(close).diff(2)) - (_s(close).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_066_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(high).pct_change(21)).abs(), 21)

def vcc_2d_067_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)) - (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_068_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(63)).diff(), 63)

def vcc_2d_069_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_070_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(252)).diff(50)

def vcc_2d_071_distress_acceleration(close, high, low, open, volume):
    return (_s(high).diff(1)) - (_s(high).diff(1)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_072_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(low).pct_change(10)).abs(), 10)

def vcc_2d_073_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(21)) - (_s(open).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_074_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(42)).diff(), 42)

def vcc_2d_075_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_076_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)).diff(25)

def vcc_2d_077_distress_acceleration(close, high, low, open, volume):
    return (_s(low).diff(50)) - (_s(low).diff(50)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_078_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(open).pct_change(5)).abs(), 5)

def vcc_2d_079_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_080_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(21)).diff(), 21)

def vcc_2d_081_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_082_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(63)).diff(12)

def vcc_2d_083_distress_acceleration(close, high, low, open, volume):
    return (_s(open).diff(25)) - (_s(open).diff(25)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_084_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(volume).pct_change(252)).abs(), 252)

def vcc_2d_085_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(5)) - (_s(close).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_086_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(10)).diff(), 10)

def vcc_2d_087_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_088_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)).diff(8)

def vcc_2d_089_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).diff(12)) - (_s(volume).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_090_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(close).pct_change(126)).abs(), 126)

def vcc_2d_091_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(252)) - (_s(high).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_092_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(5)).diff(), 5)

def vcc_2d_093_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_094_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(21)).diff(4)

def vcc_2d_095_distress_acceleration(close, high, low, open, volume):
    return (_s(close).diff(8)) - (_s(close).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_096_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(high).pct_change(63)).abs(), 63)

def vcc_2d_097_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)) - (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_098_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(252)).diff(), 252)

def vcc_2d_099_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_100_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)).diff(2)

def vcc_2d_101_distress_acceleration(close, high, low, open, volume):
    return (_s(high).diff(4)) - (_s(high).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_102_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(low).pct_change(42)).abs(), 42)

def vcc_2d_103_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(63)) - (_s(open).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_104_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(126)).diff(), 126)

def vcc_2d_105_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_106_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)).diff(1)

def vcc_2d_107_distress_acceleration(close, high, low, open, volume):
    return (_s(low).diff(2)) - (_s(low).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_108_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(open).pct_change(21)).abs(), 21)

def vcc_2d_109_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_110_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(63)).diff(), 63)

def vcc_2d_111_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_112_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(252)).diff(50)

def vcc_2d_113_distress_acceleration(close, high, low, open, volume):
    return (_s(open).diff(1)) - (_s(open).diff(1)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_114_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(volume).pct_change(10)).abs(), 10)

def vcc_2d_115_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)) - (_s(close).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_116_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(42)).diff(), 42)

def vcc_2d_117_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_118_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)).diff(25)

def vcc_2d_119_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).diff(50)) - (_s(volume).diff(50)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_120_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(close).pct_change(5)).abs(), 5)

def vcc_2d_121_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)) - (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_122_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(21)).diff(), 21)

def vcc_2d_123_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_124_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(63)).diff(12)

def vcc_2d_125_distress_acceleration(close, high, low, open, volume):
    return (_s(close).diff(25)) - (_s(close).diff(25)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_126_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(high).pct_change(252)).abs(), 252)

def vcc_2d_127_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(5)) - (_s(low).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).mean()

def vcc_2d_128_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(10)).diff(), 10)

def vcc_2d_129_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(21)).rolling(21, min_periods=max(3, 21//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_130_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)).diff(8)

def vcc_2d_131_distress_acceleration(close, high, low, open, volume):
    return (_s(high).diff(12)) - (_s(high).diff(12)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_132_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(low).pct_change(126)).abs(), 126)

def vcc_2d_133_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(252)) - (_s(open).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).mean()

def vcc_2d_134_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(5)).diff(), 5)

def vcc_2d_135_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_136_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(21)).diff(4)

def vcc_2d_137_distress_acceleration(close, high, low, open, volume):
    return (_s(low).diff(8)) - (_s(low).diff(8)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_138_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(open).pct_change(63)).abs(), 63)

def vcc_2d_139_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)) - (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_140_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(252)).diff(), 252)

def vcc_2d_141_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)).rolling(5, min_periods=max(3, 5//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_142_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)).diff(2)

def vcc_2d_143_distress_acceleration(close, high, low, open, volume):
    return (_s(open).diff(4)) - (_s(open).diff(4)).rolling(21, min_periods=max(3, 21//4)).mean()

def vcc_2d_144_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(volume).pct_change(42)).abs(), 42)

def vcc_2d_145_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(63)) - (_s(close).pct_change(63)).rolling(63, min_periods=max(3, 63//4)).mean()

def vcc_2d_146_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(126)).diff(), 126)

def vcc_2d_147_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(252)).rolling(252, min_periods=max(3, 252//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_148_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(5)).diff(1)

def vcc_2d_149_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).diff(2)) - (_s(volume).diff(2)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_150_distress_acceleration(close, high, low, open, volume):
    return _rank((_s(close).pct_change(21)).abs(), 21)

def vcc_2d_001_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_002_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(21)).diff(), 21)

def vcc_2d_003_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_004_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(63)).diff(12)

def vcc_2d_005_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_006_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(5)).diff(), 5)

def vcc_2d_007_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_008_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(21)).diff(4)

def vcc_2d_009_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_010_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(63)).diff(), 63)

def vcc_2d_011_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_012_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)).diff(1)

def vcc_2d_013_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_014_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(21)).diff(), 21)

def vcc_2d_015_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_016_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(63)).diff(12)

def vcc_2d_017_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_018_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(5)).diff(), 5)

def vcc_2d_019_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_020_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)).diff(4)

def vcc_2d_021_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_022_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(63)).diff(), 63)

def vcc_2d_023_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_024_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(5)).diff(1)

def vcc_2d_025_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_026_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(21)).diff(), 21)

def vcc_2d_027_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_028_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(63)).diff(12)

def vcc_2d_029_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_030_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(5)).diff(), 5)

def vcc_2d_031_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_032_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(21)).diff(4)

def vcc_2d_033_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)) - (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_034_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(63)).diff(), 63)

def vcc_2d_035_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_036_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(5)).diff(1)

def vcc_2d_037_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)) - (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_038_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(21)).diff(), 21)

def vcc_2d_039_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_040_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(63)).diff(12)

def vcc_2d_041_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)) - (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_042_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(5)).diff(), 5)

def vcc_2d_043_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_044_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(21)).diff(4)

def vcc_2d_045_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)) - (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_046_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(63)).diff(), 63)

def vcc_2d_047_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_048_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(5)).diff(1)

def vcc_2d_049_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)) - (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_050_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(21)).diff(), 21)

def vcc_2d_051_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_052_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(63)).diff(12)

def vcc_2d_053_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)) - (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_054_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(5)).diff(), 5)

def vcc_2d_055_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_056_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(21)).diff(4)

def vcc_2d_057_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)) - (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_058_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(63)).diff(), 63)

def vcc_2d_059_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_060_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(5)).diff(1)

def vcc_2d_061_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_062_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(21)).diff(), 21)

def vcc_2d_063_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_064_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(63)).diff(12)

def vcc_2d_065_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_066_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(5)).diff(), 5)

def vcc_2d_067_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_068_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(21)).diff(4)

def vcc_2d_069_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_070_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(63)).diff(), 63)

def vcc_2d_071_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_072_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)).diff(1)

def vcc_2d_073_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_074_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(21)).diff(), 21)

def vcc_2d_075_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_076_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(63)).diff(12)

def vcc_2d_077_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_078_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(5)).diff(), 5)

def vcc_2d_079_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_080_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)).diff(4)

def vcc_2d_081_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_082_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(63)).diff(), 63)

def vcc_2d_083_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_084_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(5)).diff(1)

def vcc_2d_085_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_086_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(21)).diff(), 21)

def vcc_2d_087_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_088_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(63)).diff(12)

def vcc_2d_089_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_090_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(5)).diff(), 5)

def vcc_2d_091_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_092_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(21)).diff(4)

def vcc_2d_093_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)) - (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_094_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(63)).diff(), 63)

def vcc_2d_095_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_096_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(5)).diff(1)

def vcc_2d_097_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)) - (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_098_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(21)).diff(), 21)

def vcc_2d_099_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_100_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(63)).diff(12)

def vcc_2d_101_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)) - (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_102_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(5)).diff(), 5)

def vcc_2d_103_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_104_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(21)).diff(4)

def vcc_2d_105_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)) - (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_106_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(63)).diff(), 63)

def vcc_2d_107_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_108_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(5)).diff(1)

def vcc_2d_109_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)) - (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_110_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(21)).diff(), 21)

def vcc_2d_111_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_112_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(63)).diff(12)

def vcc_2d_113_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)) - (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_114_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(5)).diff(), 5)

def vcc_2d_115_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_116_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(21)).diff(4)

def vcc_2d_117_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)) - (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_118_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(63)).diff(), 63)

def vcc_2d_119_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_120_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(5)).diff(1)

def vcc_2d_121_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(10)) - (_s(volume).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_122_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(21)).diff(), 21)

def vcc_2d_123_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_124_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(63)).diff(12)

def vcc_2d_125_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(126)) - (_s(close).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_126_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(5)).diff(), 5)

def vcc_2d_127_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_128_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(21)).diff(4)

def vcc_2d_129_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(42)) - (_s(open).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_130_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(63)).diff(), 63)

def vcc_2d_131_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_132_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(5)).diff(1)

def vcc_2d_133_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(10)) - (_s(low).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_134_distress_acceleration(close, high, low, open, volume):
    return _z((_s(open).pct_change(21)).diff(), 21)

def vcc_2d_135_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_136_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(63)).diff(12)

def vcc_2d_137_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(126)) - (_s(high).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_138_distress_acceleration(close, high, low, open, volume):
    return _z((_s(low).pct_change(5)).diff(), 5)

def vcc_2d_139_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_140_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(21)).diff(4)

def vcc_2d_141_distress_acceleration(close, high, low, open, volume):
    return (_s(volume).pct_change(42)) - (_s(volume).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).mean()

def vcc_2d_142_distress_acceleration(close, high, low, open, volume):
    return _z((_s(high).pct_change(63)).diff(), 63)

def vcc_2d_143_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_144_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(5)).diff(1)

def vcc_2d_145_distress_acceleration(close, high, low, open, volume):
    return (_s(close).pct_change(10)) - (_s(close).pct_change(10)).rolling(10, min_periods=max(3, 10//4)).mean()

def vcc_2d_146_distress_acceleration(close, high, low, open, volume):
    return _z((_s(volume).pct_change(21)).diff(), 21)

def vcc_2d_147_distress_acceleration(close, high, low, open, volume):
    return (_s(high).pct_change(42)).rolling(42, min_periods=max(3, 42//4)).apply(lambda x: x.iloc[-1] - x.iloc[0], raw=False)

def vcc_2d_148_distress_acceleration(close, high, low, open, volume):
    return (_s(low).pct_change(63)).diff(12)

def vcc_2d_149_distress_acceleration(close, high, low, open, volume):
    return (_s(open).pct_change(126)) - (_s(open).pct_change(126)).rolling(126, min_periods=max(3, 126//4)).mean()

def vcc_2d_150_distress_acceleration(close, high, low, open, volume):
    return _z((_s(close).pct_change(5)).diff(), 5)

VOLUME_CONCENTRATION_REGISTRY_2ND_DERIVATIVES = {
    "vcc_2d_001_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_001_distress_acceleration},
    "vcc_2d_002_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_002_distress_acceleration},
    "vcc_2d_003_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_003_distress_acceleration},
    "vcc_2d_004_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_004_distress_acceleration},
    "vcc_2d_005_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_005_distress_acceleration},
    "vcc_2d_006_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_006_distress_acceleration},
    "vcc_2d_007_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_007_distress_acceleration},
    "vcc_2d_008_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_008_distress_acceleration},
    "vcc_2d_009_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_009_distress_acceleration},
    "vcc_2d_010_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_010_distress_acceleration},
    "vcc_2d_011_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_011_distress_acceleration},
    "vcc_2d_012_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_012_distress_acceleration},
    "vcc_2d_013_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_013_distress_acceleration},
    "vcc_2d_014_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_014_distress_acceleration},
    "vcc_2d_015_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_015_distress_acceleration},
    "vcc_2d_016_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_016_distress_acceleration},
    "vcc_2d_017_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_017_distress_acceleration},
    "vcc_2d_018_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_018_distress_acceleration},
    "vcc_2d_019_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_019_distress_acceleration},
    "vcc_2d_020_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_020_distress_acceleration},
    "vcc_2d_021_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_021_distress_acceleration},
    "vcc_2d_022_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_022_distress_acceleration},
    "vcc_2d_023_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_023_distress_acceleration},
    "vcc_2d_024_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_024_distress_acceleration},
    "vcc_2d_025_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_025_distress_acceleration},
    "vcc_2d_026_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_026_distress_acceleration},
    "vcc_2d_027_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_027_distress_acceleration},
    "vcc_2d_028_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_028_distress_acceleration},
    "vcc_2d_029_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_029_distress_acceleration},
    "vcc_2d_030_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_030_distress_acceleration},
    "vcc_2d_031_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_031_distress_acceleration},
    "vcc_2d_032_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_032_distress_acceleration},
    "vcc_2d_033_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_033_distress_acceleration},
    "vcc_2d_034_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_034_distress_acceleration},
    "vcc_2d_035_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_035_distress_acceleration},
    "vcc_2d_036_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_036_distress_acceleration},
    "vcc_2d_037_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_037_distress_acceleration},
    "vcc_2d_038_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_038_distress_acceleration},
    "vcc_2d_039_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_039_distress_acceleration},
    "vcc_2d_040_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_040_distress_acceleration},
    "vcc_2d_041_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_041_distress_acceleration},
    "vcc_2d_042_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_042_distress_acceleration},
    "vcc_2d_043_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_043_distress_acceleration},
    "vcc_2d_044_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_044_distress_acceleration},
    "vcc_2d_045_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_045_distress_acceleration},
    "vcc_2d_046_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_046_distress_acceleration},
    "vcc_2d_047_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_047_distress_acceleration},
    "vcc_2d_048_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_048_distress_acceleration},
    "vcc_2d_049_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_049_distress_acceleration},
    "vcc_2d_050_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_050_distress_acceleration},
    "vcc_2d_051_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_051_distress_acceleration},
    "vcc_2d_052_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_052_distress_acceleration},
    "vcc_2d_053_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_053_distress_acceleration},
    "vcc_2d_054_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_054_distress_acceleration},
    "vcc_2d_055_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_055_distress_acceleration},
    "vcc_2d_056_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_056_distress_acceleration},
    "vcc_2d_057_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_057_distress_acceleration},
    "vcc_2d_058_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_058_distress_acceleration},
    "vcc_2d_059_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_059_distress_acceleration},
    "vcc_2d_060_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_060_distress_acceleration},
    "vcc_2d_061_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_061_distress_acceleration},
    "vcc_2d_062_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_062_distress_acceleration},
    "vcc_2d_063_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_063_distress_acceleration},
    "vcc_2d_064_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_064_distress_acceleration},
    "vcc_2d_065_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_065_distress_acceleration},
    "vcc_2d_066_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_066_distress_acceleration},
    "vcc_2d_067_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_067_distress_acceleration},
    "vcc_2d_068_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_068_distress_acceleration},
    "vcc_2d_069_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_069_distress_acceleration},
    "vcc_2d_070_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_070_distress_acceleration},
    "vcc_2d_071_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_071_distress_acceleration},
    "vcc_2d_072_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_072_distress_acceleration},
    "vcc_2d_073_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_073_distress_acceleration},
    "vcc_2d_074_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_074_distress_acceleration},
    "vcc_2d_075_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_075_distress_acceleration},
    "vcc_2d_076_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_076_distress_acceleration},
    "vcc_2d_077_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_077_distress_acceleration},
    "vcc_2d_078_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_078_distress_acceleration},
    "vcc_2d_079_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_079_distress_acceleration},
    "vcc_2d_080_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_080_distress_acceleration},
    "vcc_2d_081_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_081_distress_acceleration},
    "vcc_2d_082_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_082_distress_acceleration},
    "vcc_2d_083_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_083_distress_acceleration},
    "vcc_2d_084_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_084_distress_acceleration},
    "vcc_2d_085_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_085_distress_acceleration},
    "vcc_2d_086_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_086_distress_acceleration},
    "vcc_2d_087_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_087_distress_acceleration},
    "vcc_2d_088_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_088_distress_acceleration},
    "vcc_2d_089_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_089_distress_acceleration},
    "vcc_2d_090_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_090_distress_acceleration},
    "vcc_2d_091_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_091_distress_acceleration},
    "vcc_2d_092_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_092_distress_acceleration},
    "vcc_2d_093_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_093_distress_acceleration},
    "vcc_2d_094_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_094_distress_acceleration},
    "vcc_2d_095_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_095_distress_acceleration},
    "vcc_2d_096_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_096_distress_acceleration},
    "vcc_2d_097_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_097_distress_acceleration},
    "vcc_2d_098_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_098_distress_acceleration},
    "vcc_2d_099_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_099_distress_acceleration},
    "vcc_2d_100_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_100_distress_acceleration},
    "vcc_2d_101_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_101_distress_acceleration},
    "vcc_2d_102_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_102_distress_acceleration},
    "vcc_2d_103_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_103_distress_acceleration},
    "vcc_2d_104_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_104_distress_acceleration},
    "vcc_2d_105_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_105_distress_acceleration},
    "vcc_2d_106_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_106_distress_acceleration},
    "vcc_2d_107_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_107_distress_acceleration},
    "vcc_2d_108_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_108_distress_acceleration},
    "vcc_2d_109_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_109_distress_acceleration},
    "vcc_2d_110_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_110_distress_acceleration},
    "vcc_2d_111_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_111_distress_acceleration},
    "vcc_2d_112_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_112_distress_acceleration},
    "vcc_2d_113_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_113_distress_acceleration},
    "vcc_2d_114_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_114_distress_acceleration},
    "vcc_2d_115_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_115_distress_acceleration},
    "vcc_2d_116_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_116_distress_acceleration},
    "vcc_2d_117_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_117_distress_acceleration},
    "vcc_2d_118_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_118_distress_acceleration},
    "vcc_2d_119_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_119_distress_acceleration},
    "vcc_2d_120_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_120_distress_acceleration},
    "vcc_2d_121_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_121_distress_acceleration},
    "vcc_2d_122_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_122_distress_acceleration},
    "vcc_2d_123_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_123_distress_acceleration},
    "vcc_2d_124_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_124_distress_acceleration},
    "vcc_2d_125_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_125_distress_acceleration},
    "vcc_2d_126_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_126_distress_acceleration},
    "vcc_2d_127_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_127_distress_acceleration},
    "vcc_2d_128_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_128_distress_acceleration},
    "vcc_2d_129_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_129_distress_acceleration},
    "vcc_2d_130_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_130_distress_acceleration},
    "vcc_2d_131_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_131_distress_acceleration},
    "vcc_2d_132_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_132_distress_acceleration},
    "vcc_2d_133_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_133_distress_acceleration},
    "vcc_2d_134_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_134_distress_acceleration},
    "vcc_2d_135_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_135_distress_acceleration},
    "vcc_2d_136_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_136_distress_acceleration},
    "vcc_2d_137_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_137_distress_acceleration},
    "vcc_2d_138_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_138_distress_acceleration},
    "vcc_2d_139_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_139_distress_acceleration},
    "vcc_2d_140_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_140_distress_acceleration},
    "vcc_2d_141_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_141_distress_acceleration},
    "vcc_2d_142_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_142_distress_acceleration},
    "vcc_2d_143_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_143_distress_acceleration},
    "vcc_2d_144_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_144_distress_acceleration},
    "vcc_2d_145_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_145_distress_acceleration},
    "vcc_2d_146_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_146_distress_acceleration},
    "vcc_2d_147_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_147_distress_acceleration},
    "vcc_2d_148_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_148_distress_acceleration},
    "vcc_2d_149_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_149_distress_acceleration},
    "vcc_2d_150_distress_acceleration": {"inputs": ['close', 'high', 'low', 'open', 'volume'], "func": vcc_2d_150_distress_acceleration},
}
