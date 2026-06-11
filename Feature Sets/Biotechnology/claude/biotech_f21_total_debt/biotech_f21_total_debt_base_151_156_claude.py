"""Family f21 - Total debt | silver DB additions base 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def td_f21_total_debt_noncurrent_debt_assets_63d_base_v151_signal(debtnc, assets):
    return _clean(_mean(_safe_div(debtnc, assets.abs()), 63))


def td_f21_total_debt_noncurrent_debt_assets_252d_base_v152_signal(debtnc, assets):
    return _clean(_mean(_safe_div(debtnc, assets.abs()), 252))


def td_f21_total_debt_noncurrent_debt_marketcap_63d_base_v153_signal(debtnc, marketcap):
    return _clean(_mean(_safe_div(debtnc, marketcap.abs()), 63))


def td_f21_total_debt_noncurrent_debt_marketcap_252d_base_v154_signal(debtnc, marketcap):
    return _clean(_mean(_safe_div(debtnc, marketcap.abs()), 252))


def td_f21_total_debt_debt_usd_assets_252d_base_v155_signal(debtusd, assets):
    return _clean(_mean(_safe_div(debtusd, assets.abs()), 252))


def td_f21_total_debt_net_debt_issuance_252d_base_v156_signal(ncfdebt, debt):
    return _clean(_mean(_safe_div(ncfdebt, debt.abs()), 252))
