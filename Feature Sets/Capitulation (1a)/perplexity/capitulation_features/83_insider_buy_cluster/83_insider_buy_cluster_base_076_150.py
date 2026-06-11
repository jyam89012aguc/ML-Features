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

def ibc_076_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ibc_077_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def ibc_078_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ibc_079_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ibc_080_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ibc_081_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ibc_082_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_083_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ibc_084_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(21)

def ibc_085_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _z(x, 63)

def ibc_086_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, y)

def ibc_087_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x - y, y.abs())

def ibc_088_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _rank(x, 504)

def ibc_089_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibc_090_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibc_091_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close))

def ibc_092_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibc_093_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibc_094_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibc_095_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibc_096_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_097_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibc_098_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(126)

def ibc_099_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _z(x, 252)

def ibc_100_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, y)

def ibc_101_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x - y, y.abs())

def ibc_102_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _rank(x, 21)

def ibc_103_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibc_104_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibc_105_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close))

def ibc_106_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibc_107_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibc_108_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def ibc_109_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def ibc_110_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_111_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def ibc_112_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(504)

def ibc_113_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _z(x, 756)

def ibc_114_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, y)

def ibc_115_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x - y, y.abs())

def ibc_116_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _rank(x, 126)

def ibc_117_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def ibc_118_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def ibc_119_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close))

def ibc_120_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def ibc_121_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def ibc_122_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def ibc_123_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def ibc_124_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_125_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def ibc_126_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(21)

def ibc_127_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _z(x, 63)

def ibc_128_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, y)

def ibc_129_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x - y, y.abs())

def ibc_130_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _rank(x, 504)

def ibc_131_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def ibc_132_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def ibc_133_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close))

def ibc_134_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def ibc_135_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def ibc_136_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def ibc_137_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def ibc_138_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def ibc_139_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def ibc_140_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(126)

def ibc_141_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 252)

def ibc_142_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def ibc_143_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def ibc_144_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 21)

def ibc_145_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def ibc_146_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def ibc_147_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def ibc_148_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def ibc_149_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def ibc_150_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

INSIDER_BUY_CLUSTER_REGISTRY_076_150 = {
    "ibc_076_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_076_capitulation_signal},
    "ibc_077_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_077_capitulation_signal},
    "ibc_078_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_078_capitulation_signal},
    "ibc_079_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_079_capitulation_signal},
    "ibc_080_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_080_capitulation_signal},
    "ibc_081_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_081_capitulation_signal},
    "ibc_082_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_082_capitulation_signal},
    "ibc_083_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_083_capitulation_signal},
    "ibc_084_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_084_capitulation_signal},
    "ibc_085_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_085_capitulation_signal},
    "ibc_086_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_086_capitulation_signal},
    "ibc_087_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_087_capitulation_signal},
    "ibc_088_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_088_capitulation_signal},
    "ibc_089_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_089_capitulation_signal},
    "ibc_090_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_090_capitulation_signal},
    "ibc_091_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_091_capitulation_signal},
    "ibc_092_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_092_capitulation_signal},
    "ibc_093_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_093_capitulation_signal},
    "ibc_094_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_094_capitulation_signal},
    "ibc_095_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_095_capitulation_signal},
    "ibc_096_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_096_capitulation_signal},
    "ibc_097_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_097_capitulation_signal},
    "ibc_098_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_098_capitulation_signal},
    "ibc_099_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_099_capitulation_signal},
    "ibc_100_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_100_capitulation_signal},
    "ibc_101_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_101_capitulation_signal},
    "ibc_102_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_102_capitulation_signal},
    "ibc_103_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_103_capitulation_signal},
    "ibc_104_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_104_capitulation_signal},
    "ibc_105_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_105_capitulation_signal},
    "ibc_106_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_106_capitulation_signal},
    "ibc_107_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_107_capitulation_signal},
    "ibc_108_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_108_capitulation_signal},
    "ibc_109_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_109_capitulation_signal},
    "ibc_110_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_110_capitulation_signal},
    "ibc_111_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_111_capitulation_signal},
    "ibc_112_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_112_capitulation_signal},
    "ibc_113_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_113_capitulation_signal},
    "ibc_114_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_114_capitulation_signal},
    "ibc_115_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_115_capitulation_signal},
    "ibc_116_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_116_capitulation_signal},
    "ibc_117_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_117_capitulation_signal},
    "ibc_118_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_118_capitulation_signal},
    "ibc_119_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_119_capitulation_signal},
    "ibc_120_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_120_capitulation_signal},
    "ibc_121_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_121_capitulation_signal},
    "ibc_122_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_122_capitulation_signal},
    "ibc_123_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_123_capitulation_signal},
    "ibc_124_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_124_capitulation_signal},
    "ibc_125_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_125_capitulation_signal},
    "ibc_126_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_126_capitulation_signal},
    "ibc_127_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_127_capitulation_signal},
    "ibc_128_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_128_capitulation_signal},
    "ibc_129_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_129_capitulation_signal},
    "ibc_130_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_130_capitulation_signal},
    "ibc_131_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_131_capitulation_signal},
    "ibc_132_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_132_capitulation_signal},
    "ibc_133_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_133_capitulation_signal},
    "ibc_134_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_134_capitulation_signal},
    "ibc_135_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_135_capitulation_signal},
    "ibc_136_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_136_capitulation_signal},
    "ibc_137_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_137_capitulation_signal},
    "ibc_138_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_138_capitulation_signal},
    "ibc_139_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_139_capitulation_signal},
    "ibc_140_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_140_capitulation_signal},
    "ibc_141_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_141_capitulation_signal},
    "ibc_142_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_142_capitulation_signal},
    "ibc_143_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_143_capitulation_signal},
    "ibc_144_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_144_capitulation_signal},
    "ibc_145_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_145_capitulation_signal},
    "ibc_146_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_146_capitulation_signal},
    "ibc_147_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_147_capitulation_signal},
    "ibc_148_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_148_capitulation_signal},
    "ibc_149_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_149_capitulation_signal},
    "ibc_150_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": ibc_150_capitulation_signal},
}
