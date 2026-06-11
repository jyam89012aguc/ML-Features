"""Family f102 - Trading liquidity and tradability | base 001-012."""
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


def _dollar_volume(closeadj, volume):
    return closeadj.abs() * volume.abs()


# 21d dollar volume
def tl_f102_trading_liquidity_dollar_volume_21d_base_v001_signal(closeadj, volume):
    result = _mean(_dollar_volume(closeadj, volume), 21)
    return _clean(result)


# 63d dollar volume
def tl_f102_trading_liquidity_dollar_volume_63d_base_v002_signal(closeadj, volume):
    result = _mean(_dollar_volume(closeadj, volume), 63)
    return _clean(result)


# 252d dollar volume
def tl_f102_trading_liquidity_dollar_volume_252d_base_v003_signal(closeadj, volume):
    result = _mean(_dollar_volume(closeadj, volume), 252)
    return _clean(result)


# 63d dollar volume / market cap
def tl_f102_trading_liquidity_turnover_63d_base_v004_signal(closeadj, volume, marketcap):
    result = _safe_div(_mean(_dollar_volume(closeadj, volume), 63), marketcap.abs())
    return _clean(result)


# 252d dollar volume / market cap
def tl_f102_trading_liquidity_turnover_252d_base_v005_signal(closeadj, volume, marketcap):
    result = _safe_div(_mean(_dollar_volume(closeadj, volume), 252), marketcap.abs())
    return _clean(result)


# Current volume versus 1m average
def tl_f102_trading_liquidity_volume_vs_1m_base_v006_signal(volume, volumeavg1m):
    result = _safe_div(volume, volumeavg1m.abs())
    return _clean(result)


# Current volume versus 3m average
def tl_f102_trading_liquidity_volume_vs_3m_base_v007_signal(volume, volumeavg3m):
    result = _safe_div(volume, volumeavg3m.abs())
    return _clean(result)


# 1m volume average versus 3m volume average
def tl_f102_trading_liquidity_volume_average_accel_base_v008_signal(volumeavg1m, volumeavg3m):
    result = _safe_div(volumeavg1m - volumeavg3m, volumeavg3m.abs())
    return _clean(result)


# 63d liquidity drought: dollar volume relative to its own 252d average
def tl_f102_trading_liquidity_dollar_volume_drought_base_v009_signal(closeadj, volume):
    dv = _dollar_volume(closeadj, volume)
    result = _safe_div(_mean(dv, 63), _mean(dv, 252).abs())
    return _clean(result)


# 21d dollar volume volatility
def tl_f102_trading_liquidity_dollar_volume_volatility_21d_base_v010_signal(closeadj, volume):
    result = _std(_dollar_volume(closeadj, volume), 21)
    return _clean(result)


# 63d dollar volume volatility / mean
def tl_f102_trading_liquidity_dollar_volume_cv_63d_base_v011_signal(closeadj, volume):
    dv = _dollar_volume(closeadj, volume)
    result = _safe_div(_std(dv, 63), _mean(dv, 63).abs())
    return _clean(result)


# 21d price impact proxy: absolute return per dollar volume
def tl_f102_trading_liquidity_price_impact_21d_base_v012_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    result = _mean(_safe_div(ret, _dollar_volume(closeadj, volume).abs()), 21)
    return _clean(result)
