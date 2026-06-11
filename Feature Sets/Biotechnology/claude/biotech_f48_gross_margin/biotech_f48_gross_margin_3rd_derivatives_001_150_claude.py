"""Family f48 - Gross margin level & trend  (H_Margins) | 3rd derivatives 001-150"""
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
def _gross_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _gross_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _gross_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw grossmargin
def gm_f48_gross_margin_raw_21d_accel_v001_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw grossmargin
def gm_f48_gross_margin_raw_21d_accel_v002_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw grossmargin
def gm_f48_gross_margin_raw_21d_accel_v003_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw grossmargin
def gm_f48_gross_margin_raw_63d_accel_v004_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw grossmargin
def gm_f48_gross_margin_raw_63d_accel_v005_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw grossmargin
def gm_f48_gross_margin_raw_63d_accel_v006_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw grossmargin
def gm_f48_gross_margin_raw_126d_accel_v007_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw grossmargin
def gm_f48_gross_margin_raw_126d_accel_v008_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw grossmargin
def gm_f48_gross_margin_raw_126d_accel_v009_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw grossmargin
def gm_f48_gross_margin_raw_252d_accel_v010_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw grossmargin
def gm_f48_gross_margin_raw_252d_accel_v011_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw grossmargin
def gm_f48_gross_margin_raw_252d_accel_v012_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw grossmargin
def gm_f48_gross_margin_raw_504d_accel_v013_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw grossmargin
def gm_f48_gross_margin_raw_504d_accel_v014_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw grossmargin
def gm_f48_gross_margin_raw_504d_accel_v015_signal(grossmargin, closeadj):
    base = _mean(grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log grossmargin
def gm_f48_gross_margin_log_21d_accel_v016_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log grossmargin
def gm_f48_gross_margin_log_21d_accel_v017_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log grossmargin
def gm_f48_gross_margin_log_21d_accel_v018_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log grossmargin
def gm_f48_gross_margin_log_63d_accel_v019_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log grossmargin
def gm_f48_gross_margin_log_63d_accel_v020_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log grossmargin
def gm_f48_gross_margin_log_63d_accel_v021_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log grossmargin
def gm_f48_gross_margin_log_126d_accel_v022_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log grossmargin
def gm_f48_gross_margin_log_126d_accel_v023_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log grossmargin
def gm_f48_gross_margin_log_126d_accel_v024_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log grossmargin
def gm_f48_gross_margin_log_252d_accel_v025_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log grossmargin
def gm_f48_gross_margin_log_252d_accel_v026_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log grossmargin
def gm_f48_gross_margin_log_252d_accel_v027_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log grossmargin
def gm_f48_gross_margin_log_504d_accel_v028_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log grossmargin
def gm_f48_gross_margin_log_504d_accel_v029_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log grossmargin
def gm_f48_gross_margin_log_504d_accel_v030_signal(grossmargin, closeadj):
    base = _mean(_gross_margin_log(grossmargin), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare grossmargin
def gm_f48_gross_margin_pershare_21d_accel_v031_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare grossmargin
def gm_f48_gross_margin_pershare_21d_accel_v032_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare grossmargin
def gm_f48_gross_margin_pershare_21d_accel_v033_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare grossmargin
def gm_f48_gross_margin_pershare_63d_accel_v034_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare grossmargin
def gm_f48_gross_margin_pershare_63d_accel_v035_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare grossmargin
def gm_f48_gross_margin_pershare_63d_accel_v036_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare grossmargin
def gm_f48_gross_margin_pershare_126d_accel_v037_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare grossmargin
def gm_f48_gross_margin_pershare_126d_accel_v038_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare grossmargin
def gm_f48_gross_margin_pershare_126d_accel_v039_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare grossmargin
def gm_f48_gross_margin_pershare_252d_accel_v040_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare grossmargin
def gm_f48_gross_margin_pershare_252d_accel_v041_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare grossmargin
def gm_f48_gross_margin_pershare_252d_accel_v042_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare grossmargin
def gm_f48_gross_margin_pershare_504d_accel_v043_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare grossmargin
def gm_f48_gross_margin_pershare_504d_accel_v044_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare grossmargin
def gm_f48_gross_margin_pershare_504d_accel_v045_signal(grossmargin, sharesbas, closeadj):
    base = _mean(_gross_margin_per_share(grossmargin, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets grossmargin
def gm_f48_gross_margin_per_assets_21d_accel_v046_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets grossmargin
def gm_f48_gross_margin_per_assets_21d_accel_v047_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets grossmargin
def gm_f48_gross_margin_per_assets_21d_accel_v048_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets grossmargin
def gm_f48_gross_margin_per_assets_63d_accel_v049_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets grossmargin
def gm_f48_gross_margin_per_assets_63d_accel_v050_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets grossmargin
def gm_f48_gross_margin_per_assets_63d_accel_v051_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets grossmargin
def gm_f48_gross_margin_per_assets_126d_accel_v052_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets grossmargin
def gm_f48_gross_margin_per_assets_126d_accel_v053_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets grossmargin
def gm_f48_gross_margin_per_assets_126d_accel_v054_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets grossmargin
def gm_f48_gross_margin_per_assets_252d_accel_v055_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets grossmargin
def gm_f48_gross_margin_per_assets_252d_accel_v056_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets grossmargin
def gm_f48_gross_margin_per_assets_252d_accel_v057_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets grossmargin
def gm_f48_gross_margin_per_assets_504d_accel_v058_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets grossmargin
def gm_f48_gross_margin_per_assets_504d_accel_v059_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets grossmargin
def gm_f48_gross_margin_per_assets_504d_accel_v060_signal(grossmargin, assets):
    base = _mean(_gross_margin_scaled(grossmargin, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_21d_accel_v061_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_21d_accel_v062_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_21d_accel_v063_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_63d_accel_v064_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_63d_accel_v065_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_63d_accel_v066_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_126d_accel_v067_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_126d_accel_v068_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_126d_accel_v069_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_252d_accel_v070_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_252d_accel_v071_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_252d_accel_v072_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_504d_accel_v073_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_504d_accel_v074_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap grossmargin
def gm_f48_gross_margin_per_marketcap_504d_accel_v075_signal(grossmargin, marketcap):
    base = _mean(_gross_margin_scaled(grossmargin, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity grossmargin
def gm_f48_gross_margin_per_equity_21d_accel_v076_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity grossmargin
def gm_f48_gross_margin_per_equity_21d_accel_v077_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity grossmargin
def gm_f48_gross_margin_per_equity_21d_accel_v078_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity grossmargin
def gm_f48_gross_margin_per_equity_63d_accel_v079_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity grossmargin
def gm_f48_gross_margin_per_equity_63d_accel_v080_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity grossmargin
def gm_f48_gross_margin_per_equity_63d_accel_v081_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity grossmargin
def gm_f48_gross_margin_per_equity_126d_accel_v082_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity grossmargin
def gm_f48_gross_margin_per_equity_126d_accel_v083_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity grossmargin
def gm_f48_gross_margin_per_equity_126d_accel_v084_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity grossmargin
def gm_f48_gross_margin_per_equity_252d_accel_v085_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity grossmargin
def gm_f48_gross_margin_per_equity_252d_accel_v086_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity grossmargin
def gm_f48_gross_margin_per_equity_252d_accel_v087_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity grossmargin
def gm_f48_gross_margin_per_equity_504d_accel_v088_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity grossmargin
def gm_f48_gross_margin_per_equity_504d_accel_v089_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity grossmargin
def gm_f48_gross_margin_per_equity_504d_accel_v090_signal(grossmargin, equity):
    base = _mean(_gross_margin_scaled(grossmargin, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std grossmargin
def gm_f48_gross_margin_std_21d_accel_v091_signal(grossmargin, closeadj):
    base = _std(grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std grossmargin
def gm_f48_gross_margin_std_21d_accel_v092_signal(grossmargin, closeadj):
    base = _std(grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std grossmargin
def gm_f48_gross_margin_std_21d_accel_v093_signal(grossmargin, closeadj):
    base = _std(grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std grossmargin
def gm_f48_gross_margin_std_63d_accel_v094_signal(grossmargin, closeadj):
    base = _std(grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std grossmargin
def gm_f48_gross_margin_std_63d_accel_v095_signal(grossmargin, closeadj):
    base = _std(grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std grossmargin
def gm_f48_gross_margin_std_63d_accel_v096_signal(grossmargin, closeadj):
    base = _std(grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std grossmargin
def gm_f48_gross_margin_std_126d_accel_v097_signal(grossmargin, closeadj):
    base = _std(grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std grossmargin
def gm_f48_gross_margin_std_126d_accel_v098_signal(grossmargin, closeadj):
    base = _std(grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std grossmargin
def gm_f48_gross_margin_std_126d_accel_v099_signal(grossmargin, closeadj):
    base = _std(grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std grossmargin
def gm_f48_gross_margin_std_252d_accel_v100_signal(grossmargin, closeadj):
    base = _std(grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std grossmargin
def gm_f48_gross_margin_std_252d_accel_v101_signal(grossmargin, closeadj):
    base = _std(grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std grossmargin
def gm_f48_gross_margin_std_252d_accel_v102_signal(grossmargin, closeadj):
    base = _std(grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std grossmargin
def gm_f48_gross_margin_std_504d_accel_v103_signal(grossmargin, closeadj):
    base = _std(grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std grossmargin
def gm_f48_gross_margin_std_504d_accel_v104_signal(grossmargin, closeadj):
    base = _std(grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std grossmargin
def gm_f48_gross_margin_std_504d_accel_v105_signal(grossmargin, closeadj):
    base = _std(grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm grossmargin
def gm_f48_gross_margin_ewm_21d_accel_v106_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm grossmargin
def gm_f48_gross_margin_ewm_21d_accel_v107_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm grossmargin
def gm_f48_gross_margin_ewm_21d_accel_v108_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm grossmargin
def gm_f48_gross_margin_ewm_63d_accel_v109_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm grossmargin
def gm_f48_gross_margin_ewm_63d_accel_v110_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm grossmargin
def gm_f48_gross_margin_ewm_63d_accel_v111_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm grossmargin
def gm_f48_gross_margin_ewm_126d_accel_v112_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm grossmargin
def gm_f48_gross_margin_ewm_126d_accel_v113_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm grossmargin
def gm_f48_gross_margin_ewm_126d_accel_v114_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm grossmargin
def gm_f48_gross_margin_ewm_252d_accel_v115_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm grossmargin
def gm_f48_gross_margin_ewm_252d_accel_v116_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm grossmargin
def gm_f48_gross_margin_ewm_252d_accel_v117_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm grossmargin
def gm_f48_gross_margin_ewm_504d_accel_v118_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm grossmargin
def gm_f48_gross_margin_ewm_504d_accel_v119_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm grossmargin
def gm_f48_gross_margin_ewm_504d_accel_v120_signal(grossmargin, closeadj):
    base = grossmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq grossmargin
def gm_f48_gross_margin_sq_21d_accel_v121_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq grossmargin
def gm_f48_gross_margin_sq_21d_accel_v122_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq grossmargin
def gm_f48_gross_margin_sq_21d_accel_v123_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq grossmargin
def gm_f48_gross_margin_sq_63d_accel_v124_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq grossmargin
def gm_f48_gross_margin_sq_63d_accel_v125_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq grossmargin
def gm_f48_gross_margin_sq_63d_accel_v126_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq grossmargin
def gm_f48_gross_margin_sq_126d_accel_v127_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq grossmargin
def gm_f48_gross_margin_sq_126d_accel_v128_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq grossmargin
def gm_f48_gross_margin_sq_126d_accel_v129_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq grossmargin
def gm_f48_gross_margin_sq_252d_accel_v130_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq grossmargin
def gm_f48_gross_margin_sq_252d_accel_v131_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq grossmargin
def gm_f48_gross_margin_sq_252d_accel_v132_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq grossmargin
def gm_f48_gross_margin_sq_504d_accel_v133_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq grossmargin
def gm_f48_gross_margin_sq_504d_accel_v134_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq grossmargin
def gm_f48_gross_margin_sq_504d_accel_v135_signal(grossmargin, closeadj):
    base = _mean(grossmargin * grossmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z grossmargin
def gm_f48_gross_margin_z_21d_accel_v136_signal(grossmargin):
    base = _z(grossmargin, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z grossmargin
def gm_f48_gross_margin_z_21d_accel_v137_signal(grossmargin):
    base = _z(grossmargin, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z grossmargin
def gm_f48_gross_margin_z_21d_accel_v138_signal(grossmargin):
    base = _z(grossmargin, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z grossmargin
def gm_f48_gross_margin_z_63d_accel_v139_signal(grossmargin):
    base = _z(grossmargin, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z grossmargin
def gm_f48_gross_margin_z_63d_accel_v140_signal(grossmargin):
    base = _z(grossmargin, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z grossmargin
def gm_f48_gross_margin_z_63d_accel_v141_signal(grossmargin):
    base = _z(grossmargin, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z grossmargin
def gm_f48_gross_margin_z_126d_accel_v142_signal(grossmargin):
    base = _z(grossmargin, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z grossmargin
def gm_f48_gross_margin_z_126d_accel_v143_signal(grossmargin):
    base = _z(grossmargin, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z grossmargin
def gm_f48_gross_margin_z_126d_accel_v144_signal(grossmargin):
    base = _z(grossmargin, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z grossmargin
def gm_f48_gross_margin_z_252d_accel_v145_signal(grossmargin):
    base = _z(grossmargin, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z grossmargin
def gm_f48_gross_margin_z_252d_accel_v146_signal(grossmargin):
    base = _z(grossmargin, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z grossmargin
def gm_f48_gross_margin_z_252d_accel_v147_signal(grossmargin):
    base = _z(grossmargin, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z grossmargin
def gm_f48_gross_margin_z_504d_accel_v148_signal(grossmargin):
    base = _z(grossmargin, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z grossmargin
def gm_f48_gross_margin_z_504d_accel_v149_signal(grossmargin):
    base = _z(grossmargin, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z grossmargin
def gm_f48_gross_margin_z_504d_accel_v150_signal(grossmargin):
    base = _z(grossmargin, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
