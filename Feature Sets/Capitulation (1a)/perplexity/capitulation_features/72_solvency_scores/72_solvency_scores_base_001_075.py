"""Generated capitulation features for 72_solvency_scores: solvency composites.
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

def slv_001_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 63)

def slv_002_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_003_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_004_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 504)

def slv_005_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def slv_006_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def slv_007_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_008_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def slv_009_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def slv_010_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def slv_011_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def slv_012_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_013_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def slv_014_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(126)

def slv_015_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 252)

def slv_016_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_017_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_018_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 21)

def slv_019_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def slv_020_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def slv_021_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_022_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def slv_023_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def slv_024_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def slv_025_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def slv_026_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_027_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def slv_028_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(504)

def slv_029_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 756)

def slv_030_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_031_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_032_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 126)

def slv_033_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def slv_034_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def slv_035_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_036_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def slv_037_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def slv_038_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def slv_039_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def slv_040_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_041_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def slv_042_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(21)

def slv_043_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 63)

def slv_044_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_045_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_046_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 504)

def slv_047_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def slv_048_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def slv_049_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_050_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def slv_051_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def slv_052_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def slv_053_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def slv_054_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_055_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def slv_056_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(126)

def slv_057_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 252)

def slv_058_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_059_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_060_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 21)

def slv_061_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def slv_062_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def slv_063_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _div(x, _s(close))

def slv_064_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def slv_065_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def slv_066_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def slv_067_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def slv_068_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def slv_069_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def slv_070_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(liabilities, close)
    return _s(x).pct_change(504)

def slv_071_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(liabilities, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 756)

def slv_072_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(retainedearnings, close)
    return _div(x, y)

def slv_073_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(retainedearnings, close)
    y = _align_to_close(ebit, close)
    return _div(x - y, y.abs())

def slv_074_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(ebit, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 126)

def slv_075_capitulation_signal(close, assets, liabilities, workingcapital, retainedearnings, ebit, marketcap, revenue):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(revenue, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

SOLVENCY_SCORES_REGISTRY_001_075 = {
    "slv_001_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_001_capitulation_signal},
    "slv_002_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_002_capitulation_signal},
    "slv_003_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_003_capitulation_signal},
    "slv_004_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_004_capitulation_signal},
    "slv_005_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_005_capitulation_signal},
    "slv_006_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_006_capitulation_signal},
    "slv_007_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_007_capitulation_signal},
    "slv_008_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_008_capitulation_signal},
    "slv_009_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_009_capitulation_signal},
    "slv_010_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_010_capitulation_signal},
    "slv_011_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_011_capitulation_signal},
    "slv_012_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_012_capitulation_signal},
    "slv_013_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_013_capitulation_signal},
    "slv_014_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_014_capitulation_signal},
    "slv_015_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_015_capitulation_signal},
    "slv_016_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_016_capitulation_signal},
    "slv_017_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_017_capitulation_signal},
    "slv_018_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_018_capitulation_signal},
    "slv_019_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_019_capitulation_signal},
    "slv_020_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_020_capitulation_signal},
    "slv_021_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_021_capitulation_signal},
    "slv_022_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_022_capitulation_signal},
    "slv_023_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_023_capitulation_signal},
    "slv_024_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_024_capitulation_signal},
    "slv_025_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_025_capitulation_signal},
    "slv_026_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_026_capitulation_signal},
    "slv_027_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_027_capitulation_signal},
    "slv_028_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_028_capitulation_signal},
    "slv_029_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_029_capitulation_signal},
    "slv_030_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_030_capitulation_signal},
    "slv_031_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_031_capitulation_signal},
    "slv_032_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_032_capitulation_signal},
    "slv_033_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_033_capitulation_signal},
    "slv_034_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_034_capitulation_signal},
    "slv_035_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_035_capitulation_signal},
    "slv_036_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_036_capitulation_signal},
    "slv_037_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_037_capitulation_signal},
    "slv_038_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_038_capitulation_signal},
    "slv_039_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_039_capitulation_signal},
    "slv_040_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_040_capitulation_signal},
    "slv_041_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_041_capitulation_signal},
    "slv_042_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_042_capitulation_signal},
    "slv_043_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_043_capitulation_signal},
    "slv_044_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_044_capitulation_signal},
    "slv_045_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_045_capitulation_signal},
    "slv_046_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_046_capitulation_signal},
    "slv_047_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_047_capitulation_signal},
    "slv_048_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_048_capitulation_signal},
    "slv_049_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_049_capitulation_signal},
    "slv_050_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_050_capitulation_signal},
    "slv_051_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_051_capitulation_signal},
    "slv_052_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_052_capitulation_signal},
    "slv_053_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_053_capitulation_signal},
    "slv_054_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_054_capitulation_signal},
    "slv_055_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_055_capitulation_signal},
    "slv_056_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_056_capitulation_signal},
    "slv_057_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_057_capitulation_signal},
    "slv_058_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_058_capitulation_signal},
    "slv_059_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_059_capitulation_signal},
    "slv_060_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_060_capitulation_signal},
    "slv_061_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_061_capitulation_signal},
    "slv_062_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_062_capitulation_signal},
    "slv_063_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_063_capitulation_signal},
    "slv_064_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_064_capitulation_signal},
    "slv_065_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_065_capitulation_signal},
    "slv_066_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_066_capitulation_signal},
    "slv_067_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_067_capitulation_signal},
    "slv_068_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_068_capitulation_signal},
    "slv_069_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_069_capitulation_signal},
    "slv_070_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_070_capitulation_signal},
    "slv_071_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_071_capitulation_signal},
    "slv_072_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_072_capitulation_signal},
    "slv_073_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_073_capitulation_signal},
    "slv_074_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_074_capitulation_signal},
    "slv_075_capitulation_signal": {"inputs": ['close', 'assets', 'liabilities', 'workingcapital', 'retainedearnings', 'ebit', 'marketcap', 'revenue'], "func": slv_075_capitulation_signal},
}
