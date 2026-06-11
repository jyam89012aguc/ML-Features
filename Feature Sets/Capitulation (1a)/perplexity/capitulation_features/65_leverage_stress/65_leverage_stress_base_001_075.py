"""Generated capitulation features for 65_leverage_stress: debt escalation.
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

def lvs_001_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _z(x, 63)

def lvs_002_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, y)

def lvs_003_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def lvs_004_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _rank(x, 504)

def lvs_005_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lvs_006_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lvs_007_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def lvs_008_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lvs_009_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lvs_010_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lvs_011_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lvs_012_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_013_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lvs_014_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(126)

def lvs_015_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _z(x, 252)

def lvs_016_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def lvs_017_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x - y, y.abs())

def lvs_018_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _rank(x, 21)

def lvs_019_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lvs_020_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lvs_021_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def lvs_022_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lvs_023_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lvs_024_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lvs_025_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lvs_026_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_027_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lvs_028_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(504)

def lvs_029_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _z(x, 756)

def lvs_030_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def lvs_031_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def lvs_032_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _rank(x, 126)

def lvs_033_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def lvs_034_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def lvs_035_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def lvs_036_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def lvs_037_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def lvs_038_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def lvs_039_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def lvs_040_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_041_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def lvs_042_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(21)

def lvs_043_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _z(x, 63)

def lvs_044_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def lvs_045_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def lvs_046_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _rank(x, 504)

def lvs_047_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def lvs_048_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def lvs_049_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close))

def lvs_050_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def lvs_051_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def lvs_052_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def lvs_053_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def lvs_054_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_055_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def lvs_056_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(126)

def lvs_057_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _z(x, 252)

def lvs_058_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, y)

def lvs_059_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x - y, y.abs())

def lvs_060_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _rank(x, 21)

def lvs_061_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def lvs_062_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def lvs_063_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x, _s(close))

def lvs_064_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def lvs_065_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def lvs_066_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def lvs_067_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def lvs_068_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def lvs_069_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def lvs_070_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(504)

def lvs_071_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(equity, close)
    y = _align_to_close(assets, close)
    return _z(x, 756)

def lvs_072_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, y)

def lvs_073_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(ebitda, close)
    return _div(x - y, y.abs())

def lvs_074_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(ebitda, close)
    y = _align_to_close(debt, close)
    return _rank(x, 126)

def lvs_075_capitulation_signal(close, debt, equity, assets, liabilities, ebitda):
    x = _align_to_close(debt, close)
    y = _align_to_close(equity, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

LEVERAGE_STRESS_REGISTRY_001_075 = {
    "lvs_001_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_001_capitulation_signal},
    "lvs_002_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_002_capitulation_signal},
    "lvs_003_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_003_capitulation_signal},
    "lvs_004_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_004_capitulation_signal},
    "lvs_005_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_005_capitulation_signal},
    "lvs_006_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_006_capitulation_signal},
    "lvs_007_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_007_capitulation_signal},
    "lvs_008_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_008_capitulation_signal},
    "lvs_009_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_009_capitulation_signal},
    "lvs_010_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_010_capitulation_signal},
    "lvs_011_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_011_capitulation_signal},
    "lvs_012_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_012_capitulation_signal},
    "lvs_013_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_013_capitulation_signal},
    "lvs_014_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_014_capitulation_signal},
    "lvs_015_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_015_capitulation_signal},
    "lvs_016_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_016_capitulation_signal},
    "lvs_017_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_017_capitulation_signal},
    "lvs_018_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_018_capitulation_signal},
    "lvs_019_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_019_capitulation_signal},
    "lvs_020_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_020_capitulation_signal},
    "lvs_021_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_021_capitulation_signal},
    "lvs_022_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_022_capitulation_signal},
    "lvs_023_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_023_capitulation_signal},
    "lvs_024_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_024_capitulation_signal},
    "lvs_025_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_025_capitulation_signal},
    "lvs_026_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_026_capitulation_signal},
    "lvs_027_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_027_capitulation_signal},
    "lvs_028_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_028_capitulation_signal},
    "lvs_029_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_029_capitulation_signal},
    "lvs_030_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_030_capitulation_signal},
    "lvs_031_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_031_capitulation_signal},
    "lvs_032_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_032_capitulation_signal},
    "lvs_033_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_033_capitulation_signal},
    "lvs_034_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_034_capitulation_signal},
    "lvs_035_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_035_capitulation_signal},
    "lvs_036_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_036_capitulation_signal},
    "lvs_037_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_037_capitulation_signal},
    "lvs_038_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_038_capitulation_signal},
    "lvs_039_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_039_capitulation_signal},
    "lvs_040_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_040_capitulation_signal},
    "lvs_041_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_041_capitulation_signal},
    "lvs_042_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_042_capitulation_signal},
    "lvs_043_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_043_capitulation_signal},
    "lvs_044_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_044_capitulation_signal},
    "lvs_045_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_045_capitulation_signal},
    "lvs_046_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_046_capitulation_signal},
    "lvs_047_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_047_capitulation_signal},
    "lvs_048_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_048_capitulation_signal},
    "lvs_049_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_049_capitulation_signal},
    "lvs_050_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_050_capitulation_signal},
    "lvs_051_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_051_capitulation_signal},
    "lvs_052_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_052_capitulation_signal},
    "lvs_053_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_053_capitulation_signal},
    "lvs_054_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_054_capitulation_signal},
    "lvs_055_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_055_capitulation_signal},
    "lvs_056_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_056_capitulation_signal},
    "lvs_057_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_057_capitulation_signal},
    "lvs_058_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_058_capitulation_signal},
    "lvs_059_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_059_capitulation_signal},
    "lvs_060_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_060_capitulation_signal},
    "lvs_061_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_061_capitulation_signal},
    "lvs_062_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_062_capitulation_signal},
    "lvs_063_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_063_capitulation_signal},
    "lvs_064_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_064_capitulation_signal},
    "lvs_065_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_065_capitulation_signal},
    "lvs_066_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_066_capitulation_signal},
    "lvs_067_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_067_capitulation_signal},
    "lvs_068_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_068_capitulation_signal},
    "lvs_069_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_069_capitulation_signal},
    "lvs_070_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_070_capitulation_signal},
    "lvs_071_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_071_capitulation_signal},
    "lvs_072_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_072_capitulation_signal},
    "lvs_073_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_073_capitulation_signal},
    "lvs_074_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_074_capitulation_signal},
    "lvs_075_capitulation_signal": {"inputs": ['close', 'debt', 'equity', 'assets', 'liabilities', 'ebitda'], "func": lvs_075_capitulation_signal},
}
