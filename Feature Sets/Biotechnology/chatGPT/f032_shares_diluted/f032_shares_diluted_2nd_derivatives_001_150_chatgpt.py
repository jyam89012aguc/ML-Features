"""Family f032 - Diluted share overhang (Dilution and Share Count) | Sharadar tables: SF1 | fields: shareswa, shareswadil, sharesbas | 2nd derivatives 001-150"""
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
def _shares_diluted_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _shares_diluted_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _shares_diluted_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw shareswa
def sd_f032_shares_diluted_raw_21d_slope_v001_signal(shareswa, closeadj):
    base = _mean(shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw shareswa
def sd_f032_shares_diluted_raw_21d_slope_v002_signal(shareswa, closeadj):
    base = _mean(shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw shareswa
def sd_f032_shares_diluted_raw_21d_slope_v003_signal(shareswa, closeadj):
    base = _mean(shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw shareswa
def sd_f032_shares_diluted_raw_63d_slope_v004_signal(shareswa, closeadj):
    base = _mean(shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw shareswa
def sd_f032_shares_diluted_raw_63d_slope_v005_signal(shareswa, closeadj):
    base = _mean(shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw shareswa
def sd_f032_shares_diluted_raw_63d_slope_v006_signal(shareswa, closeadj):
    base = _mean(shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw shareswa
def sd_f032_shares_diluted_raw_126d_slope_v007_signal(shareswa, closeadj):
    base = _mean(shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw shareswa
def sd_f032_shares_diluted_raw_126d_slope_v008_signal(shareswa, closeadj):
    base = _mean(shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw shareswa
def sd_f032_shares_diluted_raw_126d_slope_v009_signal(shareswa, closeadj):
    base = _mean(shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw shareswa
def sd_f032_shares_diluted_raw_252d_slope_v010_signal(shareswa, closeadj):
    base = _mean(shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw shareswa
def sd_f032_shares_diluted_raw_252d_slope_v011_signal(shareswa, closeadj):
    base = _mean(shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw shareswa
def sd_f032_shares_diluted_raw_252d_slope_v012_signal(shareswa, closeadj):
    base = _mean(shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw shareswa
def sd_f032_shares_diluted_raw_504d_slope_v013_signal(shareswa, closeadj):
    base = _mean(shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw shareswa
def sd_f032_shares_diluted_raw_504d_slope_v014_signal(shareswa, closeadj):
    base = _mean(shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw shareswa
def sd_f032_shares_diluted_raw_504d_slope_v015_signal(shareswa, closeadj):
    base = _mean(shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log shareswa
def sd_f032_shares_diluted_log_21d_slope_v016_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log shareswa
def sd_f032_shares_diluted_log_21d_slope_v017_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log shareswa
def sd_f032_shares_diluted_log_21d_slope_v018_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log shareswa
def sd_f032_shares_diluted_log_63d_slope_v019_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log shareswa
def sd_f032_shares_diluted_log_63d_slope_v020_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log shareswa
def sd_f032_shares_diluted_log_63d_slope_v021_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log shareswa
def sd_f032_shares_diluted_log_126d_slope_v022_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log shareswa
def sd_f032_shares_diluted_log_126d_slope_v023_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log shareswa
def sd_f032_shares_diluted_log_126d_slope_v024_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log shareswa
def sd_f032_shares_diluted_log_252d_slope_v025_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log shareswa
def sd_f032_shares_diluted_log_252d_slope_v026_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log shareswa
def sd_f032_shares_diluted_log_252d_slope_v027_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log shareswa
def sd_f032_shares_diluted_log_504d_slope_v028_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log shareswa
def sd_f032_shares_diluted_log_504d_slope_v029_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log shareswa
def sd_f032_shares_diluted_log_504d_slope_v030_signal(shareswa, closeadj):
    base = _mean(_shares_diluted_log(shareswa), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare shareswa
def sd_f032_shares_diluted_pershare_21d_slope_v031_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare shareswa
def sd_f032_shares_diluted_pershare_21d_slope_v032_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare shareswa
def sd_f032_shares_diluted_pershare_21d_slope_v033_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare shareswa
def sd_f032_shares_diluted_pershare_63d_slope_v034_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare shareswa
def sd_f032_shares_diluted_pershare_63d_slope_v035_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare shareswa
def sd_f032_shares_diluted_pershare_63d_slope_v036_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare shareswa
def sd_f032_shares_diluted_pershare_126d_slope_v037_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare shareswa
def sd_f032_shares_diluted_pershare_126d_slope_v038_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare shareswa
def sd_f032_shares_diluted_pershare_126d_slope_v039_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare shareswa
def sd_f032_shares_diluted_pershare_252d_slope_v040_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare shareswa
def sd_f032_shares_diluted_pershare_252d_slope_v041_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare shareswa
def sd_f032_shares_diluted_pershare_252d_slope_v042_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare shareswa
def sd_f032_shares_diluted_pershare_504d_slope_v043_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare shareswa
def sd_f032_shares_diluted_pershare_504d_slope_v044_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare shareswa
def sd_f032_shares_diluted_pershare_504d_slope_v045_signal(shareswa, sharesbas, closeadj):
    base = _mean(_shares_diluted_per_share(shareswa, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_21d_slope_v046_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_21d_slope_v047_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_21d_slope_v048_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_63d_slope_v049_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_63d_slope_v050_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_63d_slope_v051_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_126d_slope_v052_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_126d_slope_v053_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_126d_slope_v054_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_252d_slope_v055_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_252d_slope_v056_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_252d_slope_v057_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_504d_slope_v058_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_504d_slope_v059_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_shareswadil shareswa
def sd_f032_shares_diluted_per_shareswadil_504d_slope_v060_signal(shareswa, shareswadil):
    base = _mean(_shares_diluted_scaled(shareswa, shareswadil), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_21d_slope_v061_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_21d_slope_v062_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_21d_slope_v063_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_63d_slope_v064_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_63d_slope_v065_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_63d_slope_v066_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_126d_slope_v067_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_126d_slope_v068_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_126d_slope_v069_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_252d_slope_v070_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_252d_slope_v071_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_252d_slope_v072_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_504d_slope_v073_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_504d_slope_v074_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas shareswa
def sd_f032_shares_diluted_per_sharesbas_504d_slope_v075_signal(shareswa, sharesbas):
    base = _mean(_shares_diluted_scaled(shareswa, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets shareswa
def sd_f032_shares_diluted_per_assets_21d_slope_v076_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets shareswa
def sd_f032_shares_diluted_per_assets_21d_slope_v077_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets shareswa
def sd_f032_shares_diluted_per_assets_21d_slope_v078_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets shareswa
def sd_f032_shares_diluted_per_assets_63d_slope_v079_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets shareswa
def sd_f032_shares_diluted_per_assets_63d_slope_v080_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets shareswa
def sd_f032_shares_diluted_per_assets_63d_slope_v081_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets shareswa
def sd_f032_shares_diluted_per_assets_126d_slope_v082_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets shareswa
def sd_f032_shares_diluted_per_assets_126d_slope_v083_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets shareswa
def sd_f032_shares_diluted_per_assets_126d_slope_v084_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets shareswa
def sd_f032_shares_diluted_per_assets_252d_slope_v085_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets shareswa
def sd_f032_shares_diluted_per_assets_252d_slope_v086_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets shareswa
def sd_f032_shares_diluted_per_assets_252d_slope_v087_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets shareswa
def sd_f032_shares_diluted_per_assets_504d_slope_v088_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets shareswa
def sd_f032_shares_diluted_per_assets_504d_slope_v089_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets shareswa
def sd_f032_shares_diluted_per_assets_504d_slope_v090_signal(shareswa, assets):
    base = _mean(_shares_diluted_scaled(shareswa, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std shareswa
def sd_f032_shares_diluted_std_21d_slope_v091_signal(shareswa, closeadj):
    base = _std(shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std shareswa
def sd_f032_shares_diluted_std_21d_slope_v092_signal(shareswa, closeadj):
    base = _std(shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std shareswa
def sd_f032_shares_diluted_std_21d_slope_v093_signal(shareswa, closeadj):
    base = _std(shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std shareswa
def sd_f032_shares_diluted_std_63d_slope_v094_signal(shareswa, closeadj):
    base = _std(shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std shareswa
def sd_f032_shares_diluted_std_63d_slope_v095_signal(shareswa, closeadj):
    base = _std(shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std shareswa
def sd_f032_shares_diluted_std_63d_slope_v096_signal(shareswa, closeadj):
    base = _std(shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std shareswa
def sd_f032_shares_diluted_std_126d_slope_v097_signal(shareswa, closeadj):
    base = _std(shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std shareswa
def sd_f032_shares_diluted_std_126d_slope_v098_signal(shareswa, closeadj):
    base = _std(shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std shareswa
def sd_f032_shares_diluted_std_126d_slope_v099_signal(shareswa, closeadj):
    base = _std(shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std shareswa
def sd_f032_shares_diluted_std_252d_slope_v100_signal(shareswa, closeadj):
    base = _std(shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std shareswa
def sd_f032_shares_diluted_std_252d_slope_v101_signal(shareswa, closeadj):
    base = _std(shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std shareswa
def sd_f032_shares_diluted_std_252d_slope_v102_signal(shareswa, closeadj):
    base = _std(shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std shareswa
def sd_f032_shares_diluted_std_504d_slope_v103_signal(shareswa, closeadj):
    base = _std(shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std shareswa
def sd_f032_shares_diluted_std_504d_slope_v104_signal(shareswa, closeadj):
    base = _std(shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std shareswa
def sd_f032_shares_diluted_std_504d_slope_v105_signal(shareswa, closeadj):
    base = _std(shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm shareswa
def sd_f032_shares_diluted_ewm_21d_slope_v106_signal(shareswa, closeadj):
    base = shareswa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm shareswa
def sd_f032_shares_diluted_ewm_21d_slope_v107_signal(shareswa, closeadj):
    base = shareswa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm shareswa
def sd_f032_shares_diluted_ewm_21d_slope_v108_signal(shareswa, closeadj):
    base = shareswa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm shareswa
def sd_f032_shares_diluted_ewm_63d_slope_v109_signal(shareswa, closeadj):
    base = shareswa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm shareswa
def sd_f032_shares_diluted_ewm_63d_slope_v110_signal(shareswa, closeadj):
    base = shareswa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm shareswa
def sd_f032_shares_diluted_ewm_63d_slope_v111_signal(shareswa, closeadj):
    base = shareswa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm shareswa
def sd_f032_shares_diluted_ewm_126d_slope_v112_signal(shareswa, closeadj):
    base = shareswa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm shareswa
def sd_f032_shares_diluted_ewm_126d_slope_v113_signal(shareswa, closeadj):
    base = shareswa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm shareswa
def sd_f032_shares_diluted_ewm_126d_slope_v114_signal(shareswa, closeadj):
    base = shareswa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm shareswa
def sd_f032_shares_diluted_ewm_252d_slope_v115_signal(shareswa, closeadj):
    base = shareswa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm shareswa
def sd_f032_shares_diluted_ewm_252d_slope_v116_signal(shareswa, closeadj):
    base = shareswa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm shareswa
def sd_f032_shares_diluted_ewm_252d_slope_v117_signal(shareswa, closeadj):
    base = shareswa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm shareswa
def sd_f032_shares_diluted_ewm_504d_slope_v118_signal(shareswa, closeadj):
    base = shareswa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm shareswa
def sd_f032_shares_diluted_ewm_504d_slope_v119_signal(shareswa, closeadj):
    base = shareswa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm shareswa
def sd_f032_shares_diluted_ewm_504d_slope_v120_signal(shareswa, closeadj):
    base = shareswa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq shareswa
def sd_f032_shares_diluted_sq_21d_slope_v121_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq shareswa
def sd_f032_shares_diluted_sq_21d_slope_v122_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq shareswa
def sd_f032_shares_diluted_sq_21d_slope_v123_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq shareswa
def sd_f032_shares_diluted_sq_63d_slope_v124_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq shareswa
def sd_f032_shares_diluted_sq_63d_slope_v125_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq shareswa
def sd_f032_shares_diluted_sq_63d_slope_v126_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq shareswa
def sd_f032_shares_diluted_sq_126d_slope_v127_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq shareswa
def sd_f032_shares_diluted_sq_126d_slope_v128_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq shareswa
def sd_f032_shares_diluted_sq_126d_slope_v129_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq shareswa
def sd_f032_shares_diluted_sq_252d_slope_v130_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq shareswa
def sd_f032_shares_diluted_sq_252d_slope_v131_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq shareswa
def sd_f032_shares_diluted_sq_252d_slope_v132_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq shareswa
def sd_f032_shares_diluted_sq_504d_slope_v133_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq shareswa
def sd_f032_shares_diluted_sq_504d_slope_v134_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq shareswa
def sd_f032_shares_diluted_sq_504d_slope_v135_signal(shareswa, closeadj):
    base = _mean(shareswa * shareswa, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z shareswa
def sd_f032_shares_diluted_z_21d_slope_v136_signal(shareswa):
    base = _z(shareswa, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z shareswa
def sd_f032_shares_diluted_z_21d_slope_v137_signal(shareswa):
    base = _z(shareswa, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z shareswa
def sd_f032_shares_diluted_z_21d_slope_v138_signal(shareswa):
    base = _z(shareswa, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z shareswa
def sd_f032_shares_diluted_z_63d_slope_v139_signal(shareswa):
    base = _z(shareswa, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z shareswa
def sd_f032_shares_diluted_z_63d_slope_v140_signal(shareswa):
    base = _z(shareswa, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z shareswa
def sd_f032_shares_diluted_z_63d_slope_v141_signal(shareswa):
    base = _z(shareswa, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z shareswa
def sd_f032_shares_diluted_z_126d_slope_v142_signal(shareswa):
    base = _z(shareswa, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z shareswa
def sd_f032_shares_diluted_z_126d_slope_v143_signal(shareswa):
    base = _z(shareswa, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z shareswa
def sd_f032_shares_diluted_z_126d_slope_v144_signal(shareswa):
    base = _z(shareswa, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z shareswa
def sd_f032_shares_diluted_z_252d_slope_v145_signal(shareswa):
    base = _z(shareswa, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z shareswa
def sd_f032_shares_diluted_z_252d_slope_v146_signal(shareswa):
    base = _z(shareswa, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z shareswa
def sd_f032_shares_diluted_z_252d_slope_v147_signal(shareswa):
    base = _z(shareswa, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z shareswa
def sd_f032_shares_diluted_z_504d_slope_v148_signal(shareswa):
    base = _z(shareswa, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z shareswa
def sd_f032_shares_diluted_z_504d_slope_v149_signal(shareswa):
    base = _z(shareswa, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z shareswa
def sd_f032_shares_diluted_z_504d_slope_v150_signal(shareswa):
    base = _z(shareswa, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
