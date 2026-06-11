"""Generated capitulation features for 68_asset_quality: asset-quality contraction.
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

def aqy_001_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _z(x, 63)

def aqy_002_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, y)

def aqy_003_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def aqy_004_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _rank(x, 504)

def aqy_005_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def aqy_006_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def aqy_007_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, _s(close))

def aqy_008_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def aqy_009_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def aqy_010_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def aqy_011_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def aqy_012_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_013_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def aqy_014_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(126)

def aqy_015_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _z(x, 252)

def aqy_016_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x, y)

def aqy_017_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x - y, y.abs())

def aqy_018_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 21)

def aqy_019_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def aqy_020_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def aqy_021_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x, _s(close))

def aqy_022_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def aqy_023_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def aqy_024_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def aqy_025_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def aqy_026_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_027_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def aqy_028_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(504)

def aqy_029_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _z(x, 756)

def aqy_030_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x, y)

def aqy_031_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x - y, y.abs())

def aqy_032_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _rank(x, 126)

def aqy_033_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def aqy_034_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def aqy_035_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close))

def aqy_036_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def aqy_037_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def aqy_038_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def aqy_039_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def aqy_040_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_041_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def aqy_042_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).pct_change(21)

def aqy_043_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _z(x, 63)

def aqy_044_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def aqy_045_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x - y, y.abs())

def aqy_046_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _rank(x, 504)

def aqy_047_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def aqy_048_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def aqy_049_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def aqy_050_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def aqy_051_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def aqy_052_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def aqy_053_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def aqy_054_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_055_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def aqy_056_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).pct_change(126)

def aqy_057_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _z(x, 252)

def aqy_058_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def aqy_059_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def aqy_060_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 21)

def aqy_061_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def aqy_062_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def aqy_063_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def aqy_064_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def aqy_065_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def aqy_066_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def aqy_067_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def aqy_068_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_069_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def aqy_070_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(504)

def aqy_071_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _z(x, 756)

def aqy_072_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, y)

def aqy_073_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def aqy_074_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _rank(x, 126)

def aqy_075_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

ASSET_QUALITY_REGISTRY_001_075 = {
    "aqy_001_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_001_capitulation_signal},
    "aqy_002_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_002_capitulation_signal},
    "aqy_003_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_003_capitulation_signal},
    "aqy_004_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_004_capitulation_signal},
    "aqy_005_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_005_capitulation_signal},
    "aqy_006_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_006_capitulation_signal},
    "aqy_007_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_007_capitulation_signal},
    "aqy_008_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_008_capitulation_signal},
    "aqy_009_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_009_capitulation_signal},
    "aqy_010_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_010_capitulation_signal},
    "aqy_011_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_011_capitulation_signal},
    "aqy_012_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_012_capitulation_signal},
    "aqy_013_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_013_capitulation_signal},
    "aqy_014_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_014_capitulation_signal},
    "aqy_015_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_015_capitulation_signal},
    "aqy_016_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_016_capitulation_signal},
    "aqy_017_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_017_capitulation_signal},
    "aqy_018_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_018_capitulation_signal},
    "aqy_019_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_019_capitulation_signal},
    "aqy_020_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_020_capitulation_signal},
    "aqy_021_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_021_capitulation_signal},
    "aqy_022_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_022_capitulation_signal},
    "aqy_023_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_023_capitulation_signal},
    "aqy_024_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_024_capitulation_signal},
    "aqy_025_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_025_capitulation_signal},
    "aqy_026_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_026_capitulation_signal},
    "aqy_027_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_027_capitulation_signal},
    "aqy_028_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_028_capitulation_signal},
    "aqy_029_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_029_capitulation_signal},
    "aqy_030_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_030_capitulation_signal},
    "aqy_031_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_031_capitulation_signal},
    "aqy_032_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_032_capitulation_signal},
    "aqy_033_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_033_capitulation_signal},
    "aqy_034_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_034_capitulation_signal},
    "aqy_035_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_035_capitulation_signal},
    "aqy_036_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_036_capitulation_signal},
    "aqy_037_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_037_capitulation_signal},
    "aqy_038_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_038_capitulation_signal},
    "aqy_039_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_039_capitulation_signal},
    "aqy_040_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_040_capitulation_signal},
    "aqy_041_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_041_capitulation_signal},
    "aqy_042_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_042_capitulation_signal},
    "aqy_043_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_043_capitulation_signal},
    "aqy_044_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_044_capitulation_signal},
    "aqy_045_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_045_capitulation_signal},
    "aqy_046_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_046_capitulation_signal},
    "aqy_047_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_047_capitulation_signal},
    "aqy_048_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_048_capitulation_signal},
    "aqy_049_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_049_capitulation_signal},
    "aqy_050_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_050_capitulation_signal},
    "aqy_051_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_051_capitulation_signal},
    "aqy_052_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_052_capitulation_signal},
    "aqy_053_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_053_capitulation_signal},
    "aqy_054_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_054_capitulation_signal},
    "aqy_055_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_055_capitulation_signal},
    "aqy_056_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_056_capitulation_signal},
    "aqy_057_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_057_capitulation_signal},
    "aqy_058_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_058_capitulation_signal},
    "aqy_059_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_059_capitulation_signal},
    "aqy_060_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_060_capitulation_signal},
    "aqy_061_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_061_capitulation_signal},
    "aqy_062_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_062_capitulation_signal},
    "aqy_063_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_063_capitulation_signal},
    "aqy_064_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_064_capitulation_signal},
    "aqy_065_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_065_capitulation_signal},
    "aqy_066_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_066_capitulation_signal},
    "aqy_067_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_067_capitulation_signal},
    "aqy_068_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_068_capitulation_signal},
    "aqy_069_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_069_capitulation_signal},
    "aqy_070_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_070_capitulation_signal},
    "aqy_071_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_071_capitulation_signal},
    "aqy_072_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_072_capitulation_signal},
    "aqy_073_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_073_capitulation_signal},
    "aqy_074_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_074_capitulation_signal},
    "aqy_075_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_075_capitulation_signal},
}
