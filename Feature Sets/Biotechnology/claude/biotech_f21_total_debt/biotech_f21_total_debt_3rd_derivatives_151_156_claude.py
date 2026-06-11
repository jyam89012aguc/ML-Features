"""Family f21 - Total debt | silver DB additions third derivatives 151-156."""
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


def td_f21_total_debt_noncurrent_debt_assets_63d_accel_v151_signal(debtnc, assets):
    return _clean(_accel(_mean(_safe_div(debtnc, assets.abs()), 63), 21))


def td_f21_total_debt_noncurrent_debt_assets_252d_accel_v152_signal(debtnc, assets):
    return _clean(_accel(_mean(_safe_div(debtnc, assets.abs()), 252), 63))


def td_f21_total_debt_noncurrent_debt_marketcap_63d_accel_v153_signal(debtnc, marketcap):
    return _clean(_accel(_mean(_safe_div(debtnc, marketcap.abs()), 63), 21))


def td_f21_total_debt_noncurrent_debt_marketcap_252d_accel_v154_signal(debtnc, marketcap):
    return _clean(_accel(_mean(_safe_div(debtnc, marketcap.abs()), 252), 63))


def td_f21_total_debt_debt_usd_assets_252d_accel_v155_signal(debtusd, assets):
    return _clean(_accel(_mean(_safe_div(debtusd, assets.abs()), 252), 63))


def td_f21_total_debt_net_debt_issuance_252d_accel_v156_signal(ncfdebt, debt):
    return _clean(_accel(_mean(_safe_div(ncfdebt, debt.abs()), 252), 63))
