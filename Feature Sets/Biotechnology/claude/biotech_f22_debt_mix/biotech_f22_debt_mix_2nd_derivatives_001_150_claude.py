"""Family f22 - Debt mix current vs non-current  (D_Capital_Debt) | 2nd derivatives 001-150"""
import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _debt_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _debt_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _debt_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw debtc
def dm_f22_debt_mix_raw_21d_slope_v001_signal(debtc, closeadj):
    base = _mean(debtc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw debtc
def dm_f22_debt_mix_raw_21d_slope_v002_signal(debtc, closeadj):
    base = _mean(debtc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw debtc
def dm_f22_debt_mix_raw_21d_slope_v003_signal(debtc, closeadj):
    base = _mean(debtc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw debtc
def dm_f22_debt_mix_raw_63d_slope_v004_signal(debtc, closeadj):
    base = _mean(debtc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw debtc
def dm_f22_debt_mix_raw_63d_slope_v005_signal(debtc, closeadj):
    base = _mean(debtc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw debtc
def dm_f22_debt_mix_raw_63d_slope_v006_signal(debtc, closeadj):
    base = _mean(debtc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw debtc
def dm_f22_debt_mix_raw_126d_slope_v007_signal(debtc, closeadj):
    base = _mean(debtc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw debtc
def dm_f22_debt_mix_raw_126d_slope_v008_signal(debtc, closeadj):
    base = _mean(debtc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw debtc
def dm_f22_debt_mix_raw_126d_slope_v009_signal(debtc, closeadj):
    base = _mean(debtc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw debtc
def dm_f22_debt_mix_raw_252d_slope_v010_signal(debtc, closeadj):
    base = _mean(debtc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw debtc
def dm_f22_debt_mix_raw_252d_slope_v011_signal(debtc, closeadj):
    base = _mean(debtc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw debtc
def dm_f22_debt_mix_raw_252d_slope_v012_signal(debtc, closeadj):
    base = _mean(debtc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw debtc
def dm_f22_debt_mix_raw_504d_slope_v013_signal(debtc, closeadj):
    base = _mean(debtc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw debtc
def dm_f22_debt_mix_raw_504d_slope_v014_signal(debtc, closeadj):
    base = _mean(debtc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw debtc
def dm_f22_debt_mix_raw_504d_slope_v015_signal(debtc, closeadj):
    base = _mean(debtc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log debtc
def dm_f22_debt_mix_log_21d_slope_v016_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log debtc
def dm_f22_debt_mix_log_21d_slope_v017_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log debtc
def dm_f22_debt_mix_log_21d_slope_v018_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log debtc
def dm_f22_debt_mix_log_63d_slope_v019_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log debtc
def dm_f22_debt_mix_log_63d_slope_v020_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log debtc
def dm_f22_debt_mix_log_63d_slope_v021_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log debtc
def dm_f22_debt_mix_log_126d_slope_v022_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log debtc
def dm_f22_debt_mix_log_126d_slope_v023_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log debtc
def dm_f22_debt_mix_log_126d_slope_v024_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log debtc
def dm_f22_debt_mix_log_252d_slope_v025_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log debtc
def dm_f22_debt_mix_log_252d_slope_v026_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log debtc
def dm_f22_debt_mix_log_252d_slope_v027_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log debtc
def dm_f22_debt_mix_log_504d_slope_v028_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log debtc
def dm_f22_debt_mix_log_504d_slope_v029_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log debtc
def dm_f22_debt_mix_log_504d_slope_v030_signal(debtc, closeadj):
    base = _mean(_debt_mix_log(debtc), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare debtc
def dm_f22_debt_mix_pershare_21d_slope_v031_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare debtc
def dm_f22_debt_mix_pershare_21d_slope_v032_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare debtc
def dm_f22_debt_mix_pershare_21d_slope_v033_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare debtc
def dm_f22_debt_mix_pershare_63d_slope_v034_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare debtc
def dm_f22_debt_mix_pershare_63d_slope_v035_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare debtc
def dm_f22_debt_mix_pershare_63d_slope_v036_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare debtc
def dm_f22_debt_mix_pershare_126d_slope_v037_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare debtc
def dm_f22_debt_mix_pershare_126d_slope_v038_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare debtc
def dm_f22_debt_mix_pershare_126d_slope_v039_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare debtc
def dm_f22_debt_mix_pershare_252d_slope_v040_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare debtc
def dm_f22_debt_mix_pershare_252d_slope_v041_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare debtc
def dm_f22_debt_mix_pershare_252d_slope_v042_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare debtc
def dm_f22_debt_mix_pershare_504d_slope_v043_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare debtc
def dm_f22_debt_mix_pershare_504d_slope_v044_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare debtc
def dm_f22_debt_mix_pershare_504d_slope_v045_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_mix_per_share(debtc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets debtc
def dm_f22_debt_mix_per_assets_21d_slope_v046_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets debtc
def dm_f22_debt_mix_per_assets_21d_slope_v047_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets debtc
def dm_f22_debt_mix_per_assets_21d_slope_v048_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets debtc
def dm_f22_debt_mix_per_assets_63d_slope_v049_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets debtc
def dm_f22_debt_mix_per_assets_63d_slope_v050_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets debtc
def dm_f22_debt_mix_per_assets_63d_slope_v051_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets debtc
def dm_f22_debt_mix_per_assets_126d_slope_v052_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets debtc
def dm_f22_debt_mix_per_assets_126d_slope_v053_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets debtc
def dm_f22_debt_mix_per_assets_126d_slope_v054_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets debtc
def dm_f22_debt_mix_per_assets_252d_slope_v055_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets debtc
def dm_f22_debt_mix_per_assets_252d_slope_v056_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets debtc
def dm_f22_debt_mix_per_assets_252d_slope_v057_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets debtc
def dm_f22_debt_mix_per_assets_504d_slope_v058_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets debtc
def dm_f22_debt_mix_per_assets_504d_slope_v059_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets debtc
def dm_f22_debt_mix_per_assets_504d_slope_v060_signal(debtc, assets):
    base = _mean(_debt_mix_scaled(debtc, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_21d_slope_v061_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_21d_slope_v062_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_21d_slope_v063_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_63d_slope_v064_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_63d_slope_v065_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_63d_slope_v066_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_126d_slope_v067_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_126d_slope_v068_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_126d_slope_v069_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_252d_slope_v070_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_252d_slope_v071_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_252d_slope_v072_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_504d_slope_v073_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_504d_slope_v074_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap debtc
def dm_f22_debt_mix_per_marketcap_504d_slope_v075_signal(debtc, marketcap):
    base = _mean(_debt_mix_scaled(debtc, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity debtc
def dm_f22_debt_mix_per_equity_21d_slope_v076_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity debtc
def dm_f22_debt_mix_per_equity_21d_slope_v077_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity debtc
def dm_f22_debt_mix_per_equity_21d_slope_v078_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity debtc
def dm_f22_debt_mix_per_equity_63d_slope_v079_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity debtc
def dm_f22_debt_mix_per_equity_63d_slope_v080_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity debtc
def dm_f22_debt_mix_per_equity_63d_slope_v081_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity debtc
def dm_f22_debt_mix_per_equity_126d_slope_v082_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity debtc
def dm_f22_debt_mix_per_equity_126d_slope_v083_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity debtc
def dm_f22_debt_mix_per_equity_126d_slope_v084_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity debtc
def dm_f22_debt_mix_per_equity_252d_slope_v085_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity debtc
def dm_f22_debt_mix_per_equity_252d_slope_v086_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity debtc
def dm_f22_debt_mix_per_equity_252d_slope_v087_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity debtc
def dm_f22_debt_mix_per_equity_504d_slope_v088_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity debtc
def dm_f22_debt_mix_per_equity_504d_slope_v089_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity debtc
def dm_f22_debt_mix_per_equity_504d_slope_v090_signal(debtc, equity):
    base = _mean(_debt_mix_scaled(debtc, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std debtc
def dm_f22_debt_mix_std_21d_slope_v091_signal(debtc, closeadj):
    base = _std(debtc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std debtc
def dm_f22_debt_mix_std_21d_slope_v092_signal(debtc, closeadj):
    base = _std(debtc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std debtc
def dm_f22_debt_mix_std_21d_slope_v093_signal(debtc, closeadj):
    base = _std(debtc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std debtc
def dm_f22_debt_mix_std_63d_slope_v094_signal(debtc, closeadj):
    base = _std(debtc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std debtc
def dm_f22_debt_mix_std_63d_slope_v095_signal(debtc, closeadj):
    base = _std(debtc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std debtc
def dm_f22_debt_mix_std_63d_slope_v096_signal(debtc, closeadj):
    base = _std(debtc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std debtc
def dm_f22_debt_mix_std_126d_slope_v097_signal(debtc, closeadj):
    base = _std(debtc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std debtc
def dm_f22_debt_mix_std_126d_slope_v098_signal(debtc, closeadj):
    base = _std(debtc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std debtc
def dm_f22_debt_mix_std_126d_slope_v099_signal(debtc, closeadj):
    base = _std(debtc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std debtc
def dm_f22_debt_mix_std_252d_slope_v100_signal(debtc, closeadj):
    base = _std(debtc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std debtc
def dm_f22_debt_mix_std_252d_slope_v101_signal(debtc, closeadj):
    base = _std(debtc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std debtc
def dm_f22_debt_mix_std_252d_slope_v102_signal(debtc, closeadj):
    base = _std(debtc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std debtc
def dm_f22_debt_mix_std_504d_slope_v103_signal(debtc, closeadj):
    base = _std(debtc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std debtc
def dm_f22_debt_mix_std_504d_slope_v104_signal(debtc, closeadj):
    base = _std(debtc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std debtc
def dm_f22_debt_mix_std_504d_slope_v105_signal(debtc, closeadj):
    base = _std(debtc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm debtc
def dm_f22_debt_mix_ewm_21d_slope_v106_signal(debtc, closeadj):
    base = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm debtc
def dm_f22_debt_mix_ewm_21d_slope_v107_signal(debtc, closeadj):
    base = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm debtc
def dm_f22_debt_mix_ewm_21d_slope_v108_signal(debtc, closeadj):
    base = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm debtc
def dm_f22_debt_mix_ewm_63d_slope_v109_signal(debtc, closeadj):
    base = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm debtc
def dm_f22_debt_mix_ewm_63d_slope_v110_signal(debtc, closeadj):
    base = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm debtc
def dm_f22_debt_mix_ewm_63d_slope_v111_signal(debtc, closeadj):
    base = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm debtc
def dm_f22_debt_mix_ewm_126d_slope_v112_signal(debtc, closeadj):
    base = debtc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm debtc
def dm_f22_debt_mix_ewm_126d_slope_v113_signal(debtc, closeadj):
    base = debtc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm debtc
def dm_f22_debt_mix_ewm_126d_slope_v114_signal(debtc, closeadj):
    base = debtc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm debtc
def dm_f22_debt_mix_ewm_252d_slope_v115_signal(debtc, closeadj):
    base = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm debtc
def dm_f22_debt_mix_ewm_252d_slope_v116_signal(debtc, closeadj):
    base = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm debtc
def dm_f22_debt_mix_ewm_252d_slope_v117_signal(debtc, closeadj):
    base = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm debtc
def dm_f22_debt_mix_ewm_504d_slope_v118_signal(debtc, closeadj):
    base = debtc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm debtc
def dm_f22_debt_mix_ewm_504d_slope_v119_signal(debtc, closeadj):
    base = debtc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm debtc
def dm_f22_debt_mix_ewm_504d_slope_v120_signal(debtc, closeadj):
    base = debtc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq debtc
def dm_f22_debt_mix_sq_21d_slope_v121_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq debtc
def dm_f22_debt_mix_sq_21d_slope_v122_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq debtc
def dm_f22_debt_mix_sq_21d_slope_v123_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq debtc
def dm_f22_debt_mix_sq_63d_slope_v124_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq debtc
def dm_f22_debt_mix_sq_63d_slope_v125_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq debtc
def dm_f22_debt_mix_sq_63d_slope_v126_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq debtc
def dm_f22_debt_mix_sq_126d_slope_v127_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq debtc
def dm_f22_debt_mix_sq_126d_slope_v128_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq debtc
def dm_f22_debt_mix_sq_126d_slope_v129_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq debtc
def dm_f22_debt_mix_sq_252d_slope_v130_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq debtc
def dm_f22_debt_mix_sq_252d_slope_v131_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq debtc
def dm_f22_debt_mix_sq_252d_slope_v132_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq debtc
def dm_f22_debt_mix_sq_504d_slope_v133_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq debtc
def dm_f22_debt_mix_sq_504d_slope_v134_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq debtc
def dm_f22_debt_mix_sq_504d_slope_v135_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z debtc
def dm_f22_debt_mix_z_21d_slope_v136_signal(debtc):
    base = _z(debtc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z debtc
def dm_f22_debt_mix_z_21d_slope_v137_signal(debtc):
    base = _z(debtc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z debtc
def dm_f22_debt_mix_z_21d_slope_v138_signal(debtc):
    base = _z(debtc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z debtc
def dm_f22_debt_mix_z_63d_slope_v139_signal(debtc):
    base = _z(debtc, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z debtc
def dm_f22_debt_mix_z_63d_slope_v140_signal(debtc):
    base = _z(debtc, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z debtc
def dm_f22_debt_mix_z_63d_slope_v141_signal(debtc):
    base = _z(debtc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z debtc
def dm_f22_debt_mix_z_126d_slope_v142_signal(debtc):
    base = _z(debtc, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z debtc
def dm_f22_debt_mix_z_126d_slope_v143_signal(debtc):
    base = _z(debtc, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z debtc
def dm_f22_debt_mix_z_126d_slope_v144_signal(debtc):
    base = _z(debtc, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z debtc
def dm_f22_debt_mix_z_252d_slope_v145_signal(debtc):
    base = _z(debtc, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z debtc
def dm_f22_debt_mix_z_252d_slope_v146_signal(debtc):
    base = _z(debtc, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z debtc
def dm_f22_debt_mix_z_252d_slope_v147_signal(debtc):
    base = _z(debtc, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z debtc
def dm_f22_debt_mix_z_504d_slope_v148_signal(debtc):
    base = _z(debtc, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z debtc
def dm_f22_debt_mix_z_504d_slope_v149_signal(debtc):
    base = _z(debtc, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z debtc
def dm_f22_debt_mix_z_504d_slope_v150_signal(debtc):
    base = _z(debtc, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
