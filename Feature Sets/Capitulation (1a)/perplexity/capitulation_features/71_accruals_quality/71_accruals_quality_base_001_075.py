"""Generated capitulation features for 71_accruals_quality: accrual/cash divergence.
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

def acq_001_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _z(x, 63)

def acq_002_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, y)

def acq_003_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def acq_004_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 504)

def acq_005_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def acq_006_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def acq_007_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close))

def acq_008_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def acq_009_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def acq_010_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def acq_011_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def acq_012_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_013_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def acq_014_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(126)

def acq_015_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _z(x, 252)

def acq_016_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def acq_017_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x - y, y.abs())

def acq_018_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _rank(x, 21)

def acq_019_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def acq_020_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def acq_021_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def acq_022_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def acq_023_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def acq_024_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def acq_025_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def acq_026_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_027_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def acq_028_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(504)

def acq_029_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _z(x, 756)

def acq_030_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x, y)

def acq_031_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def acq_032_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _rank(x, 126)

def acq_033_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def acq_034_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def acq_035_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close))

def acq_036_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def acq_037_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def acq_038_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def acq_039_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def acq_040_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_041_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def acq_042_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(21)

def acq_043_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _z(x, 63)

def acq_044_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x, y)

def acq_045_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x - y, y.abs())

def acq_046_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _rank(x, 504)

def acq_047_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def acq_048_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def acq_049_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close))

def acq_050_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def acq_051_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def acq_052_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def acq_053_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def acq_054_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_055_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def acq_056_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(126)

def acq_057_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _z(x, 252)

def acq_058_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, y)

def acq_059_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x - y, y.abs())

def acq_060_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _rank(x, 21)

def acq_061_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def acq_062_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def acq_063_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x, _s(close))

def acq_064_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def acq_065_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def acq_066_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def acq_067_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def acq_068_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def acq_069_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def acq_070_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(504)

def acq_071_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(assets, close)
    return _z(x, 756)

def acq_072_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(assets, close)
    y = _align_to_close(workingcapital, close)
    return _div(x, y)

def acq_073_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(workingcapital, close)
    y = _align_to_close(receivables, close)
    return _div(x - y, y.abs())

def acq_074_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(receivables, close)
    y = _align_to_close(netinc, close)
    return _rank(x, 126)

def acq_075_capitulation_signal(close, netinc, ncfo, assets, workingcapital, receivables):
    x = _align_to_close(netinc, close)
    y = _align_to_close(ncfo, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

ACCRUALS_QUALITY_REGISTRY_001_075 = {
    "acq_001_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_001_capitulation_signal},
    "acq_002_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_002_capitulation_signal},
    "acq_003_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_003_capitulation_signal},
    "acq_004_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_004_capitulation_signal},
    "acq_005_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_005_capitulation_signal},
    "acq_006_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_006_capitulation_signal},
    "acq_007_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_007_capitulation_signal},
    "acq_008_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_008_capitulation_signal},
    "acq_009_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_009_capitulation_signal},
    "acq_010_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_010_capitulation_signal},
    "acq_011_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_011_capitulation_signal},
    "acq_012_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_012_capitulation_signal},
    "acq_013_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_013_capitulation_signal},
    "acq_014_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_014_capitulation_signal},
    "acq_015_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_015_capitulation_signal},
    "acq_016_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_016_capitulation_signal},
    "acq_017_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_017_capitulation_signal},
    "acq_018_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_018_capitulation_signal},
    "acq_019_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_019_capitulation_signal},
    "acq_020_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_020_capitulation_signal},
    "acq_021_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_021_capitulation_signal},
    "acq_022_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_022_capitulation_signal},
    "acq_023_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_023_capitulation_signal},
    "acq_024_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_024_capitulation_signal},
    "acq_025_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_025_capitulation_signal},
    "acq_026_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_026_capitulation_signal},
    "acq_027_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_027_capitulation_signal},
    "acq_028_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_028_capitulation_signal},
    "acq_029_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_029_capitulation_signal},
    "acq_030_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_030_capitulation_signal},
    "acq_031_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_031_capitulation_signal},
    "acq_032_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_032_capitulation_signal},
    "acq_033_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_033_capitulation_signal},
    "acq_034_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_034_capitulation_signal},
    "acq_035_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_035_capitulation_signal},
    "acq_036_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_036_capitulation_signal},
    "acq_037_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_037_capitulation_signal},
    "acq_038_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_038_capitulation_signal},
    "acq_039_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_039_capitulation_signal},
    "acq_040_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_040_capitulation_signal},
    "acq_041_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_041_capitulation_signal},
    "acq_042_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_042_capitulation_signal},
    "acq_043_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_043_capitulation_signal},
    "acq_044_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_044_capitulation_signal},
    "acq_045_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_045_capitulation_signal},
    "acq_046_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_046_capitulation_signal},
    "acq_047_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_047_capitulation_signal},
    "acq_048_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_048_capitulation_signal},
    "acq_049_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_049_capitulation_signal},
    "acq_050_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_050_capitulation_signal},
    "acq_051_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_051_capitulation_signal},
    "acq_052_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_052_capitulation_signal},
    "acq_053_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_053_capitulation_signal},
    "acq_054_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_054_capitulation_signal},
    "acq_055_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_055_capitulation_signal},
    "acq_056_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_056_capitulation_signal},
    "acq_057_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_057_capitulation_signal},
    "acq_058_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_058_capitulation_signal},
    "acq_059_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_059_capitulation_signal},
    "acq_060_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_060_capitulation_signal},
    "acq_061_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_061_capitulation_signal},
    "acq_062_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_062_capitulation_signal},
    "acq_063_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_063_capitulation_signal},
    "acq_064_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_064_capitulation_signal},
    "acq_065_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_065_capitulation_signal},
    "acq_066_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_066_capitulation_signal},
    "acq_067_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_067_capitulation_signal},
    "acq_068_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_068_capitulation_signal},
    "acq_069_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_069_capitulation_signal},
    "acq_070_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_070_capitulation_signal},
    "acq_071_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_071_capitulation_signal},
    "acq_072_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_072_capitulation_signal},
    "acq_073_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_073_capitulation_signal},
    "acq_074_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_074_capitulation_signal},
    "acq_075_capitulation_signal": {"inputs": ['close', 'netinc', 'ncfo', 'assets', 'workingcapital', 'receivables'], "func": acq_075_capitulation_signal},
}
