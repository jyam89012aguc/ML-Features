"""Generated capitulation features for 90_insider_silence: insider silence.
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

def isl_001_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 63)

def isl_002_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def isl_003_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def isl_004_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 504)

def isl_005_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def isl_006_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def isl_007_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def isl_008_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def isl_009_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def isl_010_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def isl_011_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def isl_012_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_013_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def isl_014_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(126)

def isl_015_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _z(x, 252)

def isl_016_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, y)

def isl_017_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x - y, y.abs())

def isl_018_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _rank(x, 21)

def isl_019_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def isl_020_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def isl_021_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close))

def isl_022_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def isl_023_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def isl_024_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def isl_025_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def isl_026_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_027_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def isl_028_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(504)

def isl_029_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _z(x, 756)

def isl_030_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, y)

def isl_031_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x - y, y.abs())

def isl_032_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _rank(x, 126)

def isl_033_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def isl_034_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def isl_035_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close))

def isl_036_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def isl_037_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def isl_038_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def isl_039_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def isl_040_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_041_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def isl_042_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(21)

def isl_043_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _z(x, 63)

def isl_044_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, y)

def isl_045_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x - y, y.abs())

def isl_046_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _rank(x, 504)

def isl_047_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def isl_048_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def isl_049_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close))

def isl_050_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def isl_051_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def isl_052_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def isl_053_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def isl_054_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_055_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def isl_056_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(126)

def isl_057_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _z(x, 252)

def isl_058_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, y)

def isl_059_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x - y, y.abs())

def isl_060_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _rank(x, 21)

def isl_061_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def isl_062_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def isl_063_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close))

def isl_064_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def isl_065_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def isl_066_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def isl_067_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def isl_068_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_069_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def isl_070_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(504)

def isl_071_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 756)

def isl_072_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def isl_073_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def isl_074_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 126)

def isl_075_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

INSIDER_SILENCE_REGISTRY_001_075 = {
    "isl_001_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_001_capitulation_signal},
    "isl_002_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_002_capitulation_signal},
    "isl_003_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_003_capitulation_signal},
    "isl_004_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_004_capitulation_signal},
    "isl_005_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_005_capitulation_signal},
    "isl_006_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_006_capitulation_signal},
    "isl_007_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_007_capitulation_signal},
    "isl_008_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_008_capitulation_signal},
    "isl_009_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_009_capitulation_signal},
    "isl_010_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_010_capitulation_signal},
    "isl_011_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_011_capitulation_signal},
    "isl_012_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_012_capitulation_signal},
    "isl_013_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_013_capitulation_signal},
    "isl_014_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_014_capitulation_signal},
    "isl_015_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_015_capitulation_signal},
    "isl_016_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_016_capitulation_signal},
    "isl_017_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_017_capitulation_signal},
    "isl_018_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_018_capitulation_signal},
    "isl_019_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_019_capitulation_signal},
    "isl_020_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_020_capitulation_signal},
    "isl_021_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_021_capitulation_signal},
    "isl_022_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_022_capitulation_signal},
    "isl_023_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_023_capitulation_signal},
    "isl_024_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_024_capitulation_signal},
    "isl_025_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_025_capitulation_signal},
    "isl_026_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_026_capitulation_signal},
    "isl_027_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_027_capitulation_signal},
    "isl_028_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_028_capitulation_signal},
    "isl_029_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_029_capitulation_signal},
    "isl_030_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_030_capitulation_signal},
    "isl_031_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_031_capitulation_signal},
    "isl_032_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_032_capitulation_signal},
    "isl_033_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_033_capitulation_signal},
    "isl_034_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_034_capitulation_signal},
    "isl_035_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_035_capitulation_signal},
    "isl_036_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_036_capitulation_signal},
    "isl_037_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_037_capitulation_signal},
    "isl_038_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_038_capitulation_signal},
    "isl_039_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_039_capitulation_signal},
    "isl_040_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_040_capitulation_signal},
    "isl_041_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_041_capitulation_signal},
    "isl_042_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_042_capitulation_signal},
    "isl_043_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_043_capitulation_signal},
    "isl_044_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_044_capitulation_signal},
    "isl_045_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_045_capitulation_signal},
    "isl_046_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_046_capitulation_signal},
    "isl_047_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_047_capitulation_signal},
    "isl_048_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_048_capitulation_signal},
    "isl_049_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_049_capitulation_signal},
    "isl_050_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_050_capitulation_signal},
    "isl_051_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_051_capitulation_signal},
    "isl_052_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_052_capitulation_signal},
    "isl_053_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_053_capitulation_signal},
    "isl_054_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_054_capitulation_signal},
    "isl_055_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_055_capitulation_signal},
    "isl_056_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_056_capitulation_signal},
    "isl_057_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_057_capitulation_signal},
    "isl_058_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_058_capitulation_signal},
    "isl_059_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_059_capitulation_signal},
    "isl_060_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_060_capitulation_signal},
    "isl_061_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_061_capitulation_signal},
    "isl_062_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_062_capitulation_signal},
    "isl_063_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_063_capitulation_signal},
    "isl_064_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_064_capitulation_signal},
    "isl_065_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_065_capitulation_signal},
    "isl_066_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_066_capitulation_signal},
    "isl_067_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_067_capitulation_signal},
    "isl_068_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_068_capitulation_signal},
    "isl_069_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_069_capitulation_signal},
    "isl_070_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_070_capitulation_signal},
    "isl_071_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_071_capitulation_signal},
    "isl_072_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_072_capitulation_signal},
    "isl_073_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_073_capitulation_signal},
    "isl_074_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_074_capitulation_signal},
    "isl_075_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_075_capitulation_signal},
}
