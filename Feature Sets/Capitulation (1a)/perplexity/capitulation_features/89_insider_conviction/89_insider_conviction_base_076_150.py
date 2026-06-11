"""Generated capitulation features for 89_insider_conviction: insider conviction.
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

def icn_076_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def icn_077_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def icn_078_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def icn_079_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def icn_080_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def icn_081_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def icn_082_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icn_083_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def icn_084_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(21)

def icn_085_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _z(x, 63)

def icn_086_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, y)

def icn_087_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x - y, y.abs())

def icn_088_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _rank(x, 504)

def icn_089_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def icn_090_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def icn_091_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close))

def icn_092_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def icn_093_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def icn_094_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def icn_095_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def icn_096_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icn_097_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def icn_098_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(126)

def icn_099_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _z(x, 252)

def icn_100_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, y)

def icn_101_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x - y, y.abs())

def icn_102_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _rank(x, 21)

def icn_103_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def icn_104_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def icn_105_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close))

def icn_106_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def icn_107_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def icn_108_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def icn_109_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def icn_110_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icn_111_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def icn_112_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(504)

def icn_113_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _z(x, 756)

def icn_114_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, y)

def icn_115_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x - y, y.abs())

def icn_116_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _rank(x, 126)

def icn_117_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def icn_118_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def icn_119_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close))

def icn_120_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def icn_121_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def icn_122_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def icn_123_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def icn_124_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icn_125_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def icn_126_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(21)

def icn_127_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _z(x, 63)

def icn_128_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, y)

def icn_129_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x - y, y.abs())

def icn_130_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _rank(x, 504)

def icn_131_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def icn_132_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def icn_133_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close))

def icn_134_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def icn_135_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def icn_136_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def icn_137_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def icn_138_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def icn_139_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def icn_140_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(126)

def icn_141_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 252)

def icn_142_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def icn_143_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def icn_144_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 21)

def icn_145_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def icn_146_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def icn_147_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def icn_148_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def icn_149_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def icn_150_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

INSIDER_CONVICTION_REGISTRY_076_150 = {
    "icn_076_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_076_capitulation_signal},
    "icn_077_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_077_capitulation_signal},
    "icn_078_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_078_capitulation_signal},
    "icn_079_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_079_capitulation_signal},
    "icn_080_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_080_capitulation_signal},
    "icn_081_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_081_capitulation_signal},
    "icn_082_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_082_capitulation_signal},
    "icn_083_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_083_capitulation_signal},
    "icn_084_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_084_capitulation_signal},
    "icn_085_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_085_capitulation_signal},
    "icn_086_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_086_capitulation_signal},
    "icn_087_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_087_capitulation_signal},
    "icn_088_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_088_capitulation_signal},
    "icn_089_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_089_capitulation_signal},
    "icn_090_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_090_capitulation_signal},
    "icn_091_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_091_capitulation_signal},
    "icn_092_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_092_capitulation_signal},
    "icn_093_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_093_capitulation_signal},
    "icn_094_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_094_capitulation_signal},
    "icn_095_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_095_capitulation_signal},
    "icn_096_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_096_capitulation_signal},
    "icn_097_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_097_capitulation_signal},
    "icn_098_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_098_capitulation_signal},
    "icn_099_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_099_capitulation_signal},
    "icn_100_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_100_capitulation_signal},
    "icn_101_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_101_capitulation_signal},
    "icn_102_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_102_capitulation_signal},
    "icn_103_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_103_capitulation_signal},
    "icn_104_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_104_capitulation_signal},
    "icn_105_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_105_capitulation_signal},
    "icn_106_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_106_capitulation_signal},
    "icn_107_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_107_capitulation_signal},
    "icn_108_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_108_capitulation_signal},
    "icn_109_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_109_capitulation_signal},
    "icn_110_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_110_capitulation_signal},
    "icn_111_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_111_capitulation_signal},
    "icn_112_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_112_capitulation_signal},
    "icn_113_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_113_capitulation_signal},
    "icn_114_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_114_capitulation_signal},
    "icn_115_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_115_capitulation_signal},
    "icn_116_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_116_capitulation_signal},
    "icn_117_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_117_capitulation_signal},
    "icn_118_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_118_capitulation_signal},
    "icn_119_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_119_capitulation_signal},
    "icn_120_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_120_capitulation_signal},
    "icn_121_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_121_capitulation_signal},
    "icn_122_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_122_capitulation_signal},
    "icn_123_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_123_capitulation_signal},
    "icn_124_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_124_capitulation_signal},
    "icn_125_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_125_capitulation_signal},
    "icn_126_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_126_capitulation_signal},
    "icn_127_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_127_capitulation_signal},
    "icn_128_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_128_capitulation_signal},
    "icn_129_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_129_capitulation_signal},
    "icn_130_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_130_capitulation_signal},
    "icn_131_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_131_capitulation_signal},
    "icn_132_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_132_capitulation_signal},
    "icn_133_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_133_capitulation_signal},
    "icn_134_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_134_capitulation_signal},
    "icn_135_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_135_capitulation_signal},
    "icn_136_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_136_capitulation_signal},
    "icn_137_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_137_capitulation_signal},
    "icn_138_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_138_capitulation_signal},
    "icn_139_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_139_capitulation_signal},
    "icn_140_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_140_capitulation_signal},
    "icn_141_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_141_capitulation_signal},
    "icn_142_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_142_capitulation_signal},
    "icn_143_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_143_capitulation_signal},
    "icn_144_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_144_capitulation_signal},
    "icn_145_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_145_capitulation_signal},
    "icn_146_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_146_capitulation_signal},
    "icn_147_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_147_capitulation_signal},
    "icn_148_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_148_capitulation_signal},
    "icn_149_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_149_capitulation_signal},
    "icn_150_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": icn_150_capitulation_signal},
}
