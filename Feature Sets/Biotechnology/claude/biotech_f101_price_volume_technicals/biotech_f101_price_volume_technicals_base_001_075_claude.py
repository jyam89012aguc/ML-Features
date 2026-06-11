"""Family f101 - Price/volume technicals from silver DB metrics | base 001-012."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _range_position(price, low, high):
    return _safe_div(price - low, high - low)


def _drawdown(price, high):
    return _safe_div(price - high, high.abs())


# Price position within 52-week range
def pvt_f101_price_volume_technicals_52w_range_position_base_v001_signal(price, high52w, low52w):
    result = _range_position(price, low52w, high52w)
    return _clean(result)


# Price position within 5-year range
def pvt_f101_price_volume_technicals_5y_range_position_base_v002_signal(price, high5y, low5y):
    result = _range_position(price, low5y, high5y)
    return _clean(result)


# Drawdown from 52-week high
def pvt_f101_price_volume_technicals_52w_drawdown_base_v003_signal(price, high52w):
    result = _drawdown(price, high52w)
    return _clean(result)


# Drawdown from 5-year high
def pvt_f101_price_volume_technicals_5y_drawdown_base_v004_signal(price, high5y):
    result = _drawdown(price, high5y)
    return _clean(result)


# Price premium to 50-day moving average
def pvt_f101_price_volume_technicals_price_vs_ma50d_base_v005_signal(price, ma50d):
    result = _safe_div(price - ma50d, ma50d.abs())
    return _clean(result)


# Price premium to 200-day moving average
def pvt_f101_price_volume_technicals_price_vs_ma200d_base_v006_signal(price, ma200d):
    result = _safe_div(price - ma200d, ma200d.abs())
    return _clean(result)


# 50d/200d moving-average stack
def pvt_f101_price_volume_technicals_ma50d_ma200d_stack_base_v007_signal(ma50d, ma200d):
    result = _safe_div(ma50d - ma200d, ma200d.abs())
    return _clean(result)


# Weekly moving-average stack
def pvt_f101_price_volume_technicals_ma50w_ma200w_stack_base_v008_signal(ma50w, ma200w):
    result = _safe_div(ma50w - ma200w, ma200w.abs())
    return _clean(result)


# Beta spread between short and long horizons
def pvt_f101_price_volume_technicals_beta_term_spread_base_v009_signal(beta1y, beta5y):
    result = beta1y - beta5y
    return _clean(result)


# 52-week drawdown adjusted by 1y beta
def pvt_f101_price_volume_technicals_beta_adjusted_52w_drawdown_base_v010_signal(price, high52w, beta1y):
    result = _drawdown(price, high52w) / (1 + beta1y.abs()).replace(0, np.nan)
    return _clean(result)


# 1y return relative to beta
def pvt_f101_price_volume_technicals_return1y_beta_efficiency_base_v011_signal(return1y, beta1y):
    result = _safe_div(return1y, 1 + beta1y.abs())
    return _clean(result)


# 5y return relative to beta
def pvt_f101_price_volume_technicals_return5y_beta_efficiency_base_v012_signal(return5y, beta5y):
    result = _safe_div(return5y, 1 + beta5y.abs())
    return _clean(result)
