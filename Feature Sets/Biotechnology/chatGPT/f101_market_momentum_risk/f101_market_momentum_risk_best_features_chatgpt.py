"""Family f101 - Source-backed market momentum and risk context.

Sharadar tables: METRICS
Fields: beta1y, beta5y, dividendyieldforward, dividendyieldtrailing, high52w,
high5y, low52w, low5y, ma50d, ma200d, ma50w, ma200w, price, return1y,
return5y, returnytd, volume, volumeavg1m, volumeavg3m.

These features fill the main silverdb coverage gap left by f086-f091: the
existing market families use OHLCV history, but not the precomputed METRICS
table context.
"""
import numpy as np
import pandas as pd


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _z(s, w):
    return _safe_div(s - _mean(s, w), _std(s, w))


def _spread(a, b):
    return a - b


# Price trend versus moving-average anchors.
def mmr_f101_price_to_ma50d_signal(price, ma50d):
    return _clean(_safe_div(price, ma50d) - 1.0)


def mmr_f101_price_to_ma200d_signal(price, ma200d):
    return _clean(_safe_div(price, ma200d) - 1.0)


def mmr_f101_ma50d_to_ma200d_signal(ma50d, ma200d):
    return _clean(_safe_div(ma50d, ma200d) - 1.0)


def mmr_f101_price_to_ma50w_signal(price, ma50w):
    return _clean(_safe_div(price, ma50w) - 1.0)


def mmr_f101_price_to_ma200w_signal(price, ma200w):
    return _clean(_safe_div(price, ma200w) - 1.0)


def mmr_f101_ma50w_to_ma200w_signal(ma50w, ma200w):
    return _clean(_safe_div(ma50w, ma200w) - 1.0)


def mmr_f101_daily_weekly_trend_agreement_signal(price, ma50d, ma200d, ma50w, ma200w):
    daily = (_safe_div(price, ma50d) - 1.0) + (_safe_div(ma50d, ma200d) - 1.0)
    weekly = (_safe_div(price, ma50w) - 1.0) + (_safe_div(ma50w, ma200w) - 1.0)
    return _clean(daily + weekly)


# Position inside source-provided high/low ranges.
def mmr_f101_price_position_52w_signal(price, high52w, low52w):
    return _clean(_safe_div(price - low52w, high52w - low52w))


def mmr_f101_price_drawdown_from_52w_high_signal(price, high52w):
    return _clean(_safe_div(price, high52w) - 1.0)


def mmr_f101_price_rebound_from_52w_low_signal(price, low52w):
    return _clean(_safe_div(price, low52w) - 1.0)


def mmr_f101_price_position_5y_signal(price, high5y, low5y):
    return _clean(_safe_div(price - low5y, high5y - low5y))


def mmr_f101_price_drawdown_from_5y_high_signal(price, high5y):
    return _clean(_safe_div(price, high5y) - 1.0)


def mmr_f101_price_rebound_from_5y_low_signal(price, low5y):
    return _clean(_safe_div(price, low5y) - 1.0)


def mmr_f101_52w_range_width_signal(high52w, low52w, price):
    return _clean(_safe_div(high52w - low52w, price))


def mmr_f101_5y_range_width_signal(high5y, low5y, price):
    return _clean(_safe_div(high5y - low5y, price))


# Return stack and acceleration.
def mmr_f101_return_ytd_signal(returnytd):
    return _clean(returnytd)


def mmr_f101_return_1y_signal(return1y):
    return _clean(return1y)


def mmr_f101_return_5y_signal(return5y):
    return _clean(return5y)


def mmr_f101_return_1y_minus_ytd_signal(return1y, returnytd):
    return _clean(_spread(return1y, returnytd))


def mmr_f101_return_5y_minus_1y_signal(return5y, return1y):
    return _clean(_spread(return5y, return1y))


def mmr_f101_return_blend_signal(returnytd, return1y, return5y):
    return _clean((0.50 * returnytd) + (0.35 * return1y) + (0.15 * return5y))


def mmr_f101_return_consistency_signal(returnytd, return1y, return5y):
    frame = pd.concat([returnytd, return1y, return5y], axis=1)
    return _clean(frame.mean(axis=1) / frame.std(axis=1).replace(0, np.nan))


def mmr_f101_positive_return_breadth_signal(returnytd, return1y, return5y):
    frame = pd.concat([returnytd, return1y, return5y], axis=1)
    return _clean(frame.gt(0).sum(axis=1) / frame.notna().sum(axis=1).replace(0, np.nan))


# Beta and risk-adjusted momentum.
def mmr_f101_beta_1y_signal(beta1y):
    return _clean(beta1y)


def mmr_f101_beta_5y_signal(beta5y):
    return _clean(beta5y)


def mmr_f101_beta_term_spread_signal(beta1y, beta5y):
    return _clean(beta1y - beta5y)


def mmr_f101_abs_beta_1y_signal(beta1y):
    return _clean(beta1y.abs())


def mmr_f101_return_1y_per_beta_1y_signal(return1y, beta1y):
    return _clean(_safe_div(return1y, beta1y.abs()))


def mmr_f101_return_ytd_per_beta_1y_signal(returnytd, beta1y):
    return _clean(_safe_div(returnytd, beta1y.abs()))


def mmr_f101_momentum_risk_balance_signal(returnytd, return1y, beta1y):
    return _clean(_safe_div((returnytd + return1y) / 2.0, 1.0 + beta1y.abs()))


# Liquidity context from source average volume fields.
def mmr_f101_volume_to_avg1m_signal(volume, volumeavg1m):
    return _clean(_safe_div(volume, volumeavg1m) - 1.0)


def mmr_f101_volume_to_avg3m_signal(volume, volumeavg3m):
    return _clean(_safe_div(volume, volumeavg3m) - 1.0)


def mmr_f101_volumeavg1m_to_3m_signal(volumeavg1m, volumeavg3m):
    return _clean(_safe_div(volumeavg1m, volumeavg3m) - 1.0)


def mmr_f101_dollar_volume_signal(price, volume):
    return _clean(price * volume)


def mmr_f101_avg1m_dollar_volume_signal(price, volumeavg1m):
    return _clean(price * volumeavg1m)


def mmr_f101_avg3m_dollar_volume_signal(price, volumeavg3m):
    return _clean(price * volumeavg3m)


def mmr_f101_log_avg3m_dollar_volume_signal(price, volumeavg3m):
    return _clean(np.log((price * volumeavg3m).abs().replace(0, np.nan)))


# Dividend yield is usually sparse for biotech, but useful as a maturity flag.
def mmr_f101_forward_dividend_yield_signal(dividendyieldforward):
    return _clean(dividendyieldforward)


def mmr_f101_trailing_dividend_yield_signal(dividendyieldtrailing):
    return _clean(dividendyieldtrailing)


def mmr_f101_dividend_yield_spread_signal(dividendyieldforward, dividendyieldtrailing):
    return _clean(dividendyieldforward - dividendyieldtrailing)


# Rolling stabilizers for model-ready variants.
def mmr_f101_return_blend_63d_mean_signal(returnytd, return1y, return5y):
    return _clean(_mean(mmr_f101_return_blend_signal(returnytd, return1y, return5y), 63))


def mmr_f101_return_blend_252d_z_signal(returnytd, return1y, return5y):
    return _clean(_z(mmr_f101_return_blend_signal(returnytd, return1y, return5y), 252))


def mmr_f101_trend_agreement_63d_mean_signal(price, ma50d, ma200d, ma50w, ma200w):
    return _clean(_mean(mmr_f101_daily_weekly_trend_agreement_signal(price, ma50d, ma200d, ma50w, ma200w), 63))


def mmr_f101_volume_shock_63d_z_signal(volume, volumeavg3m):
    return _clean(_z(mmr_f101_volume_to_avg3m_signal(volume, volumeavg3m), 63))
