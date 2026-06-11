"""Generated capitulation features for 63_cash_burn: negative free cash flow/runway.
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

def cbr_001_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _z(x, 63)

def cbr_002_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, y)

def cbr_003_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x - y, y.abs())

def cbr_004_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _rank(x, 504)

def cbr_005_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def cbr_006_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def cbr_007_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def cbr_008_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def cbr_009_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def cbr_010_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def cbr_011_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def cbr_012_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_013_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def cbr_014_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).pct_change(126)

def cbr_015_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _z(x, 252)

def cbr_016_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def cbr_017_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x - y, y.abs())

def cbr_018_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 21)

def cbr_019_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def cbr_020_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def cbr_021_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close))

def cbr_022_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def cbr_023_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def cbr_024_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def cbr_025_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def cbr_026_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_027_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def cbr_028_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(504)

def cbr_029_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _z(x, 756)

def cbr_030_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def cbr_031_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def cbr_032_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _rank(x, 126)

def cbr_033_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def cbr_034_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def cbr_035_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x, _s(close))

def cbr_036_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def cbr_037_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def cbr_038_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def cbr_039_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def cbr_040_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_041_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def cbr_042_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(21)

def cbr_043_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _z(x, 63)

def cbr_044_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, y)

def cbr_045_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x - y, y.abs())

def cbr_046_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _rank(x, 504)

def cbr_047_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def cbr_048_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def cbr_049_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def cbr_050_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def cbr_051_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def cbr_052_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def cbr_053_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def cbr_054_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_055_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def cbr_056_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).pct_change(126)

def cbr_057_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _z(x, 252)

def cbr_058_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def cbr_059_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x - y, y.abs())

def cbr_060_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 21)

def cbr_061_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def cbr_062_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def cbr_063_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close))

def cbr_064_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def cbr_065_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def cbr_066_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def cbr_067_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def cbr_068_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_069_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def cbr_070_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(504)

def cbr_071_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _z(x, 756)

def cbr_072_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def cbr_073_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def cbr_074_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _rank(x, 126)

def cbr_075_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

CASH_BURN_REGISTRY_001_075 = {
    "cbr_001_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_001_capitulation_signal},
    "cbr_002_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_002_capitulation_signal},
    "cbr_003_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_003_capitulation_signal},
    "cbr_004_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_004_capitulation_signal},
    "cbr_005_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_005_capitulation_signal},
    "cbr_006_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_006_capitulation_signal},
    "cbr_007_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_007_capitulation_signal},
    "cbr_008_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_008_capitulation_signal},
    "cbr_009_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_009_capitulation_signal},
    "cbr_010_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_010_capitulation_signal},
    "cbr_011_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_011_capitulation_signal},
    "cbr_012_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_012_capitulation_signal},
    "cbr_013_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_013_capitulation_signal},
    "cbr_014_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_014_capitulation_signal},
    "cbr_015_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_015_capitulation_signal},
    "cbr_016_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_016_capitulation_signal},
    "cbr_017_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_017_capitulation_signal},
    "cbr_018_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_018_capitulation_signal},
    "cbr_019_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_019_capitulation_signal},
    "cbr_020_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_020_capitulation_signal},
    "cbr_021_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_021_capitulation_signal},
    "cbr_022_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_022_capitulation_signal},
    "cbr_023_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_023_capitulation_signal},
    "cbr_024_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_024_capitulation_signal},
    "cbr_025_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_025_capitulation_signal},
    "cbr_026_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_026_capitulation_signal},
    "cbr_027_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_027_capitulation_signal},
    "cbr_028_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_028_capitulation_signal},
    "cbr_029_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_029_capitulation_signal},
    "cbr_030_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_030_capitulation_signal},
    "cbr_031_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_031_capitulation_signal},
    "cbr_032_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_032_capitulation_signal},
    "cbr_033_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_033_capitulation_signal},
    "cbr_034_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_034_capitulation_signal},
    "cbr_035_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_035_capitulation_signal},
    "cbr_036_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_036_capitulation_signal},
    "cbr_037_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_037_capitulation_signal},
    "cbr_038_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_038_capitulation_signal},
    "cbr_039_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_039_capitulation_signal},
    "cbr_040_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_040_capitulation_signal},
    "cbr_041_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_041_capitulation_signal},
    "cbr_042_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_042_capitulation_signal},
    "cbr_043_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_043_capitulation_signal},
    "cbr_044_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_044_capitulation_signal},
    "cbr_045_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_045_capitulation_signal},
    "cbr_046_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_046_capitulation_signal},
    "cbr_047_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_047_capitulation_signal},
    "cbr_048_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_048_capitulation_signal},
    "cbr_049_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_049_capitulation_signal},
    "cbr_050_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_050_capitulation_signal},
    "cbr_051_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_051_capitulation_signal},
    "cbr_052_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_052_capitulation_signal},
    "cbr_053_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_053_capitulation_signal},
    "cbr_054_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_054_capitulation_signal},
    "cbr_055_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_055_capitulation_signal},
    "cbr_056_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_056_capitulation_signal},
    "cbr_057_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_057_capitulation_signal},
    "cbr_058_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_058_capitulation_signal},
    "cbr_059_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_059_capitulation_signal},
    "cbr_060_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_060_capitulation_signal},
    "cbr_061_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_061_capitulation_signal},
    "cbr_062_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_062_capitulation_signal},
    "cbr_063_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_063_capitulation_signal},
    "cbr_064_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_064_capitulation_signal},
    "cbr_065_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_065_capitulation_signal},
    "cbr_066_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_066_capitulation_signal},
    "cbr_067_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_067_capitulation_signal},
    "cbr_068_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_068_capitulation_signal},
    "cbr_069_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_069_capitulation_signal},
    "cbr_070_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_070_capitulation_signal},
    "cbr_071_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_071_capitulation_signal},
    "cbr_072_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_072_capitulation_signal},
    "cbr_073_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_073_capitulation_signal},
    "cbr_074_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_074_capitulation_signal},
    "cbr_075_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_075_capitulation_signal},
}
