"""Family f97 - Multi-year price context | silver DB additions third derivatives 151-156."""
import numpy as np
import pandas as pd


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _range_position(price, low, high):
    return _safe_div(price - low, high - low)


def _drawdown(price, high):
    return _safe_div(price - high, high.abs())


def mypc_f97_multi_year_price_context_52w_range_position_accel_v151_signal(price, high52w, low52w):
    return _clean(_accel(_range_position(price, low52w, high52w), 21))


def mypc_f97_multi_year_price_context_5y_range_position_accel_v152_signal(price, high5y, low5y):
    return _clean(_accel(_range_position(price, low5y, high5y), 63))


def mypc_f97_multi_year_price_context_52w_drawdown_accel_v153_signal(price, high52w):
    return _clean(_accel(_drawdown(price, high52w), 21))


def mypc_f97_multi_year_price_context_5y_drawdown_accel_v154_signal(price, high5y):
    return _clean(_accel(_drawdown(price, high5y), 63))


def mypc_f97_multi_year_price_context_beta_adjusted_52w_drawdown_accel_v155_signal(price, high52w, beta1y):
    base = _drawdown(price, high52w) / (1 + beta1y.abs()).replace(0, np.nan)
    return _clean(_accel(base, 21))


def mypc_f97_multi_year_price_context_beta_adjusted_5y_drawdown_accel_v156_signal(price, high5y, beta5y):
    base = _drawdown(price, high5y) / (1 + beta5y.abs()).replace(0, np.nan)
    return _clean(_accel(base, 63))
