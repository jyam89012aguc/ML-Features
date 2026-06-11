"""Family f36 - Asset composition | silver DB additions third derivatives 151-156."""
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


def ac_f36_asset_composition_current_investments_assets_252d_accel_v151_signal(investmentsc, assets):
    return _clean(_accel(_mean(_safe_div(investmentsc, assets.abs()), 252), 63))


def ac_f36_asset_composition_noncurrent_investments_assets_252d_accel_v152_signal(investmentsnc, assets):
    return _clean(_accel(_mean(_safe_div(investmentsnc, assets.abs()), 252), 63))


def ac_f36_asset_composition_total_investments_assets_252d_accel_v153_signal(investments, assets):
    return _clean(_accel(_mean(_safe_div(investments, assets.abs()), 252), 63))


def ac_f36_asset_composition_cash_plus_current_investments_assets_252d_accel_v154_signal(cashneq, investmentsc, assets):
    return _clean(_accel(_mean(_safe_div(cashneq + investmentsc, assets.abs()), 252), 63))


def ac_f36_asset_composition_ppne_assets_252d_accel_v155_signal(ppnenet, assets):
    return _clean(_accel(_mean(_safe_div(ppnenet, assets.abs()), 252), 63))


def ac_f36_asset_composition_current_vs_noncurrent_investments_252d_accel_v156_signal(investmentsc, investmentsnc):
    return _clean(_accel(_mean(_safe_div(investmentsc, investmentsnc.abs()), 252), 63))
