"""Generated capitulation features for 70_dilution_acceleration: share count growth.
All windows look backward only. Trading-day constants: 252/year, 63/quarter, 21/month, 5/week.
"""
import numpy as np
import pandas as pd


def _align_to_close(s, close):
    s = pd.Series(s).copy()
    close = pd.Series(close)
    return s.reindex(close.index).ffill()

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

def dla_001_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _z(x, 63)

def dla_002_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def dla_003_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def dla_004_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _rank(x, 504)

def dla_005_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def dla_006_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def dla_007_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def dla_008_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def dla_009_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dla_010_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def dla_011_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def dla_012_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_013_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def dla_014_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).pct_change(126)

def dla_015_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _z(x, 252)

def dla_016_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x, y)

def dla_017_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def dla_018_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _rank(x, 21)

def dla_019_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def dla_020_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def dla_021_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x, _s(close))

def dla_022_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def dla_023_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def dla_024_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def dla_025_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def dla_026_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_027_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def dla_028_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(504)

def dla_029_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _z(x, 756)

def dla_030_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x, y)

def dla_031_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x - y, y.abs())

def dla_032_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 126)

def dla_033_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def dla_034_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def dla_035_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x, _s(close))

def dla_036_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def dla_037_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def dla_038_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def dla_039_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def dla_040_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_041_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def dla_042_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(21)

def dla_043_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _z(x, 63)

def dla_044_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x, y)

def dla_045_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x - y, y.abs())

def dla_046_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _rank(x, 504)

def dla_047_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def dla_048_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def dla_049_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x, _s(close))

def dla_050_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def dla_051_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dla_052_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def dla_053_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def dla_054_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_055_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def dla_056_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).pct_change(126)

def dla_057_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 252)

def dla_058_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def dla_059_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x - y, y.abs())

def dla_060_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _rank(x, 21)

def dla_061_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def dla_062_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def dla_063_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def dla_064_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def dla_065_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def dla_066_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def dla_067_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def dla_068_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_069_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def dla_070_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).pct_change(504)

def dla_071_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _z(x, 756)

def dla_072_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def dla_073_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def dla_074_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _rank(x, 126)

def dla_075_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

DILUTION_ACCELERATION_REGISTRY_001_075 = {
    "dla_001_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_001_capitulation_signal},
    "dla_002_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_002_capitulation_signal},
    "dla_003_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_003_capitulation_signal},
    "dla_004_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_004_capitulation_signal},
    "dla_005_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_005_capitulation_signal},
    "dla_006_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_006_capitulation_signal},
    "dla_007_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_007_capitulation_signal},
    "dla_008_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_008_capitulation_signal},
    "dla_009_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_009_capitulation_signal},
    "dla_010_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_010_capitulation_signal},
    "dla_011_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_011_capitulation_signal},
    "dla_012_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_012_capitulation_signal},
    "dla_013_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_013_capitulation_signal},
    "dla_014_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_014_capitulation_signal},
    "dla_015_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_015_capitulation_signal},
    "dla_016_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_016_capitulation_signal},
    "dla_017_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_017_capitulation_signal},
    "dla_018_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_018_capitulation_signal},
    "dla_019_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_019_capitulation_signal},
    "dla_020_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_020_capitulation_signal},
    "dla_021_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_021_capitulation_signal},
    "dla_022_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_022_capitulation_signal},
    "dla_023_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_023_capitulation_signal},
    "dla_024_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_024_capitulation_signal},
    "dla_025_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_025_capitulation_signal},
    "dla_026_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_026_capitulation_signal},
    "dla_027_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_027_capitulation_signal},
    "dla_028_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_028_capitulation_signal},
    "dla_029_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_029_capitulation_signal},
    "dla_030_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_030_capitulation_signal},
    "dla_031_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_031_capitulation_signal},
    "dla_032_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_032_capitulation_signal},
    "dla_033_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_033_capitulation_signal},
    "dla_034_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_034_capitulation_signal},
    "dla_035_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_035_capitulation_signal},
    "dla_036_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_036_capitulation_signal},
    "dla_037_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_037_capitulation_signal},
    "dla_038_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_038_capitulation_signal},
    "dla_039_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_039_capitulation_signal},
    "dla_040_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_040_capitulation_signal},
    "dla_041_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_041_capitulation_signal},
    "dla_042_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_042_capitulation_signal},
    "dla_043_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_043_capitulation_signal},
    "dla_044_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_044_capitulation_signal},
    "dla_045_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_045_capitulation_signal},
    "dla_046_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_046_capitulation_signal},
    "dla_047_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_047_capitulation_signal},
    "dla_048_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_048_capitulation_signal},
    "dla_049_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_049_capitulation_signal},
    "dla_050_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_050_capitulation_signal},
    "dla_051_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_051_capitulation_signal},
    "dla_052_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_052_capitulation_signal},
    "dla_053_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_053_capitulation_signal},
    "dla_054_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_054_capitulation_signal},
    "dla_055_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_055_capitulation_signal},
    "dla_056_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_056_capitulation_signal},
    "dla_057_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_057_capitulation_signal},
    "dla_058_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_058_capitulation_signal},
    "dla_059_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_059_capitulation_signal},
    "dla_060_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_060_capitulation_signal},
    "dla_061_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_061_capitulation_signal},
    "dla_062_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_062_capitulation_signal},
    "dla_063_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_063_capitulation_signal},
    "dla_064_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_064_capitulation_signal},
    "dla_065_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_065_capitulation_signal},
    "dla_066_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_066_capitulation_signal},
    "dla_067_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_067_capitulation_signal},
    "dla_068_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_068_capitulation_signal},
    "dla_069_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_069_capitulation_signal},
    "dla_070_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_070_capitulation_signal},
    "dla_071_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_071_capitulation_signal},
    "dla_072_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_072_capitulation_signal},
    "dla_073_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_073_capitulation_signal},
    "dla_074_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_074_capitulation_signal},
    "dla_075_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_075_capitulation_signal},
}
