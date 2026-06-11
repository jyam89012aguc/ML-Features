"""Family f22 - Debt mix | silver DB additions base 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def dm_f22_debt_mix_current_noncurrent_ratio_63d_base_v151_signal(debtc, debtnc):
    return _clean(_mean(_safe_div(debtc, debtnc.abs()), 63))


def dm_f22_debt_mix_current_noncurrent_ratio_252d_base_v152_signal(debtc, debtnc):
    return _clean(_mean(_safe_div(debtc, debtnc.abs()), 252))


def dm_f22_debt_mix_noncurrent_share_63d_base_v153_signal(debtnc, debt):
    return _clean(_mean(_safe_div(debtnc, debt.abs()), 63))


def dm_f22_debt_mix_noncurrent_share_252d_base_v154_signal(debtnc, debt):
    return _clean(_mean(_safe_div(debtnc, debt.abs()), 252))


def dm_f22_debt_mix_current_liability_debt_share_252d_base_v155_signal(debtc, liabilitiesc):
    return _clean(_mean(_safe_div(debtc, liabilitiesc.abs()), 252))


def dm_f22_debt_mix_noncurrent_liability_debt_share_252d_base_v156_signal(debtnc, liabilitiesnc):
    return _clean(_mean(_safe_div(debtnc, liabilitiesnc.abs()), 252))
