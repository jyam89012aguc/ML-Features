"""Family f101 - Price/volume technicals from silver DB metrics | third derivatives 001-012."""
import numpy as np
import pandas as pd


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    slope = _slope(s, w)
    return slope.diff(periods=w)


def _range_position(price, low, high):
    return _safe_div(price - low, high - low)


def _drawdown(price, high):
    return _safe_div(price - high, high.abs())


def pvt_f101_price_volume_technicals_52w_range_position_accel_v001_signal(price, high52w, low52w):
    result = _accel(_range_position(price, low52w, high52w), 21)
    return _clean(result)


def pvt_f101_price_volume_technicals_5y_range_position_accel_v002_signal(price, high5y, low5y):
    result = _accel(_range_position(price, low5y, high5y), 63)
    return _clean(result)


def pvt_f101_price_volume_technicals_52w_drawdown_accel_v003_signal(price, high52w):
    result = _accel(_drawdown(price, high52w), 21)
    return _clean(result)


def pvt_f101_price_volume_technicals_5y_drawdown_accel_v004_signal(price, high5y):
    result = _accel(_drawdown(price, high5y), 63)
    return _clean(result)


def pvt_f101_price_volume_technicals_price_vs_ma50d_accel_v005_signal(price, ma50d):
    result = _accel(_safe_div(price - ma50d, ma50d.abs()), 21)
    return _clean(result)


def pvt_f101_price_volume_technicals_price_vs_ma200d_accel_v006_signal(price, ma200d):
    result = _accel(_safe_div(price - ma200d, ma200d.abs()), 63)
    return _clean(result)


def pvt_f101_price_volume_technicals_ma50d_ma200d_stack_accel_v007_signal(ma50d, ma200d):
    result = _accel(_safe_div(ma50d - ma200d, ma200d.abs()), 21)
    return _clean(result)


def pvt_f101_price_volume_technicals_ma50w_ma200w_stack_accel_v008_signal(ma50w, ma200w):
    result = _accel(_safe_div(ma50w - ma200w, ma200w.abs()), 63)
    return _clean(result)


def pvt_f101_price_volume_technicals_beta_term_spread_accel_v009_signal(beta1y, beta5y):
    result = _accel(beta1y - beta5y, 63)
    return _clean(result)


def pvt_f101_price_volume_technicals_beta_adjusted_52w_drawdown_accel_v010_signal(price, high52w, beta1y):
    base = _drawdown(price, high52w) / (1 + beta1y.abs()).replace(0, np.nan)
    result = _accel(base, 21)
    return _clean(result)


def pvt_f101_price_volume_technicals_return1y_beta_efficiency_accel_v011_signal(return1y, beta1y):
    result = _accel(_safe_div(return1y, 1 + beta1y.abs()), 63)
    return _clean(result)


def pvt_f101_price_volume_technicals_return5y_beta_efficiency_accel_v012_signal(return5y, beta5y):
    result = _accel(_safe_div(return5y, 1 + beta5y.abs()), 252)
    return _clean(result)
