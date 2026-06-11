"""Generated capitulation features for 62_margin_compression: margin erosion.
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

def mgc_001_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _z(x, 63)

def mgc_002_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def mgc_003_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def mgc_004_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 504)

def mgc_005_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def mgc_006_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def mgc_007_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def mgc_008_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def mgc_009_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mgc_010_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def mgc_011_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def mgc_012_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_013_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def mgc_014_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def mgc_015_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _z(x, 252)

def mgc_016_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x, y)

def mgc_017_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def mgc_018_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 21)

def mgc_019_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def mgc_020_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def mgc_021_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x, _s(close))

def mgc_022_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def mgc_023_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def mgc_024_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def mgc_025_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def mgc_026_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_027_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def mgc_028_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(504)

def mgc_029_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _z(x, 756)

def mgc_030_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, y)

def mgc_031_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x - y, y.abs())

def mgc_032_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 126)

def mgc_033_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def mgc_034_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def mgc_035_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close))

def mgc_036_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def mgc_037_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def mgc_038_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def mgc_039_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def mgc_040_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_041_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def mgc_042_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(21)

def mgc_043_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _z(x, 63)

def mgc_044_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def mgc_045_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x - y, y.abs())

def mgc_046_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _rank(x, 504)

def mgc_047_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def mgc_048_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def mgc_049_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def mgc_050_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def mgc_051_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def mgc_052_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def mgc_053_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def mgc_054_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_055_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def mgc_056_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).pct_change(126)

def mgc_057_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _z(x, 252)

def mgc_058_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def mgc_059_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def mgc_060_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _rank(x, 21)

def mgc_061_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def mgc_062_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def mgc_063_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close))

def mgc_064_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def mgc_065_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def mgc_066_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def mgc_067_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def mgc_068_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def mgc_069_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def mgc_070_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return _s(x).pct_change(504)

def mgc_071_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(grossprofit, close)
    y = _align_to_close(opinc, close)
    return _z(x, 756)

def mgc_072_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(opinc, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def mgc_073_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def mgc_074_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(ebit, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 126)

def mgc_075_capitulation_signal(close, revenue, grossprofit, opinc, netinc, ebit):
    x = _align_to_close(revenue, close)
    y = _align_to_close(grossprofit, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

MARGIN_COMPRESSION_REGISTRY_001_075 = {
    "mgc_001_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_001_capitulation_signal},
    "mgc_002_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_002_capitulation_signal},
    "mgc_003_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_003_capitulation_signal},
    "mgc_004_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_004_capitulation_signal},
    "mgc_005_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_005_capitulation_signal},
    "mgc_006_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_006_capitulation_signal},
    "mgc_007_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_007_capitulation_signal},
    "mgc_008_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_008_capitulation_signal},
    "mgc_009_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_009_capitulation_signal},
    "mgc_010_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_010_capitulation_signal},
    "mgc_011_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_011_capitulation_signal},
    "mgc_012_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_012_capitulation_signal},
    "mgc_013_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_013_capitulation_signal},
    "mgc_014_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_014_capitulation_signal},
    "mgc_015_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_015_capitulation_signal},
    "mgc_016_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_016_capitulation_signal},
    "mgc_017_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_017_capitulation_signal},
    "mgc_018_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_018_capitulation_signal},
    "mgc_019_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_019_capitulation_signal},
    "mgc_020_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_020_capitulation_signal},
    "mgc_021_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_021_capitulation_signal},
    "mgc_022_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_022_capitulation_signal},
    "mgc_023_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_023_capitulation_signal},
    "mgc_024_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_024_capitulation_signal},
    "mgc_025_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_025_capitulation_signal},
    "mgc_026_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_026_capitulation_signal},
    "mgc_027_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_027_capitulation_signal},
    "mgc_028_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_028_capitulation_signal},
    "mgc_029_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_029_capitulation_signal},
    "mgc_030_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_030_capitulation_signal},
    "mgc_031_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_031_capitulation_signal},
    "mgc_032_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_032_capitulation_signal},
    "mgc_033_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_033_capitulation_signal},
    "mgc_034_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_034_capitulation_signal},
    "mgc_035_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_035_capitulation_signal},
    "mgc_036_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_036_capitulation_signal},
    "mgc_037_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_037_capitulation_signal},
    "mgc_038_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_038_capitulation_signal},
    "mgc_039_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_039_capitulation_signal},
    "mgc_040_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_040_capitulation_signal},
    "mgc_041_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_041_capitulation_signal},
    "mgc_042_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_042_capitulation_signal},
    "mgc_043_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_043_capitulation_signal},
    "mgc_044_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_044_capitulation_signal},
    "mgc_045_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_045_capitulation_signal},
    "mgc_046_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_046_capitulation_signal},
    "mgc_047_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_047_capitulation_signal},
    "mgc_048_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_048_capitulation_signal},
    "mgc_049_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_049_capitulation_signal},
    "mgc_050_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_050_capitulation_signal},
    "mgc_051_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_051_capitulation_signal},
    "mgc_052_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_052_capitulation_signal},
    "mgc_053_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_053_capitulation_signal},
    "mgc_054_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_054_capitulation_signal},
    "mgc_055_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_055_capitulation_signal},
    "mgc_056_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_056_capitulation_signal},
    "mgc_057_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_057_capitulation_signal},
    "mgc_058_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_058_capitulation_signal},
    "mgc_059_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_059_capitulation_signal},
    "mgc_060_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_060_capitulation_signal},
    "mgc_061_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_061_capitulation_signal},
    "mgc_062_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_062_capitulation_signal},
    "mgc_063_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_063_capitulation_signal},
    "mgc_064_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_064_capitulation_signal},
    "mgc_065_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_065_capitulation_signal},
    "mgc_066_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_066_capitulation_signal},
    "mgc_067_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_067_capitulation_signal},
    "mgc_068_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_068_capitulation_signal},
    "mgc_069_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_069_capitulation_signal},
    "mgc_070_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_070_capitulation_signal},
    "mgc_071_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_071_capitulation_signal},
    "mgc_072_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_072_capitulation_signal},
    "mgc_073_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_073_capitulation_signal},
    "mgc_074_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_074_capitulation_signal},
    "mgc_075_capitulation_signal": {"inputs": ['close', 'revenue', 'grossprofit', 'opinc', 'netinc', 'ebit'], "func": mgc_075_capitulation_signal},
}
