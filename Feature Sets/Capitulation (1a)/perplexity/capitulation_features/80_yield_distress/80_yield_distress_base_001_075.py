"""Generated capitulation features for 80_yield_distress: yield spikes.
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

def yld_001_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _z(x, 63)

def yld_002_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def yld_003_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def yld_004_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _rank(x, 504)

def yld_005_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def yld_006_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def yld_007_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def yld_008_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def yld_009_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def yld_010_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def yld_011_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def yld_012_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_013_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def yld_014_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).pct_change(126)

def yld_015_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _z(x, 252)

def yld_016_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x, y)

def yld_017_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def yld_018_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 21)

def yld_019_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def yld_020_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def yld_021_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x, _s(close))

def yld_022_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def yld_023_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def yld_024_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def yld_025_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def yld_026_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_027_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def yld_028_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(504)

def yld_029_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _z(x, 756)

def yld_030_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x, y)

def yld_031_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x - y, y.abs())

def yld_032_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 126)

def yld_033_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def yld_034_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def yld_035_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x, _s(close))

def yld_036_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def yld_037_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def yld_038_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def yld_039_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def yld_040_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_041_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def yld_042_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(21)

def yld_043_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 63)

def yld_044_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x, y)

def yld_045_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x - y, y.abs())

def yld_046_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _rank(x, 504)

def yld_047_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def yld_048_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def yld_049_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x, _s(close))

def yld_050_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def yld_051_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def yld_052_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def yld_053_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def yld_054_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_055_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def yld_056_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).pct_change(126)

def yld_057_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _z(x, 252)

def yld_058_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def yld_059_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x - y, y.abs())

def yld_060_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _rank(x, 21)

def yld_061_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def yld_062_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def yld_063_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def yld_064_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def yld_065_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def yld_066_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def yld_067_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def yld_068_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def yld_069_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def yld_070_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return _s(x).pct_change(504)

def yld_071_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(divyield, close)
    y = _align_to_close(eps, close)
    return _z(x, 756)

def yld_072_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(eps, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def yld_073_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(netinc, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def yld_074_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(dividends, close)
    return _rank(x, 126)

def yld_075_capitulation_signal(close, dividends, divyield, eps, netinc, marketcap):
    x = _align_to_close(dividends, close)
    y = _align_to_close(divyield, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

YIELD_DISTRESS_REGISTRY_001_075 = {
    "yld_001_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_001_capitulation_signal},
    "yld_002_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_002_capitulation_signal},
    "yld_003_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_003_capitulation_signal},
    "yld_004_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_004_capitulation_signal},
    "yld_005_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_005_capitulation_signal},
    "yld_006_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_006_capitulation_signal},
    "yld_007_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_007_capitulation_signal},
    "yld_008_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_008_capitulation_signal},
    "yld_009_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_009_capitulation_signal},
    "yld_010_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_010_capitulation_signal},
    "yld_011_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_011_capitulation_signal},
    "yld_012_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_012_capitulation_signal},
    "yld_013_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_013_capitulation_signal},
    "yld_014_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_014_capitulation_signal},
    "yld_015_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_015_capitulation_signal},
    "yld_016_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_016_capitulation_signal},
    "yld_017_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_017_capitulation_signal},
    "yld_018_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_018_capitulation_signal},
    "yld_019_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_019_capitulation_signal},
    "yld_020_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_020_capitulation_signal},
    "yld_021_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_021_capitulation_signal},
    "yld_022_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_022_capitulation_signal},
    "yld_023_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_023_capitulation_signal},
    "yld_024_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_024_capitulation_signal},
    "yld_025_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_025_capitulation_signal},
    "yld_026_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_026_capitulation_signal},
    "yld_027_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_027_capitulation_signal},
    "yld_028_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_028_capitulation_signal},
    "yld_029_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_029_capitulation_signal},
    "yld_030_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_030_capitulation_signal},
    "yld_031_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_031_capitulation_signal},
    "yld_032_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_032_capitulation_signal},
    "yld_033_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_033_capitulation_signal},
    "yld_034_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_034_capitulation_signal},
    "yld_035_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_035_capitulation_signal},
    "yld_036_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_036_capitulation_signal},
    "yld_037_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_037_capitulation_signal},
    "yld_038_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_038_capitulation_signal},
    "yld_039_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_039_capitulation_signal},
    "yld_040_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_040_capitulation_signal},
    "yld_041_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_041_capitulation_signal},
    "yld_042_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_042_capitulation_signal},
    "yld_043_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_043_capitulation_signal},
    "yld_044_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_044_capitulation_signal},
    "yld_045_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_045_capitulation_signal},
    "yld_046_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_046_capitulation_signal},
    "yld_047_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_047_capitulation_signal},
    "yld_048_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_048_capitulation_signal},
    "yld_049_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_049_capitulation_signal},
    "yld_050_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_050_capitulation_signal},
    "yld_051_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_051_capitulation_signal},
    "yld_052_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_052_capitulation_signal},
    "yld_053_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_053_capitulation_signal},
    "yld_054_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_054_capitulation_signal},
    "yld_055_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_055_capitulation_signal},
    "yld_056_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_056_capitulation_signal},
    "yld_057_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_057_capitulation_signal},
    "yld_058_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_058_capitulation_signal},
    "yld_059_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_059_capitulation_signal},
    "yld_060_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_060_capitulation_signal},
    "yld_061_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_061_capitulation_signal},
    "yld_062_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_062_capitulation_signal},
    "yld_063_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_063_capitulation_signal},
    "yld_064_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_064_capitulation_signal},
    "yld_065_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_065_capitulation_signal},
    "yld_066_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_066_capitulation_signal},
    "yld_067_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_067_capitulation_signal},
    "yld_068_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_068_capitulation_signal},
    "yld_069_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_069_capitulation_signal},
    "yld_070_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_070_capitulation_signal},
    "yld_071_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_071_capitulation_signal},
    "yld_072_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_072_capitulation_signal},
    "yld_073_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_073_capitulation_signal},
    "yld_074_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_074_capitulation_signal},
    "yld_075_capitulation_signal": {"inputs": ['close', 'dividends', 'divyield', 'eps', 'netinc', 'marketcap'], "func": yld_075_capitulation_signal},
}
