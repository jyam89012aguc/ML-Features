"""Family f071 - Book and tangible book valuation (Valuation Multiples) | Sharadar tables: DAILY,SF1 | fields: pb, bvps, tbvps, marketcap, equity | 3rd derivatives 001-150"""
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
def _price_book_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _price_book_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _price_book_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw pb
def pbv_f071_price_book_valuation_raw_21d_accel_v001_signal(pb, closeadj):
    base = _mean(pb, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw pb
def pbv_f071_price_book_valuation_raw_21d_accel_v002_signal(pb, closeadj):
    base = _mean(pb, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw pb
def pbv_f071_price_book_valuation_raw_21d_accel_v003_signal(pb, closeadj):
    base = _mean(pb, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw pb
def pbv_f071_price_book_valuation_raw_63d_accel_v004_signal(pb, closeadj):
    base = _mean(pb, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw pb
def pbv_f071_price_book_valuation_raw_63d_accel_v005_signal(pb, closeadj):
    base = _mean(pb, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw pb
def pbv_f071_price_book_valuation_raw_63d_accel_v006_signal(pb, closeadj):
    base = _mean(pb, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw pb
def pbv_f071_price_book_valuation_raw_126d_accel_v007_signal(pb, closeadj):
    base = _mean(pb, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw pb
def pbv_f071_price_book_valuation_raw_126d_accel_v008_signal(pb, closeadj):
    base = _mean(pb, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw pb
def pbv_f071_price_book_valuation_raw_126d_accel_v009_signal(pb, closeadj):
    base = _mean(pb, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw pb
def pbv_f071_price_book_valuation_raw_252d_accel_v010_signal(pb, closeadj):
    base = _mean(pb, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw pb
def pbv_f071_price_book_valuation_raw_252d_accel_v011_signal(pb, closeadj):
    base = _mean(pb, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw pb
def pbv_f071_price_book_valuation_raw_252d_accel_v012_signal(pb, closeadj):
    base = _mean(pb, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw pb
def pbv_f071_price_book_valuation_raw_504d_accel_v013_signal(pb, closeadj):
    base = _mean(pb, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw pb
def pbv_f071_price_book_valuation_raw_504d_accel_v014_signal(pb, closeadj):
    base = _mean(pb, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw pb
def pbv_f071_price_book_valuation_raw_504d_accel_v015_signal(pb, closeadj):
    base = _mean(pb, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log pb
def pbv_f071_price_book_valuation_log_21d_accel_v016_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log pb
def pbv_f071_price_book_valuation_log_21d_accel_v017_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log pb
def pbv_f071_price_book_valuation_log_21d_accel_v018_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log pb
def pbv_f071_price_book_valuation_log_63d_accel_v019_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log pb
def pbv_f071_price_book_valuation_log_63d_accel_v020_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log pb
def pbv_f071_price_book_valuation_log_63d_accel_v021_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log pb
def pbv_f071_price_book_valuation_log_126d_accel_v022_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log pb
def pbv_f071_price_book_valuation_log_126d_accel_v023_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log pb
def pbv_f071_price_book_valuation_log_126d_accel_v024_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log pb
def pbv_f071_price_book_valuation_log_252d_accel_v025_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log pb
def pbv_f071_price_book_valuation_log_252d_accel_v026_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log pb
def pbv_f071_price_book_valuation_log_252d_accel_v027_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log pb
def pbv_f071_price_book_valuation_log_504d_accel_v028_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log pb
def pbv_f071_price_book_valuation_log_504d_accel_v029_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log pb
def pbv_f071_price_book_valuation_log_504d_accel_v030_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare pb
def pbv_f071_price_book_valuation_pershare_21d_accel_v031_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare pb
def pbv_f071_price_book_valuation_pershare_21d_accel_v032_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare pb
def pbv_f071_price_book_valuation_pershare_21d_accel_v033_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare pb
def pbv_f071_price_book_valuation_pershare_63d_accel_v034_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare pb
def pbv_f071_price_book_valuation_pershare_63d_accel_v035_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare pb
def pbv_f071_price_book_valuation_pershare_63d_accel_v036_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare pb
def pbv_f071_price_book_valuation_pershare_126d_accel_v037_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare pb
def pbv_f071_price_book_valuation_pershare_126d_accel_v038_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare pb
def pbv_f071_price_book_valuation_pershare_126d_accel_v039_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare pb
def pbv_f071_price_book_valuation_pershare_252d_accel_v040_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare pb
def pbv_f071_price_book_valuation_pershare_252d_accel_v041_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare pb
def pbv_f071_price_book_valuation_pershare_252d_accel_v042_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare pb
def pbv_f071_price_book_valuation_pershare_504d_accel_v043_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare pb
def pbv_f071_price_book_valuation_pershare_504d_accel_v044_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare pb
def pbv_f071_price_book_valuation_pershare_504d_accel_v045_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_21d_accel_v046_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_21d_accel_v047_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_21d_accel_v048_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_63d_accel_v049_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_63d_accel_v050_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_63d_accel_v051_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_126d_accel_v052_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_126d_accel_v053_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_126d_accel_v054_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_252d_accel_v055_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_252d_accel_v056_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_252d_accel_v057_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_504d_accel_v058_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_504d_accel_v059_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_504d_accel_v060_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_21d_accel_v061_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_21d_accel_v062_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_21d_accel_v063_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_63d_accel_v064_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_63d_accel_v065_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_63d_accel_v066_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_126d_accel_v067_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_126d_accel_v068_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_126d_accel_v069_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_252d_accel_v070_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_252d_accel_v071_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_252d_accel_v072_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_504d_accel_v073_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_504d_accel_v074_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_504d_accel_v075_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_21d_accel_v076_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_21d_accel_v077_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_21d_accel_v078_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_63d_accel_v079_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_63d_accel_v080_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_63d_accel_v081_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_126d_accel_v082_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_126d_accel_v083_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_126d_accel_v084_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_252d_accel_v085_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_252d_accel_v086_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_252d_accel_v087_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_504d_accel_v088_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_504d_accel_v089_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_504d_accel_v090_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std pb
def pbv_f071_price_book_valuation_std_21d_accel_v091_signal(pb, closeadj):
    base = _std(pb, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std pb
def pbv_f071_price_book_valuation_std_21d_accel_v092_signal(pb, closeadj):
    base = _std(pb, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std pb
def pbv_f071_price_book_valuation_std_21d_accel_v093_signal(pb, closeadj):
    base = _std(pb, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std pb
def pbv_f071_price_book_valuation_std_63d_accel_v094_signal(pb, closeadj):
    base = _std(pb, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std pb
def pbv_f071_price_book_valuation_std_63d_accel_v095_signal(pb, closeadj):
    base = _std(pb, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std pb
def pbv_f071_price_book_valuation_std_63d_accel_v096_signal(pb, closeadj):
    base = _std(pb, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std pb
def pbv_f071_price_book_valuation_std_126d_accel_v097_signal(pb, closeadj):
    base = _std(pb, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std pb
def pbv_f071_price_book_valuation_std_126d_accel_v098_signal(pb, closeadj):
    base = _std(pb, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std pb
def pbv_f071_price_book_valuation_std_126d_accel_v099_signal(pb, closeadj):
    base = _std(pb, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std pb
def pbv_f071_price_book_valuation_std_252d_accel_v100_signal(pb, closeadj):
    base = _std(pb, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std pb
def pbv_f071_price_book_valuation_std_252d_accel_v101_signal(pb, closeadj):
    base = _std(pb, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std pb
def pbv_f071_price_book_valuation_std_252d_accel_v102_signal(pb, closeadj):
    base = _std(pb, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std pb
def pbv_f071_price_book_valuation_std_504d_accel_v103_signal(pb, closeadj):
    base = _std(pb, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std pb
def pbv_f071_price_book_valuation_std_504d_accel_v104_signal(pb, closeadj):
    base = _std(pb, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std pb
def pbv_f071_price_book_valuation_std_504d_accel_v105_signal(pb, closeadj):
    base = _std(pb, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm pb
def pbv_f071_price_book_valuation_ewm_21d_accel_v106_signal(pb, closeadj):
    base = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm pb
def pbv_f071_price_book_valuation_ewm_21d_accel_v107_signal(pb, closeadj):
    base = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm pb
def pbv_f071_price_book_valuation_ewm_21d_accel_v108_signal(pb, closeadj):
    base = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm pb
def pbv_f071_price_book_valuation_ewm_63d_accel_v109_signal(pb, closeadj):
    base = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm pb
def pbv_f071_price_book_valuation_ewm_63d_accel_v110_signal(pb, closeadj):
    base = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm pb
def pbv_f071_price_book_valuation_ewm_63d_accel_v111_signal(pb, closeadj):
    base = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm pb
def pbv_f071_price_book_valuation_ewm_126d_accel_v112_signal(pb, closeadj):
    base = pb.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm pb
def pbv_f071_price_book_valuation_ewm_126d_accel_v113_signal(pb, closeadj):
    base = pb.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm pb
def pbv_f071_price_book_valuation_ewm_126d_accel_v114_signal(pb, closeadj):
    base = pb.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm pb
def pbv_f071_price_book_valuation_ewm_252d_accel_v115_signal(pb, closeadj):
    base = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm pb
def pbv_f071_price_book_valuation_ewm_252d_accel_v116_signal(pb, closeadj):
    base = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm pb
def pbv_f071_price_book_valuation_ewm_252d_accel_v117_signal(pb, closeadj):
    base = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm pb
def pbv_f071_price_book_valuation_ewm_504d_accel_v118_signal(pb, closeadj):
    base = pb.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm pb
def pbv_f071_price_book_valuation_ewm_504d_accel_v119_signal(pb, closeadj):
    base = pb.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm pb
def pbv_f071_price_book_valuation_ewm_504d_accel_v120_signal(pb, closeadj):
    base = pb.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq pb
def pbv_f071_price_book_valuation_sq_21d_accel_v121_signal(pb, closeadj):
    base = _mean(pb * pb, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq pb
def pbv_f071_price_book_valuation_sq_21d_accel_v122_signal(pb, closeadj):
    base = _mean(pb * pb, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq pb
def pbv_f071_price_book_valuation_sq_21d_accel_v123_signal(pb, closeadj):
    base = _mean(pb * pb, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq pb
def pbv_f071_price_book_valuation_sq_63d_accel_v124_signal(pb, closeadj):
    base = _mean(pb * pb, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq pb
def pbv_f071_price_book_valuation_sq_63d_accel_v125_signal(pb, closeadj):
    base = _mean(pb * pb, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq pb
def pbv_f071_price_book_valuation_sq_63d_accel_v126_signal(pb, closeadj):
    base = _mean(pb * pb, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq pb
def pbv_f071_price_book_valuation_sq_126d_accel_v127_signal(pb, closeadj):
    base = _mean(pb * pb, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq pb
def pbv_f071_price_book_valuation_sq_126d_accel_v128_signal(pb, closeadj):
    base = _mean(pb * pb, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq pb
def pbv_f071_price_book_valuation_sq_126d_accel_v129_signal(pb, closeadj):
    base = _mean(pb * pb, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq pb
def pbv_f071_price_book_valuation_sq_252d_accel_v130_signal(pb, closeadj):
    base = _mean(pb * pb, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq pb
def pbv_f071_price_book_valuation_sq_252d_accel_v131_signal(pb, closeadj):
    base = _mean(pb * pb, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq pb
def pbv_f071_price_book_valuation_sq_252d_accel_v132_signal(pb, closeadj):
    base = _mean(pb * pb, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq pb
def pbv_f071_price_book_valuation_sq_504d_accel_v133_signal(pb, closeadj):
    base = _mean(pb * pb, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq pb
def pbv_f071_price_book_valuation_sq_504d_accel_v134_signal(pb, closeadj):
    base = _mean(pb * pb, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq pb
def pbv_f071_price_book_valuation_sq_504d_accel_v135_signal(pb, closeadj):
    base = _mean(pb * pb, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z pb
def pbv_f071_price_book_valuation_z_21d_accel_v136_signal(pb):
    base = _z(pb, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z pb
def pbv_f071_price_book_valuation_z_21d_accel_v137_signal(pb):
    base = _z(pb, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z pb
def pbv_f071_price_book_valuation_z_21d_accel_v138_signal(pb):
    base = _z(pb, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z pb
def pbv_f071_price_book_valuation_z_63d_accel_v139_signal(pb):
    base = _z(pb, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z pb
def pbv_f071_price_book_valuation_z_63d_accel_v140_signal(pb):
    base = _z(pb, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z pb
def pbv_f071_price_book_valuation_z_63d_accel_v141_signal(pb):
    base = _z(pb, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z pb
def pbv_f071_price_book_valuation_z_126d_accel_v142_signal(pb):
    base = _z(pb, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z pb
def pbv_f071_price_book_valuation_z_126d_accel_v143_signal(pb):
    base = _z(pb, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z pb
def pbv_f071_price_book_valuation_z_126d_accel_v144_signal(pb):
    base = _z(pb, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z pb
def pbv_f071_price_book_valuation_z_252d_accel_v145_signal(pb):
    base = _z(pb, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z pb
def pbv_f071_price_book_valuation_z_252d_accel_v146_signal(pb):
    base = _z(pb, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z pb
def pbv_f071_price_book_valuation_z_252d_accel_v147_signal(pb):
    base = _z(pb, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z pb
def pbv_f071_price_book_valuation_z_504d_accel_v148_signal(pb):
    base = _z(pb, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z pb
def pbv_f071_price_book_valuation_z_504d_accel_v149_signal(pb):
    base = _z(pb, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z pb
def pbv_f071_price_book_valuation_z_504d_accel_v150_signal(pb):
    base = _z(pb, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
