"""Family f023 - Current versus long-term debt mix (Capital Structure) | Sharadar tables: SF1 | fields: debtc, debtnc, debt | 3rd derivatives 001-150"""
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
def _debt_maturity_mix_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _debt_maturity_mix_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _debt_maturity_mix_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw debtc
def dmm_f023_debt_maturity_mix_raw_21d_accel_v001_signal(debtc, closeadj):
    base = _mean(debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw debtc
def dmm_f023_debt_maturity_mix_raw_21d_accel_v002_signal(debtc, closeadj):
    base = _mean(debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw debtc
def dmm_f023_debt_maturity_mix_raw_21d_accel_v003_signal(debtc, closeadj):
    base = _mean(debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw debtc
def dmm_f023_debt_maturity_mix_raw_63d_accel_v004_signal(debtc, closeadj):
    base = _mean(debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw debtc
def dmm_f023_debt_maturity_mix_raw_63d_accel_v005_signal(debtc, closeadj):
    base = _mean(debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw debtc
def dmm_f023_debt_maturity_mix_raw_63d_accel_v006_signal(debtc, closeadj):
    base = _mean(debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw debtc
def dmm_f023_debt_maturity_mix_raw_126d_accel_v007_signal(debtc, closeadj):
    base = _mean(debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw debtc
def dmm_f023_debt_maturity_mix_raw_126d_accel_v008_signal(debtc, closeadj):
    base = _mean(debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw debtc
def dmm_f023_debt_maturity_mix_raw_126d_accel_v009_signal(debtc, closeadj):
    base = _mean(debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw debtc
def dmm_f023_debt_maturity_mix_raw_252d_accel_v010_signal(debtc, closeadj):
    base = _mean(debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw debtc
def dmm_f023_debt_maturity_mix_raw_252d_accel_v011_signal(debtc, closeadj):
    base = _mean(debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw debtc
def dmm_f023_debt_maturity_mix_raw_252d_accel_v012_signal(debtc, closeadj):
    base = _mean(debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw debtc
def dmm_f023_debt_maturity_mix_raw_504d_accel_v013_signal(debtc, closeadj):
    base = _mean(debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw debtc
def dmm_f023_debt_maturity_mix_raw_504d_accel_v014_signal(debtc, closeadj):
    base = _mean(debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw debtc
def dmm_f023_debt_maturity_mix_raw_504d_accel_v015_signal(debtc, closeadj):
    base = _mean(debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log debtc
def dmm_f023_debt_maturity_mix_log_21d_accel_v016_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log debtc
def dmm_f023_debt_maturity_mix_log_21d_accel_v017_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log debtc
def dmm_f023_debt_maturity_mix_log_21d_accel_v018_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log debtc
def dmm_f023_debt_maturity_mix_log_63d_accel_v019_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log debtc
def dmm_f023_debt_maturity_mix_log_63d_accel_v020_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log debtc
def dmm_f023_debt_maturity_mix_log_63d_accel_v021_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log debtc
def dmm_f023_debt_maturity_mix_log_126d_accel_v022_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log debtc
def dmm_f023_debt_maturity_mix_log_126d_accel_v023_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log debtc
def dmm_f023_debt_maturity_mix_log_126d_accel_v024_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log debtc
def dmm_f023_debt_maturity_mix_log_252d_accel_v025_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log debtc
def dmm_f023_debt_maturity_mix_log_252d_accel_v026_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log debtc
def dmm_f023_debt_maturity_mix_log_252d_accel_v027_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log debtc
def dmm_f023_debt_maturity_mix_log_504d_accel_v028_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log debtc
def dmm_f023_debt_maturity_mix_log_504d_accel_v029_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log debtc
def dmm_f023_debt_maturity_mix_log_504d_accel_v030_signal(debtc, closeadj):
    base = _mean(_debt_maturity_mix_log(debtc), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_21d_accel_v031_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_21d_accel_v032_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_21d_accel_v033_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_63d_accel_v034_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_63d_accel_v035_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_63d_accel_v036_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_126d_accel_v037_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_126d_accel_v038_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_126d_accel_v039_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_252d_accel_v040_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_252d_accel_v041_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_252d_accel_v042_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_504d_accel_v043_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_504d_accel_v044_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare debtc
def dmm_f023_debt_maturity_mix_pershare_504d_accel_v045_signal(debtc, sharesbas, closeadj):
    base = _mean(_debt_maturity_mix_per_share(debtc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_21d_accel_v046_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_21d_accel_v047_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_21d_accel_v048_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_63d_accel_v049_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_63d_accel_v050_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_63d_accel_v051_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_126d_accel_v052_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_126d_accel_v053_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_126d_accel_v054_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_252d_accel_v055_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_252d_accel_v056_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_252d_accel_v057_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_504d_accel_v058_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_504d_accel_v059_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_debtnc debtc
def dmm_f023_debt_maturity_mix_per_debtnc_504d_accel_v060_signal(debtc, debtnc):
    base = _mean(_debt_maturity_mix_scaled(debtc, debtnc), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_21d_accel_v061_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_21d_accel_v062_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_21d_accel_v063_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_63d_accel_v064_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_63d_accel_v065_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_63d_accel_v066_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_126d_accel_v067_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_126d_accel_v068_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_126d_accel_v069_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_252d_accel_v070_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_252d_accel_v071_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_252d_accel_v072_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_504d_accel_v073_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_504d_accel_v074_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_debt debtc
def dmm_f023_debt_maturity_mix_per_debt_504d_accel_v075_signal(debtc, debt):
    base = _mean(_debt_maturity_mix_scaled(debtc, debt), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_21d_accel_v076_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_21d_accel_v077_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_21d_accel_v078_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_63d_accel_v079_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_63d_accel_v080_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_63d_accel_v081_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_126d_accel_v082_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_126d_accel_v083_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_126d_accel_v084_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_252d_accel_v085_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_252d_accel_v086_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_252d_accel_v087_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_504d_accel_v088_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_504d_accel_v089_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets debtc
def dmm_f023_debt_maturity_mix_per_assets_504d_accel_v090_signal(debtc, assets):
    base = _mean(_debt_maturity_mix_scaled(debtc, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std debtc
def dmm_f023_debt_maturity_mix_std_21d_accel_v091_signal(debtc, closeadj):
    base = _std(debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std debtc
def dmm_f023_debt_maturity_mix_std_21d_accel_v092_signal(debtc, closeadj):
    base = _std(debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std debtc
def dmm_f023_debt_maturity_mix_std_21d_accel_v093_signal(debtc, closeadj):
    base = _std(debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std debtc
def dmm_f023_debt_maturity_mix_std_63d_accel_v094_signal(debtc, closeadj):
    base = _std(debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std debtc
def dmm_f023_debt_maturity_mix_std_63d_accel_v095_signal(debtc, closeadj):
    base = _std(debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std debtc
def dmm_f023_debt_maturity_mix_std_63d_accel_v096_signal(debtc, closeadj):
    base = _std(debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std debtc
def dmm_f023_debt_maturity_mix_std_126d_accel_v097_signal(debtc, closeadj):
    base = _std(debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std debtc
def dmm_f023_debt_maturity_mix_std_126d_accel_v098_signal(debtc, closeadj):
    base = _std(debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std debtc
def dmm_f023_debt_maturity_mix_std_126d_accel_v099_signal(debtc, closeadj):
    base = _std(debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std debtc
def dmm_f023_debt_maturity_mix_std_252d_accel_v100_signal(debtc, closeadj):
    base = _std(debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std debtc
def dmm_f023_debt_maturity_mix_std_252d_accel_v101_signal(debtc, closeadj):
    base = _std(debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std debtc
def dmm_f023_debt_maturity_mix_std_252d_accel_v102_signal(debtc, closeadj):
    base = _std(debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std debtc
def dmm_f023_debt_maturity_mix_std_504d_accel_v103_signal(debtc, closeadj):
    base = _std(debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std debtc
def dmm_f023_debt_maturity_mix_std_504d_accel_v104_signal(debtc, closeadj):
    base = _std(debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std debtc
def dmm_f023_debt_maturity_mix_std_504d_accel_v105_signal(debtc, closeadj):
    base = _std(debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_21d_accel_v106_signal(debtc, closeadj):
    base = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_21d_accel_v107_signal(debtc, closeadj):
    base = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_21d_accel_v108_signal(debtc, closeadj):
    base = debtc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_63d_accel_v109_signal(debtc, closeadj):
    base = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_63d_accel_v110_signal(debtc, closeadj):
    base = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_63d_accel_v111_signal(debtc, closeadj):
    base = debtc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_126d_accel_v112_signal(debtc, closeadj):
    base = debtc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_126d_accel_v113_signal(debtc, closeadj):
    base = debtc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_126d_accel_v114_signal(debtc, closeadj):
    base = debtc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_252d_accel_v115_signal(debtc, closeadj):
    base = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_252d_accel_v116_signal(debtc, closeadj):
    base = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_252d_accel_v117_signal(debtc, closeadj):
    base = debtc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_504d_accel_v118_signal(debtc, closeadj):
    base = debtc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_504d_accel_v119_signal(debtc, closeadj):
    base = debtc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm debtc
def dmm_f023_debt_maturity_mix_ewm_504d_accel_v120_signal(debtc, closeadj):
    base = debtc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq debtc
def dmm_f023_debt_maturity_mix_sq_21d_accel_v121_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq debtc
def dmm_f023_debt_maturity_mix_sq_21d_accel_v122_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq debtc
def dmm_f023_debt_maturity_mix_sq_21d_accel_v123_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq debtc
def dmm_f023_debt_maturity_mix_sq_63d_accel_v124_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq debtc
def dmm_f023_debt_maturity_mix_sq_63d_accel_v125_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq debtc
def dmm_f023_debt_maturity_mix_sq_63d_accel_v126_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq debtc
def dmm_f023_debt_maturity_mix_sq_126d_accel_v127_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq debtc
def dmm_f023_debt_maturity_mix_sq_126d_accel_v128_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq debtc
def dmm_f023_debt_maturity_mix_sq_126d_accel_v129_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq debtc
def dmm_f023_debt_maturity_mix_sq_252d_accel_v130_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq debtc
def dmm_f023_debt_maturity_mix_sq_252d_accel_v131_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq debtc
def dmm_f023_debt_maturity_mix_sq_252d_accel_v132_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq debtc
def dmm_f023_debt_maturity_mix_sq_504d_accel_v133_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq debtc
def dmm_f023_debt_maturity_mix_sq_504d_accel_v134_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq debtc
def dmm_f023_debt_maturity_mix_sq_504d_accel_v135_signal(debtc, closeadj):
    base = _mean(debtc * debtc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z debtc
def dmm_f023_debt_maturity_mix_z_21d_accel_v136_signal(debtc):
    base = _z(debtc, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z debtc
def dmm_f023_debt_maturity_mix_z_21d_accel_v137_signal(debtc):
    base = _z(debtc, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z debtc
def dmm_f023_debt_maturity_mix_z_21d_accel_v138_signal(debtc):
    base = _z(debtc, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z debtc
def dmm_f023_debt_maturity_mix_z_63d_accel_v139_signal(debtc):
    base = _z(debtc, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z debtc
def dmm_f023_debt_maturity_mix_z_63d_accel_v140_signal(debtc):
    base = _z(debtc, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z debtc
def dmm_f023_debt_maturity_mix_z_63d_accel_v141_signal(debtc):
    base = _z(debtc, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z debtc
def dmm_f023_debt_maturity_mix_z_126d_accel_v142_signal(debtc):
    base = _z(debtc, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z debtc
def dmm_f023_debt_maturity_mix_z_126d_accel_v143_signal(debtc):
    base = _z(debtc, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z debtc
def dmm_f023_debt_maturity_mix_z_126d_accel_v144_signal(debtc):
    base = _z(debtc, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z debtc
def dmm_f023_debt_maturity_mix_z_252d_accel_v145_signal(debtc):
    base = _z(debtc, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z debtc
def dmm_f023_debt_maturity_mix_z_252d_accel_v146_signal(debtc):
    base = _z(debtc, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z debtc
def dmm_f023_debt_maturity_mix_z_252d_accel_v147_signal(debtc):
    base = _z(debtc, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z debtc
def dmm_f023_debt_maturity_mix_z_504d_accel_v148_signal(debtc):
    base = _z(debtc, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z debtc
def dmm_f023_debt_maturity_mix_z_504d_accel_v149_signal(debtc):
    base = _z(debtc, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z debtc
def dmm_f023_debt_maturity_mix_z_504d_accel_v150_signal(debtc):
    base = _z(debtc, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
