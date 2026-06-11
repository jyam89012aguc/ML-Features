"""Family f73 - Market cap | silver DB liquidity additions third derivatives 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _dollar_volume(closeadj, volume):
    return closeadj.abs() * volume.abs()


def mc_f73_market_cap_dollar_volume_to_marketcap_21d_accel_v151_signal(closeadj, volume, marketcap):
    return _clean(_accel(_safe_div(_mean(_dollar_volume(closeadj, volume), 21), marketcap.abs()), 21))


def mc_f73_market_cap_dollar_volume_to_marketcap_63d_accel_v152_signal(closeadj, volume, marketcap):
    return _clean(_accel(_safe_div(_mean(_dollar_volume(closeadj, volume), 63), marketcap.abs()), 21))


def mc_f73_market_cap_dollar_volume_to_marketcap_252d_accel_v153_signal(closeadj, volume, marketcap):
    return _clean(_accel(_safe_div(_mean(_dollar_volume(closeadj, volume), 252), marketcap.abs()), 63))


def mc_f73_market_cap_volume_to_marketcap_63d_accel_v154_signal(volume, marketcap):
    return _clean(_accel(_safe_div(_mean(volume.abs(), 63), marketcap.abs()), 21))


def mc_f73_market_cap_volume_shock_marketcap_21d_accel_v155_signal(volume, volumeavg1m, marketcap):
    return _clean(_accel(_safe_div(_mean(_safe_div(volume, volumeavg1m.abs()), 21), marketcap.abs()), 21))


def mc_f73_market_cap_liquidity_drought_63d_252d_accel_v156_signal(closeadj, volume):
    dv = _dollar_volume(closeadj, volume)
    return _clean(_accel(_safe_div(_mean(dv, 63), _mean(dv, 252).abs()), 21))
