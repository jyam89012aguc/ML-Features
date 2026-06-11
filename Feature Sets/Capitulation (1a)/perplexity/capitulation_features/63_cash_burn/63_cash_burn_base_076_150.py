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

def cbr_076_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def cbr_077_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x, _s(close))

def cbr_078_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def cbr_079_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def cbr_080_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def cbr_081_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def cbr_082_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_083_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def cbr_084_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(21)

def cbr_085_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _z(x, 63)

def cbr_086_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, y)

def cbr_087_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x - y, y.abs())

def cbr_088_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _rank(x, 504)

def cbr_089_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def cbr_090_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def cbr_091_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def cbr_092_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def cbr_093_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def cbr_094_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def cbr_095_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def cbr_096_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_097_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def cbr_098_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).pct_change(126)

def cbr_099_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _z(x, 252)

def cbr_100_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def cbr_101_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x - y, y.abs())

def cbr_102_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 21)

def cbr_103_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def cbr_104_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def cbr_105_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close))

def cbr_106_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def cbr_107_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def cbr_108_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def cbr_109_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def cbr_110_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_111_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def cbr_112_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).pct_change(504)

def cbr_113_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _z(x, 756)

def cbr_114_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(x, y)

def cbr_115_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x - y, y.abs())

def cbr_116_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _rank(x, 126)

def cbr_117_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def cbr_118_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def cbr_119_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x, _s(close))

def cbr_120_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def cbr_121_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def cbr_122_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def cbr_123_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def cbr_124_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_125_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def cbr_126_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).pct_change(21)

def cbr_127_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _z(x, 63)

def cbr_128_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, y)

def cbr_129_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x - y, y.abs())

def cbr_130_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _rank(x, 504)

def cbr_131_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def cbr_132_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def cbr_133_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(x, _s(close))

def cbr_134_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def cbr_135_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def cbr_136_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def cbr_137_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def cbr_138_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def cbr_139_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def cbr_140_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).pct_change(126)

def cbr_141_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _z(x, 252)

def cbr_142_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, y)

def cbr_143_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return _div(x - y, y.abs())

def cbr_144_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _rank(x, 21)

def cbr_145_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(cashneq, close)
    y = _align_to_close(opex, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def cbr_146_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(opex, close)
    y = _align_to_close(capex, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def cbr_147_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(capex, close)
    y = _align_to_close(ncfo, close)
    return _div(x, _s(close))

def cbr_148_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(ncfo, close)
    y = _align_to_close(debt, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def cbr_149_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(debt, close)
    y = _align_to_close(fcf, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def cbr_150_capitulation_signal(close, fcf, cashneq, opex, capex, ncfo, debt):
    x = _align_to_close(fcf, close)
    y = _align_to_close(cashneq, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

CASH_BURN_REGISTRY_076_150 = {
    "cbr_076_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_076_capitulation_signal},
    "cbr_077_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_077_capitulation_signal},
    "cbr_078_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_078_capitulation_signal},
    "cbr_079_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_079_capitulation_signal},
    "cbr_080_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_080_capitulation_signal},
    "cbr_081_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_081_capitulation_signal},
    "cbr_082_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_082_capitulation_signal},
    "cbr_083_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_083_capitulation_signal},
    "cbr_084_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_084_capitulation_signal},
    "cbr_085_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_085_capitulation_signal},
    "cbr_086_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_086_capitulation_signal},
    "cbr_087_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_087_capitulation_signal},
    "cbr_088_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_088_capitulation_signal},
    "cbr_089_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_089_capitulation_signal},
    "cbr_090_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_090_capitulation_signal},
    "cbr_091_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_091_capitulation_signal},
    "cbr_092_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_092_capitulation_signal},
    "cbr_093_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_093_capitulation_signal},
    "cbr_094_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_094_capitulation_signal},
    "cbr_095_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_095_capitulation_signal},
    "cbr_096_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_096_capitulation_signal},
    "cbr_097_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_097_capitulation_signal},
    "cbr_098_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_098_capitulation_signal},
    "cbr_099_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_099_capitulation_signal},
    "cbr_100_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_100_capitulation_signal},
    "cbr_101_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_101_capitulation_signal},
    "cbr_102_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_102_capitulation_signal},
    "cbr_103_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_103_capitulation_signal},
    "cbr_104_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_104_capitulation_signal},
    "cbr_105_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_105_capitulation_signal},
    "cbr_106_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_106_capitulation_signal},
    "cbr_107_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_107_capitulation_signal},
    "cbr_108_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_108_capitulation_signal},
    "cbr_109_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_109_capitulation_signal},
    "cbr_110_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_110_capitulation_signal},
    "cbr_111_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_111_capitulation_signal},
    "cbr_112_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_112_capitulation_signal},
    "cbr_113_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_113_capitulation_signal},
    "cbr_114_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_114_capitulation_signal},
    "cbr_115_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_115_capitulation_signal},
    "cbr_116_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_116_capitulation_signal},
    "cbr_117_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_117_capitulation_signal},
    "cbr_118_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_118_capitulation_signal},
    "cbr_119_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_119_capitulation_signal},
    "cbr_120_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_120_capitulation_signal},
    "cbr_121_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_121_capitulation_signal},
    "cbr_122_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_122_capitulation_signal},
    "cbr_123_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_123_capitulation_signal},
    "cbr_124_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_124_capitulation_signal},
    "cbr_125_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_125_capitulation_signal},
    "cbr_126_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_126_capitulation_signal},
    "cbr_127_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_127_capitulation_signal},
    "cbr_128_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_128_capitulation_signal},
    "cbr_129_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_129_capitulation_signal},
    "cbr_130_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_130_capitulation_signal},
    "cbr_131_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_131_capitulation_signal},
    "cbr_132_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_132_capitulation_signal},
    "cbr_133_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_133_capitulation_signal},
    "cbr_134_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_134_capitulation_signal},
    "cbr_135_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_135_capitulation_signal},
    "cbr_136_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_136_capitulation_signal},
    "cbr_137_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_137_capitulation_signal},
    "cbr_138_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_138_capitulation_signal},
    "cbr_139_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_139_capitulation_signal},
    "cbr_140_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_140_capitulation_signal},
    "cbr_141_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_141_capitulation_signal},
    "cbr_142_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_142_capitulation_signal},
    "cbr_143_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_143_capitulation_signal},
    "cbr_144_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_144_capitulation_signal},
    "cbr_145_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_145_capitulation_signal},
    "cbr_146_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_146_capitulation_signal},
    "cbr_147_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_147_capitulation_signal},
    "cbr_148_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_148_capitulation_signal},
    "cbr_149_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_149_capitulation_signal},
    "cbr_150_capitulation_signal": {"inputs": ['close', 'fcf', 'cashneq', 'opex', 'capex', 'ncfo', 'debt'], "func": cbr_150_capitulation_signal},
}
