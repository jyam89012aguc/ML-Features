"""Family f042 - PP&E and facility footprint (Balance Sheet Composition) | Sharadar tables: SF1 | fields: ppnenet, capex, assets | 3rd derivatives 001-150"""
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
def _ppne_and_facilities_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ppne_and_facilities_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ppne_and_facilities_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ppnenet
def paf_f042_ppne_and_facilities_raw_21d_accel_v001_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ppnenet
def paf_f042_ppne_and_facilities_raw_21d_accel_v002_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ppnenet
def paf_f042_ppne_and_facilities_raw_21d_accel_v003_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ppnenet
def paf_f042_ppne_and_facilities_raw_63d_accel_v004_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ppnenet
def paf_f042_ppne_and_facilities_raw_63d_accel_v005_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ppnenet
def paf_f042_ppne_and_facilities_raw_63d_accel_v006_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ppnenet
def paf_f042_ppne_and_facilities_raw_126d_accel_v007_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ppnenet
def paf_f042_ppne_and_facilities_raw_126d_accel_v008_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ppnenet
def paf_f042_ppne_and_facilities_raw_126d_accel_v009_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ppnenet
def paf_f042_ppne_and_facilities_raw_252d_accel_v010_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ppnenet
def paf_f042_ppne_and_facilities_raw_252d_accel_v011_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ppnenet
def paf_f042_ppne_and_facilities_raw_252d_accel_v012_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ppnenet
def paf_f042_ppne_and_facilities_raw_504d_accel_v013_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ppnenet
def paf_f042_ppne_and_facilities_raw_504d_accel_v014_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ppnenet
def paf_f042_ppne_and_facilities_raw_504d_accel_v015_signal(ppnenet, closeadj):
    base = _mean(ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ppnenet
def paf_f042_ppne_and_facilities_log_21d_accel_v016_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ppnenet
def paf_f042_ppne_and_facilities_log_21d_accel_v017_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ppnenet
def paf_f042_ppne_and_facilities_log_21d_accel_v018_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ppnenet
def paf_f042_ppne_and_facilities_log_63d_accel_v019_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ppnenet
def paf_f042_ppne_and_facilities_log_63d_accel_v020_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ppnenet
def paf_f042_ppne_and_facilities_log_63d_accel_v021_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ppnenet
def paf_f042_ppne_and_facilities_log_126d_accel_v022_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ppnenet
def paf_f042_ppne_and_facilities_log_126d_accel_v023_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ppnenet
def paf_f042_ppne_and_facilities_log_126d_accel_v024_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ppnenet
def paf_f042_ppne_and_facilities_log_252d_accel_v025_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ppnenet
def paf_f042_ppne_and_facilities_log_252d_accel_v026_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ppnenet
def paf_f042_ppne_and_facilities_log_252d_accel_v027_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ppnenet
def paf_f042_ppne_and_facilities_log_504d_accel_v028_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ppnenet
def paf_f042_ppne_and_facilities_log_504d_accel_v029_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ppnenet
def paf_f042_ppne_and_facilities_log_504d_accel_v030_signal(ppnenet, closeadj):
    base = _mean(_ppne_and_facilities_log(ppnenet), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_21d_accel_v031_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_21d_accel_v032_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_21d_accel_v033_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_63d_accel_v034_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_63d_accel_v035_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_63d_accel_v036_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_126d_accel_v037_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_126d_accel_v038_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_126d_accel_v039_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_252d_accel_v040_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_252d_accel_v041_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_252d_accel_v042_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_504d_accel_v043_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_504d_accel_v044_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ppnenet
def paf_f042_ppne_and_facilities_pershare_504d_accel_v045_signal(ppnenet, sharesbas, closeadj):
    base = _mean(_ppne_and_facilities_per_share(ppnenet, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_21d_accel_v046_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_21d_accel_v047_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_21d_accel_v048_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_63d_accel_v049_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_63d_accel_v050_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_63d_accel_v051_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_126d_accel_v052_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_126d_accel_v053_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_126d_accel_v054_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_252d_accel_v055_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_252d_accel_v056_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_252d_accel_v057_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_504d_accel_v058_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_504d_accel_v059_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ppnenet
def paf_f042_ppne_and_facilities_per_assets_504d_accel_v060_signal(ppnenet, assets):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_21d_accel_v061_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_21d_accel_v062_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_21d_accel_v063_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_63d_accel_v064_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_63d_accel_v065_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_63d_accel_v066_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_126d_accel_v067_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_126d_accel_v068_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_126d_accel_v069_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_252d_accel_v070_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_252d_accel_v071_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_252d_accel_v072_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_504d_accel_v073_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_504d_accel_v074_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap ppnenet
def paf_f042_ppne_and_facilities_per_marketcap_504d_accel_v075_signal(ppnenet, marketcap):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_21d_accel_v076_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_21d_accel_v077_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_21d_accel_v078_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_63d_accel_v079_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_63d_accel_v080_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_63d_accel_v081_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_126d_accel_v082_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_126d_accel_v083_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_126d_accel_v084_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_252d_accel_v085_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_252d_accel_v086_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_252d_accel_v087_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_504d_accel_v088_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_504d_accel_v089_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity ppnenet
def paf_f042_ppne_and_facilities_per_equity_504d_accel_v090_signal(ppnenet, equity):
    base = _mean(_ppne_and_facilities_scaled(ppnenet, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ppnenet
def paf_f042_ppne_and_facilities_std_21d_accel_v091_signal(ppnenet, closeadj):
    base = _std(ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ppnenet
def paf_f042_ppne_and_facilities_std_21d_accel_v092_signal(ppnenet, closeadj):
    base = _std(ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ppnenet
def paf_f042_ppne_and_facilities_std_21d_accel_v093_signal(ppnenet, closeadj):
    base = _std(ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ppnenet
def paf_f042_ppne_and_facilities_std_63d_accel_v094_signal(ppnenet, closeadj):
    base = _std(ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ppnenet
def paf_f042_ppne_and_facilities_std_63d_accel_v095_signal(ppnenet, closeadj):
    base = _std(ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ppnenet
def paf_f042_ppne_and_facilities_std_63d_accel_v096_signal(ppnenet, closeadj):
    base = _std(ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ppnenet
def paf_f042_ppne_and_facilities_std_126d_accel_v097_signal(ppnenet, closeadj):
    base = _std(ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ppnenet
def paf_f042_ppne_and_facilities_std_126d_accel_v098_signal(ppnenet, closeadj):
    base = _std(ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ppnenet
def paf_f042_ppne_and_facilities_std_126d_accel_v099_signal(ppnenet, closeadj):
    base = _std(ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ppnenet
def paf_f042_ppne_and_facilities_std_252d_accel_v100_signal(ppnenet, closeadj):
    base = _std(ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ppnenet
def paf_f042_ppne_and_facilities_std_252d_accel_v101_signal(ppnenet, closeadj):
    base = _std(ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ppnenet
def paf_f042_ppne_and_facilities_std_252d_accel_v102_signal(ppnenet, closeadj):
    base = _std(ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ppnenet
def paf_f042_ppne_and_facilities_std_504d_accel_v103_signal(ppnenet, closeadj):
    base = _std(ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ppnenet
def paf_f042_ppne_and_facilities_std_504d_accel_v104_signal(ppnenet, closeadj):
    base = _std(ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ppnenet
def paf_f042_ppne_and_facilities_std_504d_accel_v105_signal(ppnenet, closeadj):
    base = _std(ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_21d_accel_v106_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_21d_accel_v107_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_21d_accel_v108_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_63d_accel_v109_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_63d_accel_v110_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_63d_accel_v111_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_126d_accel_v112_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_126d_accel_v113_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_126d_accel_v114_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_252d_accel_v115_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_252d_accel_v116_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_252d_accel_v117_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_504d_accel_v118_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_504d_accel_v119_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ppnenet
def paf_f042_ppne_and_facilities_ewm_504d_accel_v120_signal(ppnenet, closeadj):
    base = ppnenet.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ppnenet
def paf_f042_ppne_and_facilities_sq_21d_accel_v121_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ppnenet
def paf_f042_ppne_and_facilities_sq_21d_accel_v122_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ppnenet
def paf_f042_ppne_and_facilities_sq_21d_accel_v123_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ppnenet
def paf_f042_ppne_and_facilities_sq_63d_accel_v124_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ppnenet
def paf_f042_ppne_and_facilities_sq_63d_accel_v125_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ppnenet
def paf_f042_ppne_and_facilities_sq_63d_accel_v126_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ppnenet
def paf_f042_ppne_and_facilities_sq_126d_accel_v127_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ppnenet
def paf_f042_ppne_and_facilities_sq_126d_accel_v128_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ppnenet
def paf_f042_ppne_and_facilities_sq_126d_accel_v129_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ppnenet
def paf_f042_ppne_and_facilities_sq_252d_accel_v130_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ppnenet
def paf_f042_ppne_and_facilities_sq_252d_accel_v131_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ppnenet
def paf_f042_ppne_and_facilities_sq_252d_accel_v132_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ppnenet
def paf_f042_ppne_and_facilities_sq_504d_accel_v133_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ppnenet
def paf_f042_ppne_and_facilities_sq_504d_accel_v134_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ppnenet
def paf_f042_ppne_and_facilities_sq_504d_accel_v135_signal(ppnenet, closeadj):
    base = _mean(ppnenet * ppnenet, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ppnenet
def paf_f042_ppne_and_facilities_z_21d_accel_v136_signal(ppnenet):
    base = _z(ppnenet, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ppnenet
def paf_f042_ppne_and_facilities_z_21d_accel_v137_signal(ppnenet):
    base = _z(ppnenet, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ppnenet
def paf_f042_ppne_and_facilities_z_21d_accel_v138_signal(ppnenet):
    base = _z(ppnenet, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ppnenet
def paf_f042_ppne_and_facilities_z_63d_accel_v139_signal(ppnenet):
    base = _z(ppnenet, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ppnenet
def paf_f042_ppne_and_facilities_z_63d_accel_v140_signal(ppnenet):
    base = _z(ppnenet, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ppnenet
def paf_f042_ppne_and_facilities_z_63d_accel_v141_signal(ppnenet):
    base = _z(ppnenet, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ppnenet
def paf_f042_ppne_and_facilities_z_126d_accel_v142_signal(ppnenet):
    base = _z(ppnenet, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ppnenet
def paf_f042_ppne_and_facilities_z_126d_accel_v143_signal(ppnenet):
    base = _z(ppnenet, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ppnenet
def paf_f042_ppne_and_facilities_z_126d_accel_v144_signal(ppnenet):
    base = _z(ppnenet, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ppnenet
def paf_f042_ppne_and_facilities_z_252d_accel_v145_signal(ppnenet):
    base = _z(ppnenet, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ppnenet
def paf_f042_ppne_and_facilities_z_252d_accel_v146_signal(ppnenet):
    base = _z(ppnenet, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ppnenet
def paf_f042_ppne_and_facilities_z_252d_accel_v147_signal(ppnenet):
    base = _z(ppnenet, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ppnenet
def paf_f042_ppne_and_facilities_z_504d_accel_v148_signal(ppnenet):
    base = _z(ppnenet, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ppnenet
def paf_f042_ppne_and_facilities_z_504d_accel_v149_signal(ppnenet):
    base = _z(ppnenet, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ppnenet
def paf_f042_ppne_and_facilities_z_504d_accel_v150_signal(ppnenet):
    base = _z(ppnenet, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
