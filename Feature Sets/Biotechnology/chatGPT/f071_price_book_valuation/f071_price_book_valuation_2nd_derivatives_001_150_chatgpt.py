"""Family f071 - Book and tangible book valuation (Valuation Multiples) | Sharadar tables: DAILY,SF1 | fields: pb, bvps, tbvps, marketcap, equity | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw pb
def pbv_f071_price_book_valuation_raw_21d_slope_v001_signal(pb, closeadj):
    base = _mean(pb, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw pb
def pbv_f071_price_book_valuation_raw_21d_slope_v002_signal(pb, closeadj):
    base = _mean(pb, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw pb
def pbv_f071_price_book_valuation_raw_21d_slope_v003_signal(pb, closeadj):
    base = _mean(pb, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw pb
def pbv_f071_price_book_valuation_raw_63d_slope_v004_signal(pb, closeadj):
    base = _mean(pb, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw pb
def pbv_f071_price_book_valuation_raw_63d_slope_v005_signal(pb, closeadj):
    base = _mean(pb, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw pb
def pbv_f071_price_book_valuation_raw_63d_slope_v006_signal(pb, closeadj):
    base = _mean(pb, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw pb
def pbv_f071_price_book_valuation_raw_126d_slope_v007_signal(pb, closeadj):
    base = _mean(pb, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw pb
def pbv_f071_price_book_valuation_raw_126d_slope_v008_signal(pb, closeadj):
    base = _mean(pb, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw pb
def pbv_f071_price_book_valuation_raw_126d_slope_v009_signal(pb, closeadj):
    base = _mean(pb, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw pb
def pbv_f071_price_book_valuation_raw_252d_slope_v010_signal(pb, closeadj):
    base = _mean(pb, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw pb
def pbv_f071_price_book_valuation_raw_252d_slope_v011_signal(pb, closeadj):
    base = _mean(pb, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw pb
def pbv_f071_price_book_valuation_raw_252d_slope_v012_signal(pb, closeadj):
    base = _mean(pb, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw pb
def pbv_f071_price_book_valuation_raw_504d_slope_v013_signal(pb, closeadj):
    base = _mean(pb, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw pb
def pbv_f071_price_book_valuation_raw_504d_slope_v014_signal(pb, closeadj):
    base = _mean(pb, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw pb
def pbv_f071_price_book_valuation_raw_504d_slope_v015_signal(pb, closeadj):
    base = _mean(pb, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log pb
def pbv_f071_price_book_valuation_log_21d_slope_v016_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log pb
def pbv_f071_price_book_valuation_log_21d_slope_v017_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log pb
def pbv_f071_price_book_valuation_log_21d_slope_v018_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log pb
def pbv_f071_price_book_valuation_log_63d_slope_v019_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log pb
def pbv_f071_price_book_valuation_log_63d_slope_v020_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log pb
def pbv_f071_price_book_valuation_log_63d_slope_v021_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log pb
def pbv_f071_price_book_valuation_log_126d_slope_v022_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log pb
def pbv_f071_price_book_valuation_log_126d_slope_v023_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log pb
def pbv_f071_price_book_valuation_log_126d_slope_v024_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log pb
def pbv_f071_price_book_valuation_log_252d_slope_v025_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log pb
def pbv_f071_price_book_valuation_log_252d_slope_v026_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log pb
def pbv_f071_price_book_valuation_log_252d_slope_v027_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log pb
def pbv_f071_price_book_valuation_log_504d_slope_v028_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log pb
def pbv_f071_price_book_valuation_log_504d_slope_v029_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log pb
def pbv_f071_price_book_valuation_log_504d_slope_v030_signal(pb, closeadj):
    base = _mean(_price_book_valuation_log(pb), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare pb
def pbv_f071_price_book_valuation_pershare_21d_slope_v031_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare pb
def pbv_f071_price_book_valuation_pershare_21d_slope_v032_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare pb
def pbv_f071_price_book_valuation_pershare_21d_slope_v033_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare pb
def pbv_f071_price_book_valuation_pershare_63d_slope_v034_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare pb
def pbv_f071_price_book_valuation_pershare_63d_slope_v035_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare pb
def pbv_f071_price_book_valuation_pershare_63d_slope_v036_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare pb
def pbv_f071_price_book_valuation_pershare_126d_slope_v037_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare pb
def pbv_f071_price_book_valuation_pershare_126d_slope_v038_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare pb
def pbv_f071_price_book_valuation_pershare_126d_slope_v039_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare pb
def pbv_f071_price_book_valuation_pershare_252d_slope_v040_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare pb
def pbv_f071_price_book_valuation_pershare_252d_slope_v041_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare pb
def pbv_f071_price_book_valuation_pershare_252d_slope_v042_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare pb
def pbv_f071_price_book_valuation_pershare_504d_slope_v043_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare pb
def pbv_f071_price_book_valuation_pershare_504d_slope_v044_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare pb
def pbv_f071_price_book_valuation_pershare_504d_slope_v045_signal(pb, sharesbas, closeadj):
    base = _mean(_price_book_valuation_per_share(pb, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_21d_slope_v046_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_21d_slope_v047_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_21d_slope_v048_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_63d_slope_v049_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_63d_slope_v050_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_63d_slope_v051_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_126d_slope_v052_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_126d_slope_v053_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_126d_slope_v054_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_252d_slope_v055_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_252d_slope_v056_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_252d_slope_v057_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_504d_slope_v058_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_504d_slope_v059_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_bvps pb
def pbv_f071_price_book_valuation_per_bvps_504d_slope_v060_signal(pb, bvps):
    base = _mean(_price_book_valuation_scaled(pb, bvps), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_21d_slope_v061_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_21d_slope_v062_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_21d_slope_v063_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_63d_slope_v064_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_63d_slope_v065_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_63d_slope_v066_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_126d_slope_v067_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_126d_slope_v068_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_126d_slope_v069_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_252d_slope_v070_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_252d_slope_v071_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_252d_slope_v072_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_504d_slope_v073_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_504d_slope_v074_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_tbvps pb
def pbv_f071_price_book_valuation_per_tbvps_504d_slope_v075_signal(pb, tbvps):
    base = _mean(_price_book_valuation_scaled(pb, tbvps), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_21d_slope_v076_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_21d_slope_v077_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_21d_slope_v078_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_63d_slope_v079_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_63d_slope_v080_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_63d_slope_v081_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_126d_slope_v082_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_126d_slope_v083_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_126d_slope_v084_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_252d_slope_v085_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_252d_slope_v086_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_252d_slope_v087_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_504d_slope_v088_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_504d_slope_v089_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap pb
def pbv_f071_price_book_valuation_per_marketcap_504d_slope_v090_signal(pb, marketcap):
    base = _mean(_price_book_valuation_scaled(pb, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std pb
def pbv_f071_price_book_valuation_std_21d_slope_v091_signal(pb, closeadj):
    base = _std(pb, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std pb
def pbv_f071_price_book_valuation_std_21d_slope_v092_signal(pb, closeadj):
    base = _std(pb, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std pb
def pbv_f071_price_book_valuation_std_21d_slope_v093_signal(pb, closeadj):
    base = _std(pb, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std pb
def pbv_f071_price_book_valuation_std_63d_slope_v094_signal(pb, closeadj):
    base = _std(pb, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std pb
def pbv_f071_price_book_valuation_std_63d_slope_v095_signal(pb, closeadj):
    base = _std(pb, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std pb
def pbv_f071_price_book_valuation_std_63d_slope_v096_signal(pb, closeadj):
    base = _std(pb, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std pb
def pbv_f071_price_book_valuation_std_126d_slope_v097_signal(pb, closeadj):
    base = _std(pb, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std pb
def pbv_f071_price_book_valuation_std_126d_slope_v098_signal(pb, closeadj):
    base = _std(pb, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std pb
def pbv_f071_price_book_valuation_std_126d_slope_v099_signal(pb, closeadj):
    base = _std(pb, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std pb
def pbv_f071_price_book_valuation_std_252d_slope_v100_signal(pb, closeadj):
    base = _std(pb, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std pb
def pbv_f071_price_book_valuation_std_252d_slope_v101_signal(pb, closeadj):
    base = _std(pb, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std pb
def pbv_f071_price_book_valuation_std_252d_slope_v102_signal(pb, closeadj):
    base = _std(pb, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std pb
def pbv_f071_price_book_valuation_std_504d_slope_v103_signal(pb, closeadj):
    base = _std(pb, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std pb
def pbv_f071_price_book_valuation_std_504d_slope_v104_signal(pb, closeadj):
    base = _std(pb, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std pb
def pbv_f071_price_book_valuation_std_504d_slope_v105_signal(pb, closeadj):
    base = _std(pb, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm pb
def pbv_f071_price_book_valuation_ewm_21d_slope_v106_signal(pb, closeadj):
    base = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm pb
def pbv_f071_price_book_valuation_ewm_21d_slope_v107_signal(pb, closeadj):
    base = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm pb
def pbv_f071_price_book_valuation_ewm_21d_slope_v108_signal(pb, closeadj):
    base = pb.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm pb
def pbv_f071_price_book_valuation_ewm_63d_slope_v109_signal(pb, closeadj):
    base = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm pb
def pbv_f071_price_book_valuation_ewm_63d_slope_v110_signal(pb, closeadj):
    base = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm pb
def pbv_f071_price_book_valuation_ewm_63d_slope_v111_signal(pb, closeadj):
    base = pb.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm pb
def pbv_f071_price_book_valuation_ewm_126d_slope_v112_signal(pb, closeadj):
    base = pb.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm pb
def pbv_f071_price_book_valuation_ewm_126d_slope_v113_signal(pb, closeadj):
    base = pb.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm pb
def pbv_f071_price_book_valuation_ewm_126d_slope_v114_signal(pb, closeadj):
    base = pb.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm pb
def pbv_f071_price_book_valuation_ewm_252d_slope_v115_signal(pb, closeadj):
    base = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm pb
def pbv_f071_price_book_valuation_ewm_252d_slope_v116_signal(pb, closeadj):
    base = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm pb
def pbv_f071_price_book_valuation_ewm_252d_slope_v117_signal(pb, closeadj):
    base = pb.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm pb
def pbv_f071_price_book_valuation_ewm_504d_slope_v118_signal(pb, closeadj):
    base = pb.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm pb
def pbv_f071_price_book_valuation_ewm_504d_slope_v119_signal(pb, closeadj):
    base = pb.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm pb
def pbv_f071_price_book_valuation_ewm_504d_slope_v120_signal(pb, closeadj):
    base = pb.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq pb
def pbv_f071_price_book_valuation_sq_21d_slope_v121_signal(pb, closeadj):
    base = _mean(pb * pb, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq pb
def pbv_f071_price_book_valuation_sq_21d_slope_v122_signal(pb, closeadj):
    base = _mean(pb * pb, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq pb
def pbv_f071_price_book_valuation_sq_21d_slope_v123_signal(pb, closeadj):
    base = _mean(pb * pb, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq pb
def pbv_f071_price_book_valuation_sq_63d_slope_v124_signal(pb, closeadj):
    base = _mean(pb * pb, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq pb
def pbv_f071_price_book_valuation_sq_63d_slope_v125_signal(pb, closeadj):
    base = _mean(pb * pb, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq pb
def pbv_f071_price_book_valuation_sq_63d_slope_v126_signal(pb, closeadj):
    base = _mean(pb * pb, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq pb
def pbv_f071_price_book_valuation_sq_126d_slope_v127_signal(pb, closeadj):
    base = _mean(pb * pb, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq pb
def pbv_f071_price_book_valuation_sq_126d_slope_v128_signal(pb, closeadj):
    base = _mean(pb * pb, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq pb
def pbv_f071_price_book_valuation_sq_126d_slope_v129_signal(pb, closeadj):
    base = _mean(pb * pb, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq pb
def pbv_f071_price_book_valuation_sq_252d_slope_v130_signal(pb, closeadj):
    base = _mean(pb * pb, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq pb
def pbv_f071_price_book_valuation_sq_252d_slope_v131_signal(pb, closeadj):
    base = _mean(pb * pb, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq pb
def pbv_f071_price_book_valuation_sq_252d_slope_v132_signal(pb, closeadj):
    base = _mean(pb * pb, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq pb
def pbv_f071_price_book_valuation_sq_504d_slope_v133_signal(pb, closeadj):
    base = _mean(pb * pb, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq pb
def pbv_f071_price_book_valuation_sq_504d_slope_v134_signal(pb, closeadj):
    base = _mean(pb * pb, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq pb
def pbv_f071_price_book_valuation_sq_504d_slope_v135_signal(pb, closeadj):
    base = _mean(pb * pb, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z pb
def pbv_f071_price_book_valuation_z_21d_slope_v136_signal(pb):
    base = _z(pb, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z pb
def pbv_f071_price_book_valuation_z_21d_slope_v137_signal(pb):
    base = _z(pb, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z pb
def pbv_f071_price_book_valuation_z_21d_slope_v138_signal(pb):
    base = _z(pb, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z pb
def pbv_f071_price_book_valuation_z_63d_slope_v139_signal(pb):
    base = _z(pb, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z pb
def pbv_f071_price_book_valuation_z_63d_slope_v140_signal(pb):
    base = _z(pb, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z pb
def pbv_f071_price_book_valuation_z_63d_slope_v141_signal(pb):
    base = _z(pb, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z pb
def pbv_f071_price_book_valuation_z_126d_slope_v142_signal(pb):
    base = _z(pb, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z pb
def pbv_f071_price_book_valuation_z_126d_slope_v143_signal(pb):
    base = _z(pb, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z pb
def pbv_f071_price_book_valuation_z_126d_slope_v144_signal(pb):
    base = _z(pb, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z pb
def pbv_f071_price_book_valuation_z_252d_slope_v145_signal(pb):
    base = _z(pb, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z pb
def pbv_f071_price_book_valuation_z_252d_slope_v146_signal(pb):
    base = _z(pb, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z pb
def pbv_f071_price_book_valuation_z_252d_slope_v147_signal(pb):
    base = _z(pb, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z pb
def pbv_f071_price_book_valuation_z_504d_slope_v148_signal(pb):
    base = _z(pb, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z pb
def pbv_f071_price_book_valuation_z_504d_slope_v149_signal(pb):
    base = _z(pb, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z pb
def pbv_f071_price_book_valuation_z_504d_slope_v150_signal(pb):
    base = _z(pb, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
