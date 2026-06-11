"""Generated capitulation features for 83_insider_buy_cluster: insider buy clustering.
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

def ibc_001_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 63)

def ibc_002_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def ibc_003_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def ibc_004_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 504)

def ibc_005_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibc_006_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibc_007_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def ibc_008_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibc_009_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibc_010_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibc_011_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibc_012_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_013_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibc_014_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(126)

def ibc_015_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _z(x, 252)

def ibc_016_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, y)

def ibc_017_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x - y, y.abs())

def ibc_018_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _rank(x, 21)

def ibc_019_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibc_020_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibc_021_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close))

def ibc_022_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibc_023_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibc_024_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ibc_025_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ibc_026_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_027_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ibc_028_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(504)

def ibc_029_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _z(x, 756)

def ibc_030_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, y)

def ibc_031_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x - y, y.abs())

def ibc_032_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _rank(x, 126)

def ibc_033_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ibc_034_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ibc_035_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close))

def ibc_036_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ibc_037_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ibc_038_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ibc_039_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ibc_040_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_041_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ibc_042_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(21)

def ibc_043_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _z(x, 63)

def ibc_044_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, y)

def ibc_045_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x - y, y.abs())

def ibc_046_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _rank(x, 504)

def ibc_047_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibc_048_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibc_049_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close))

def ibc_050_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibc_051_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibc_052_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibc_053_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibc_054_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_055_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibc_056_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(126)

def ibc_057_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _z(x, 252)

def ibc_058_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, y)

def ibc_059_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x - y, y.abs())

def ibc_060_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _rank(x, 21)

def ibc_061_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibc_062_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibc_063_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close))

def ibc_064_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibc_065_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibc_066_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ibc_067_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ibc_068_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_069_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ibc_070_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(504)

def ibc_071_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 756)

def ibc_072_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def ibc_073_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def ibc_074_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 126)

def ibc_075_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

INSIDER_BUY_CLUSTER_REGISTRY_001_075 = {
    "ibc_001_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_001_capitulation_signal},
    "ibc_002_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_002_capitulation_signal},
    "ibc_003_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_003_capitulation_signal},
    "ibc_004_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_004_capitulation_signal},
    "ibc_005_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_005_capitulation_signal},
    "ibc_006_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_006_capitulation_signal},
    "ibc_007_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_007_capitulation_signal},
    "ibc_008_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_008_capitulation_signal},
    "ibc_009_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_009_capitulation_signal},
    "ibc_010_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_010_capitulation_signal},
    "ibc_011_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_011_capitulation_signal},
    "ibc_012_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_012_capitulation_signal},
    "ibc_013_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_013_capitulation_signal},
    "ibc_014_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_014_capitulation_signal},
    "ibc_015_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_015_capitulation_signal},
    "ibc_016_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_016_capitulation_signal},
    "ibc_017_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_017_capitulation_signal},
    "ibc_018_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_018_capitulation_signal},
    "ibc_019_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_019_capitulation_signal},
    "ibc_020_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_020_capitulation_signal},
    "ibc_021_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_021_capitulation_signal},
    "ibc_022_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_022_capitulation_signal},
    "ibc_023_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_023_capitulation_signal},
    "ibc_024_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_024_capitulation_signal},
    "ibc_025_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_025_capitulation_signal},
    "ibc_026_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_026_capitulation_signal},
    "ibc_027_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_027_capitulation_signal},
    "ibc_028_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_028_capitulation_signal},
    "ibc_029_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_029_capitulation_signal},
    "ibc_030_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_030_capitulation_signal},
    "ibc_031_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_031_capitulation_signal},
    "ibc_032_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_032_capitulation_signal},
    "ibc_033_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_033_capitulation_signal},
    "ibc_034_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_034_capitulation_signal},
    "ibc_035_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_035_capitulation_signal},
    "ibc_036_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_036_capitulation_signal},
    "ibc_037_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_037_capitulation_signal},
    "ibc_038_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_038_capitulation_signal},
    "ibc_039_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_039_capitulation_signal},
    "ibc_040_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_040_capitulation_signal},
    "ibc_041_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_041_capitulation_signal},
    "ibc_042_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_042_capitulation_signal},
    "ibc_043_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_043_capitulation_signal},
    "ibc_044_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_044_capitulation_signal},
    "ibc_045_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_045_capitulation_signal},
    "ibc_046_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_046_capitulation_signal},
    "ibc_047_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_047_capitulation_signal},
    "ibc_048_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_048_capitulation_signal},
    "ibc_049_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_049_capitulation_signal},
    "ibc_050_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_050_capitulation_signal},
    "ibc_051_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_051_capitulation_signal},
    "ibc_052_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_052_capitulation_signal},
    "ibc_053_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_053_capitulation_signal},
    "ibc_054_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_054_capitulation_signal},
    "ibc_055_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_055_capitulation_signal},
    "ibc_056_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_056_capitulation_signal},
    "ibc_057_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_057_capitulation_signal},
    "ibc_058_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_058_capitulation_signal},
    "ibc_059_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_059_capitulation_signal},
    "ibc_060_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_060_capitulation_signal},
    "ibc_061_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_061_capitulation_signal},
    "ibc_062_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_062_capitulation_signal},
    "ibc_063_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_063_capitulation_signal},
    "ibc_064_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_064_capitulation_signal},
    "ibc_065_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_065_capitulation_signal},
    "ibc_066_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_066_capitulation_signal},
    "ibc_067_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_067_capitulation_signal},
    "ibc_068_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_068_capitulation_signal},
    "ibc_069_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_069_capitulation_signal},
    "ibc_070_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_070_capitulation_signal},
    "ibc_071_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_071_capitulation_signal},
    "ibc_072_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_072_capitulation_signal},
    "ibc_073_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_073_capitulation_signal},
    "ibc_074_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_074_capitulation_signal},
    "ibc_075_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_075_capitulation_signal},
}
