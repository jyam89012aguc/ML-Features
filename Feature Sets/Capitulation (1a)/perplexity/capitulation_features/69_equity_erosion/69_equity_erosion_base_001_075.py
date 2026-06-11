"""Generated capitulation features for 69_equity_erosion: book value/equity erosion.
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

def eqe_001_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _z(x, 63)

def eqe_002_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def eqe_003_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x - y, y.abs())

def eqe_004_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _rank(x, 504)

def eqe_005_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def eqe_006_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def eqe_007_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def eqe_008_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def eqe_009_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def eqe_010_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def eqe_011_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def eqe_012_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_013_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def eqe_014_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(126)

def eqe_015_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _z(x, 252)

def eqe_016_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x, y)

def eqe_017_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def eqe_018_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _rank(x, 21)

def eqe_019_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def eqe_020_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def eqe_021_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x, _s(close))

def eqe_022_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def eqe_023_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def eqe_024_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def eqe_025_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def eqe_026_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_027_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def eqe_028_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(504)

def eqe_029_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _z(x, 756)

def eqe_030_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def eqe_031_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x - y, y.abs())

def eqe_032_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _rank(x, 126)

def eqe_033_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def eqe_034_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def eqe_035_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, _s(close))

def eqe_036_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def eqe_037_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def eqe_038_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def eqe_039_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def eqe_040_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_041_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def eqe_042_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(21)

def eqe_043_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _z(x, 63)

def eqe_044_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def eqe_045_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x - y, y.abs())

def eqe_046_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _rank(x, 504)

def eqe_047_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def eqe_048_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def eqe_049_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def eqe_050_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def eqe_051_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def eqe_052_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def eqe_053_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def eqe_054_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_055_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def eqe_056_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).pct_change(126)

def eqe_057_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _z(x, 252)

def eqe_058_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, y)

def eqe_059_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def eqe_060_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _rank(x, 21)

def eqe_061_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def eqe_062_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def eqe_063_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def eqe_064_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def eqe_065_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def eqe_066_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def eqe_067_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def eqe_068_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def eqe_069_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def eqe_070_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return _s(x).pct_change(504)

def eqe_071_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(bookvalue, close)
    return _z(x, 756)

def eqe_072_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(bookvalue, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def eqe_073_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x - y, y.abs())

def eqe_074_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(equity, close)
    return _rank(x, 126)

def eqe_075_capitulation_signal(close, equity, retainedearnings, bookvalue, assets, liabilities):
    x = _align_to_close(equity, close)
    y = _align_to_close(retainedearnings, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

EQUITY_EROSION_REGISTRY_001_075 = {
    "eqe_001_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_001_capitulation_signal},
    "eqe_002_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_002_capitulation_signal},
    "eqe_003_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_003_capitulation_signal},
    "eqe_004_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_004_capitulation_signal},
    "eqe_005_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_005_capitulation_signal},
    "eqe_006_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_006_capitulation_signal},
    "eqe_007_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_007_capitulation_signal},
    "eqe_008_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_008_capitulation_signal},
    "eqe_009_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_009_capitulation_signal},
    "eqe_010_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_010_capitulation_signal},
    "eqe_011_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_011_capitulation_signal},
    "eqe_012_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_012_capitulation_signal},
    "eqe_013_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_013_capitulation_signal},
    "eqe_014_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_014_capitulation_signal},
    "eqe_015_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_015_capitulation_signal},
    "eqe_016_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_016_capitulation_signal},
    "eqe_017_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_017_capitulation_signal},
    "eqe_018_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_018_capitulation_signal},
    "eqe_019_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_019_capitulation_signal},
    "eqe_020_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_020_capitulation_signal},
    "eqe_021_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_021_capitulation_signal},
    "eqe_022_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_022_capitulation_signal},
    "eqe_023_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_023_capitulation_signal},
    "eqe_024_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_024_capitulation_signal},
    "eqe_025_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_025_capitulation_signal},
    "eqe_026_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_026_capitulation_signal},
    "eqe_027_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_027_capitulation_signal},
    "eqe_028_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_028_capitulation_signal},
    "eqe_029_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_029_capitulation_signal},
    "eqe_030_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_030_capitulation_signal},
    "eqe_031_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_031_capitulation_signal},
    "eqe_032_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_032_capitulation_signal},
    "eqe_033_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_033_capitulation_signal},
    "eqe_034_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_034_capitulation_signal},
    "eqe_035_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_035_capitulation_signal},
    "eqe_036_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_036_capitulation_signal},
    "eqe_037_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_037_capitulation_signal},
    "eqe_038_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_038_capitulation_signal},
    "eqe_039_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_039_capitulation_signal},
    "eqe_040_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_040_capitulation_signal},
    "eqe_041_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_041_capitulation_signal},
    "eqe_042_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_042_capitulation_signal},
    "eqe_043_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_043_capitulation_signal},
    "eqe_044_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_044_capitulation_signal},
    "eqe_045_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_045_capitulation_signal},
    "eqe_046_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_046_capitulation_signal},
    "eqe_047_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_047_capitulation_signal},
    "eqe_048_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_048_capitulation_signal},
    "eqe_049_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_049_capitulation_signal},
    "eqe_050_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_050_capitulation_signal},
    "eqe_051_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_051_capitulation_signal},
    "eqe_052_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_052_capitulation_signal},
    "eqe_053_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_053_capitulation_signal},
    "eqe_054_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_054_capitulation_signal},
    "eqe_055_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_055_capitulation_signal},
    "eqe_056_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_056_capitulation_signal},
    "eqe_057_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_057_capitulation_signal},
    "eqe_058_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_058_capitulation_signal},
    "eqe_059_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_059_capitulation_signal},
    "eqe_060_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_060_capitulation_signal},
    "eqe_061_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_061_capitulation_signal},
    "eqe_062_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_062_capitulation_signal},
    "eqe_063_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_063_capitulation_signal},
    "eqe_064_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_064_capitulation_signal},
    "eqe_065_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_065_capitulation_signal},
    "eqe_066_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_066_capitulation_signal},
    "eqe_067_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_067_capitulation_signal},
    "eqe_068_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_068_capitulation_signal},
    "eqe_069_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_069_capitulation_signal},
    "eqe_070_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_070_capitulation_signal},
    "eqe_071_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_071_capitulation_signal},
    "eqe_072_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_072_capitulation_signal},
    "eqe_073_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_073_capitulation_signal},
    "eqe_074_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_074_capitulation_signal},
    "eqe_075_capitulation_signal": {"inputs": ['close', 'equity', 'retainedearnings', 'bookvalue', 'assets', 'liabilities'], "func": eqe_075_capitulation_signal},
}
