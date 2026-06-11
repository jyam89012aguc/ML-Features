"""Generated capitulation features for 66_interest_coverage: interest coverage deterioration.
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

def icv_001_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _z(x, 63)

def icv_002_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, y)

def icv_003_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x - y, y.abs())

def icv_004_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 504)

def icv_005_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def icv_006_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def icv_007_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def icv_008_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def icv_009_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def icv_010_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def icv_011_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def icv_012_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_013_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def icv_014_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(126)

def icv_015_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _z(x, 252)

def icv_016_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def icv_017_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def icv_018_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 21)

def icv_019_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def icv_020_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def icv_021_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close))

def icv_022_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def icv_023_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def icv_024_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def icv_025_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def icv_026_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_027_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def icv_028_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(504)

def icv_029_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _z(x, 756)

def icv_030_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x, y)

def icv_031_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x - y, y.abs())

def icv_032_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _rank(x, 126)

def icv_033_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def icv_034_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def icv_035_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x, _s(close))

def icv_036_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def icv_037_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def icv_038_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def icv_039_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def icv_040_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_041_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def icv_042_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(21)

def icv_043_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _z(x, 63)

def icv_044_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x, y)

def icv_045_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x - y, y.abs())

def icv_046_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _rank(x, 504)

def icv_047_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def icv_048_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def icv_049_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close))

def icv_050_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def icv_051_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def icv_052_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def icv_053_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def icv_054_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_055_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def icv_056_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(126)

def icv_057_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 252)

def icv_058_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def icv_059_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def icv_060_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _rank(x, 21)

def icv_061_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def icv_062_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def icv_063_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close))

def icv_064_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def icv_065_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def icv_066_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def icv_067_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def icv_068_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icv_069_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def icv_070_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return _s(x).pct_change(504)

def icv_071_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(intexp, close)
    y = _align_to_close(debt, close)
    return _z(x, 756)

def icv_072_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(debt, close)
    y = _align_to_close(ebitda, close)
    return _div(x, y)

def icv_073_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(cashneq, close)
    return _div(x - y, y.abs())

def icv_074_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(ebit, close)
    return _rank(x, 126)

def icv_075_capitulation_signal(close, ebit, intexp, debt, ebitda, cashneq):
    x = _align_to_close(ebit, close)
    y = _align_to_close(intexp, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

INTEREST_COVERAGE_REGISTRY_001_075 = {
    "icv_001_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_001_capitulation_signal},
    "icv_002_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_002_capitulation_signal},
    "icv_003_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_003_capitulation_signal},
    "icv_004_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_004_capitulation_signal},
    "icv_005_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_005_capitulation_signal},
    "icv_006_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_006_capitulation_signal},
    "icv_007_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_007_capitulation_signal},
    "icv_008_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_008_capitulation_signal},
    "icv_009_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_009_capitulation_signal},
    "icv_010_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_010_capitulation_signal},
    "icv_011_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_011_capitulation_signal},
    "icv_012_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_012_capitulation_signal},
    "icv_013_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_013_capitulation_signal},
    "icv_014_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_014_capitulation_signal},
    "icv_015_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_015_capitulation_signal},
    "icv_016_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_016_capitulation_signal},
    "icv_017_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_017_capitulation_signal},
    "icv_018_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_018_capitulation_signal},
    "icv_019_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_019_capitulation_signal},
    "icv_020_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_020_capitulation_signal},
    "icv_021_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_021_capitulation_signal},
    "icv_022_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_022_capitulation_signal},
    "icv_023_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_023_capitulation_signal},
    "icv_024_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_024_capitulation_signal},
    "icv_025_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_025_capitulation_signal},
    "icv_026_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_026_capitulation_signal},
    "icv_027_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_027_capitulation_signal},
    "icv_028_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_028_capitulation_signal},
    "icv_029_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_029_capitulation_signal},
    "icv_030_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_030_capitulation_signal},
    "icv_031_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_031_capitulation_signal},
    "icv_032_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_032_capitulation_signal},
    "icv_033_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_033_capitulation_signal},
    "icv_034_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_034_capitulation_signal},
    "icv_035_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_035_capitulation_signal},
    "icv_036_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_036_capitulation_signal},
    "icv_037_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_037_capitulation_signal},
    "icv_038_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_038_capitulation_signal},
    "icv_039_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_039_capitulation_signal},
    "icv_040_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_040_capitulation_signal},
    "icv_041_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_041_capitulation_signal},
    "icv_042_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_042_capitulation_signal},
    "icv_043_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_043_capitulation_signal},
    "icv_044_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_044_capitulation_signal},
    "icv_045_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_045_capitulation_signal},
    "icv_046_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_046_capitulation_signal},
    "icv_047_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_047_capitulation_signal},
    "icv_048_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_048_capitulation_signal},
    "icv_049_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_049_capitulation_signal},
    "icv_050_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_050_capitulation_signal},
    "icv_051_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_051_capitulation_signal},
    "icv_052_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_052_capitulation_signal},
    "icv_053_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_053_capitulation_signal},
    "icv_054_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_054_capitulation_signal},
    "icv_055_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_055_capitulation_signal},
    "icv_056_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_056_capitulation_signal},
    "icv_057_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_057_capitulation_signal},
    "icv_058_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_058_capitulation_signal},
    "icv_059_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_059_capitulation_signal},
    "icv_060_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_060_capitulation_signal},
    "icv_061_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_061_capitulation_signal},
    "icv_062_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_062_capitulation_signal},
    "icv_063_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_063_capitulation_signal},
    "icv_064_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_064_capitulation_signal},
    "icv_065_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_065_capitulation_signal},
    "icv_066_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_066_capitulation_signal},
    "icv_067_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_067_capitulation_signal},
    "icv_068_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_068_capitulation_signal},
    "icv_069_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_069_capitulation_signal},
    "icv_070_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_070_capitulation_signal},
    "icv_071_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_071_capitulation_signal},
    "icv_072_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_072_capitulation_signal},
    "icv_073_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_073_capitulation_signal},
    "icv_074_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_074_capitulation_signal},
    "icv_075_capitulation_signal": {"inputs": ['close', 'ebit', 'intexp', 'debt', 'ebitda', 'cashneq'], "func": icv_075_capitulation_signal},
}
