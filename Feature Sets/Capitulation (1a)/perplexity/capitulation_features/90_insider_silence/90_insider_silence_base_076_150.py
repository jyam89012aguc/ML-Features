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

def isl_076_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def isl_077_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def isl_078_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def isl_079_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def isl_080_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def isl_081_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def isl_082_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_083_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def isl_084_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(21)

def isl_085_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _z(x, 63)

def isl_086_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, y)

def isl_087_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x - y, y.abs())

def isl_088_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _rank(x, 504)

def isl_089_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def isl_090_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def isl_091_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close))

def isl_092_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def isl_093_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def isl_094_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def isl_095_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def isl_096_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_097_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def isl_098_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(126)

def isl_099_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _z(x, 252)

def isl_100_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, y)

def isl_101_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x - y, y.abs())

def isl_102_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _rank(x, 21)

def isl_103_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def isl_104_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def isl_105_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close))

def isl_106_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def isl_107_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def isl_108_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def isl_109_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def isl_110_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_111_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def isl_112_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(504)

def isl_113_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _z(x, 756)

def isl_114_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, y)

def isl_115_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x - y, y.abs())

def isl_116_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _rank(x, 126)

def isl_117_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def isl_118_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def isl_119_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close))

def isl_120_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def isl_121_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def isl_122_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def isl_123_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def isl_124_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_125_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def isl_126_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).pct_change(21)

def isl_127_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _z(x, 63)

def isl_128_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, y)

def isl_129_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x - y, y.abs())

def isl_130_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _rank(x, 504)

def isl_131_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def isl_132_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def isl_133_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close))

def isl_134_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def isl_135_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def isl_136_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def isl_137_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def isl_138_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def isl_139_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def isl_140_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).pct_change(126)

def isl_141_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _z(x, 252)

def isl_142_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, y)

def isl_143_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x - y, y.abs())

def isl_144_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return _rank(x, 21)

def isl_145_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def isl_146_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sells, close)
    y = _align_to_close(insider_buy_value, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def isl_147_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buy_value, close)
    y = _align_to_close(insider_sell_value, close)
    return _div(x, _s(close))

def isl_148_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_sell_value, close)
    y = _align_to_close(insider_txn_count, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def isl_149_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_txn_count, close)
    y = _align_to_close(insider_buys, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def isl_150_capitulation_signal(close, insider_buys, insider_sells, insider_buy_value, insider_sell_value, insider_txn_count):
    x = _align_to_close(insider_buys, close)
    y = _align_to_close(insider_sells, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

INSIDER_SILENCE_REGISTRY_076_150 = {
    "isl_076_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_076_capitulation_signal},
    "isl_077_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_077_capitulation_signal},
    "isl_078_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_078_capitulation_signal},
    "isl_079_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_079_capitulation_signal},
    "isl_080_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_080_capitulation_signal},
    "isl_081_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_081_capitulation_signal},
    "isl_082_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_082_capitulation_signal},
    "isl_083_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_083_capitulation_signal},
    "isl_084_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_084_capitulation_signal},
    "isl_085_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_085_capitulation_signal},
    "isl_086_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_086_capitulation_signal},
    "isl_087_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_087_capitulation_signal},
    "isl_088_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_088_capitulation_signal},
    "isl_089_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_089_capitulation_signal},
    "isl_090_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_090_capitulation_signal},
    "isl_091_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_091_capitulation_signal},
    "isl_092_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_092_capitulation_signal},
    "isl_093_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_093_capitulation_signal},
    "isl_094_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_094_capitulation_signal},
    "isl_095_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_095_capitulation_signal},
    "isl_096_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_096_capitulation_signal},
    "isl_097_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_097_capitulation_signal},
    "isl_098_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_098_capitulation_signal},
    "isl_099_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_099_capitulation_signal},
    "isl_100_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_100_capitulation_signal},
    "isl_101_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_101_capitulation_signal},
    "isl_102_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_102_capitulation_signal},
    "isl_103_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_103_capitulation_signal},
    "isl_104_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_104_capitulation_signal},
    "isl_105_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_105_capitulation_signal},
    "isl_106_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_106_capitulation_signal},
    "isl_107_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_107_capitulation_signal},
    "isl_108_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_108_capitulation_signal},
    "isl_109_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_109_capitulation_signal},
    "isl_110_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_110_capitulation_signal},
    "isl_111_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_111_capitulation_signal},
    "isl_112_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_112_capitulation_signal},
    "isl_113_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_113_capitulation_signal},
    "isl_114_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_114_capitulation_signal},
    "isl_115_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_115_capitulation_signal},
    "isl_116_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_116_capitulation_signal},
    "isl_117_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_117_capitulation_signal},
    "isl_118_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_118_capitulation_signal},
    "isl_119_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_119_capitulation_signal},
    "isl_120_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_120_capitulation_signal},
    "isl_121_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_121_capitulation_signal},
    "isl_122_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_122_capitulation_signal},
    "isl_123_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_123_capitulation_signal},
    "isl_124_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_124_capitulation_signal},
    "isl_125_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_125_capitulation_signal},
    "isl_126_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_126_capitulation_signal},
    "isl_127_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_127_capitulation_signal},
    "isl_128_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_128_capitulation_signal},
    "isl_129_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_129_capitulation_signal},
    "isl_130_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_130_capitulation_signal},
    "isl_131_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_131_capitulation_signal},
    "isl_132_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_132_capitulation_signal},
    "isl_133_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_133_capitulation_signal},
    "isl_134_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_134_capitulation_signal},
    "isl_135_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_135_capitulation_signal},
    "isl_136_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_136_capitulation_signal},
    "isl_137_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_137_capitulation_signal},
    "isl_138_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_138_capitulation_signal},
    "isl_139_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_139_capitulation_signal},
    "isl_140_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_140_capitulation_signal},
    "isl_141_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_141_capitulation_signal},
    "isl_142_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_142_capitulation_signal},
    "isl_143_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_143_capitulation_signal},
    "isl_144_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_144_capitulation_signal},
    "isl_145_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_145_capitulation_signal},
    "isl_146_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_146_capitulation_signal},
    "isl_147_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_147_capitulation_signal},
    "isl_148_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_148_capitulation_signal},
    "isl_149_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_149_capitulation_signal},
    "isl_150_capitulation_signal": {"inputs": ['close', 'insider_buys', 'insider_sells', 'insider_buy_value', 'insider_sell_value', 'insider_txn_count'], "func": isl_150_capitulation_signal},
}
