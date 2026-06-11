"""Generated capitulation features for 70_dilution_acceleration: share count growth.
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

def dla_076_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def dla_077_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def dla_078_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def dla_079_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def dla_080_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def dla_081_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def dla_082_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_083_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def dla_084_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).pct_change(21)

def dla_085_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _z(x, 63)

def dla_086_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x, y)

def dla_087_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x - y, y.abs())

def dla_088_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _rank(x, 504)

def dla_089_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def dla_090_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def dla_091_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x, _s(close))

def dla_092_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def dla_093_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dla_094_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def dla_095_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def dla_096_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_097_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def dla_098_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(126)

def dla_099_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _z(x, 252)

def dla_100_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x, y)

def dla_101_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x - y, y.abs())

def dla_102_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _rank(x, 21)

def dla_103_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def dla_104_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def dla_105_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x, _s(close))

def dla_106_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def dla_107_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def dla_108_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def dla_109_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def dla_110_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_111_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def dla_112_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(504)

def dla_113_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _z(x, 756)

def dla_114_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x, y)

def dla_115_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x - y, y.abs())

def dla_116_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _rank(x, 126)

def dla_117_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def dla_118_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def dla_119_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x, _s(close))

def dla_120_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def dla_121_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def dla_122_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def dla_123_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def dla_124_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_125_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def dla_126_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).pct_change(21)

def dla_127_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _z(x, 63)

def dla_128_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, y)

def dla_129_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x - y, y.abs())

def dla_130_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _rank(x, 504)

def dla_131_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def dla_132_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def dla_133_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close))

def dla_134_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def dla_135_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def dla_136_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def dla_137_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def dla_138_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def dla_139_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def dla_140_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).pct_change(126)

def dla_141_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _z(x, 252)

def dla_142_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, y)

def dla_143_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x - y, y.abs())

def dla_144_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return _rank(x, 21)

def dla_145_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def dla_146_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(shareswa, close)
    y = _align_to_close(sharefactor, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def dla_147_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharefactor, close)
    y = _align_to_close(marketcap, close)
    return _div(x, _s(close))

def dla_148_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(marketcap, close)
    y = _align_to_close(equity, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def dla_149_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(equity, close)
    y = _align_to_close(sharesbas, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def dla_150_capitulation_signal(close, sharesbas, shareswa, sharefactor, marketcap, equity):
    x = _align_to_close(sharesbas, close)
    y = _align_to_close(shareswa, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

DILUTION_ACCELERATION_REGISTRY_076_150 = {
    "dla_076_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_076_capitulation_signal},
    "dla_077_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_077_capitulation_signal},
    "dla_078_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_078_capitulation_signal},
    "dla_079_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_079_capitulation_signal},
    "dla_080_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_080_capitulation_signal},
    "dla_081_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_081_capitulation_signal},
    "dla_082_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_082_capitulation_signal},
    "dla_083_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_083_capitulation_signal},
    "dla_084_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_084_capitulation_signal},
    "dla_085_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_085_capitulation_signal},
    "dla_086_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_086_capitulation_signal},
    "dla_087_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_087_capitulation_signal},
    "dla_088_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_088_capitulation_signal},
    "dla_089_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_089_capitulation_signal},
    "dla_090_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_090_capitulation_signal},
    "dla_091_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_091_capitulation_signal},
    "dla_092_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_092_capitulation_signal},
    "dla_093_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_093_capitulation_signal},
    "dla_094_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_094_capitulation_signal},
    "dla_095_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_095_capitulation_signal},
    "dla_096_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_096_capitulation_signal},
    "dla_097_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_097_capitulation_signal},
    "dla_098_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_098_capitulation_signal},
    "dla_099_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_099_capitulation_signal},
    "dla_100_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_100_capitulation_signal},
    "dla_101_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_101_capitulation_signal},
    "dla_102_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_102_capitulation_signal},
    "dla_103_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_103_capitulation_signal},
    "dla_104_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_104_capitulation_signal},
    "dla_105_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_105_capitulation_signal},
    "dla_106_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_106_capitulation_signal},
    "dla_107_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_107_capitulation_signal},
    "dla_108_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_108_capitulation_signal},
    "dla_109_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_109_capitulation_signal},
    "dla_110_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_110_capitulation_signal},
    "dla_111_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_111_capitulation_signal},
    "dla_112_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_112_capitulation_signal},
    "dla_113_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_113_capitulation_signal},
    "dla_114_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_114_capitulation_signal},
    "dla_115_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_115_capitulation_signal},
    "dla_116_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_116_capitulation_signal},
    "dla_117_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_117_capitulation_signal},
    "dla_118_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_118_capitulation_signal},
    "dla_119_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_119_capitulation_signal},
    "dla_120_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_120_capitulation_signal},
    "dla_121_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_121_capitulation_signal},
    "dla_122_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_122_capitulation_signal},
    "dla_123_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_123_capitulation_signal},
    "dla_124_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_124_capitulation_signal},
    "dla_125_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_125_capitulation_signal},
    "dla_126_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_126_capitulation_signal},
    "dla_127_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_127_capitulation_signal},
    "dla_128_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_128_capitulation_signal},
    "dla_129_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_129_capitulation_signal},
    "dla_130_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_130_capitulation_signal},
    "dla_131_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_131_capitulation_signal},
    "dla_132_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_132_capitulation_signal},
    "dla_133_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_133_capitulation_signal},
    "dla_134_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_134_capitulation_signal},
    "dla_135_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_135_capitulation_signal},
    "dla_136_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_136_capitulation_signal},
    "dla_137_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_137_capitulation_signal},
    "dla_138_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_138_capitulation_signal},
    "dla_139_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_139_capitulation_signal},
    "dla_140_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_140_capitulation_signal},
    "dla_141_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_141_capitulation_signal},
    "dla_142_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_142_capitulation_signal},
    "dla_143_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_143_capitulation_signal},
    "dla_144_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_144_capitulation_signal},
    "dla_145_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_145_capitulation_signal},
    "dla_146_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_146_capitulation_signal},
    "dla_147_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_147_capitulation_signal},
    "dla_148_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_148_capitulation_signal},
    "dla_149_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_149_capitulation_signal},
    "dla_150_capitulation_signal": {"inputs": ['close', 'sharesbas', 'shareswa', 'sharefactor', 'marketcap', 'equity'], "func": dla_150_capitulation_signal},
}
