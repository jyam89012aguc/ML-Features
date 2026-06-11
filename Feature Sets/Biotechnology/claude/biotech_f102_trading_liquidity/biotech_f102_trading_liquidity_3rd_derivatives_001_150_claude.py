"""Family f102 - Trading liquidity and tradability | third derivatives 001-012."""
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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _dollar_volume(closeadj, volume):
    return closeadj.abs() * volume.abs()


def tl_f102_trading_liquidity_dollar_volume_21d_accel_v001_signal(closeadj, volume):
    result = _accel(_mean(_dollar_volume(closeadj, volume), 21), 21)
    return _clean(result)


def tl_f102_trading_liquidity_dollar_volume_63d_accel_v002_signal(closeadj, volume):
    result = _accel(_mean(_dollar_volume(closeadj, volume), 63), 21)
    return _clean(result)


def tl_f102_trading_liquidity_dollar_volume_252d_accel_v003_signal(closeadj, volume):
    result = _accel(_mean(_dollar_volume(closeadj, volume), 252), 63)
    return _clean(result)


def tl_f102_trading_liquidity_turnover_63d_accel_v004_signal(closeadj, volume, marketcap):
    base = _safe_div(_mean(_dollar_volume(closeadj, volume), 63), marketcap.abs())
    result = _accel(base, 21)
    return _clean(result)


def tl_f102_trading_liquidity_turnover_252d_accel_v005_signal(closeadj, volume, marketcap):
    base = _safe_div(_mean(_dollar_volume(closeadj, volume), 252), marketcap.abs())
    result = _accel(base, 63)
    return _clean(result)


def tl_f102_trading_liquidity_volume_vs_1m_accel_v006_signal(volume, volumeavg1m):
    result = _accel(_safe_div(volume, volumeavg1m.abs()), 21)
    return _clean(result)


def tl_f102_trading_liquidity_volume_vs_3m_accel_v007_signal(volume, volumeavg3m):
    result = _accel(_safe_div(volume, volumeavg3m.abs()), 21)
    return _clean(result)


def tl_f102_trading_liquidity_volume_average_accel_accel_v008_signal(volumeavg1m, volumeavg3m):
    base = _safe_div(volumeavg1m - volumeavg3m, volumeavg3m.abs())
    result = _accel(base, 21)
    return _clean(result)


def tl_f102_trading_liquidity_dollar_volume_drought_accel_v009_signal(closeadj, volume):
    dv = _dollar_volume(closeadj, volume)
    result = _accel(_safe_div(_mean(dv, 63), _mean(dv, 252).abs()), 21)
    return _clean(result)


def tl_f102_trading_liquidity_dollar_volume_volatility_21d_accel_v010_signal(closeadj, volume):
    result = _accel(_std(_dollar_volume(closeadj, volume), 21), 21)
    return _clean(result)


def tl_f102_trading_liquidity_dollar_volume_cv_63d_accel_v011_signal(closeadj, volume):
    dv = _dollar_volume(closeadj, volume)
    result = _accel(_safe_div(_std(dv, 63), _mean(dv, 63).abs()), 21)
    return _clean(result)


def tl_f102_trading_liquidity_price_impact_21d_accel_v012_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    base = _mean(_safe_div(ret, _dollar_volume(closeadj, volume).abs()), 21)
    result = _accel(base, 21)
    return _clean(result)
