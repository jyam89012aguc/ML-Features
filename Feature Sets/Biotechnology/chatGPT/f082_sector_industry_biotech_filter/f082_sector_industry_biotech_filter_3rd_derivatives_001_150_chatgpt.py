"""Family f082 - Sector and industry biotech filter (Security Master and Universe) | Sharadar tables: TICKERS | fields: sector, industry, sicsector, sicindustry, famasector, famaindustry | 3rd derivatives 001-150"""
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
def _sector_industry_biotech_filter_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sector_industry_biotech_filter_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sector_industry_biotech_filter_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_21d_accel_v001_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_21d_accel_v002_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_21d_accel_v003_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_63d_accel_v004_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_63d_accel_v005_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_63d_accel_v006_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_126d_accel_v007_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_126d_accel_v008_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_126d_accel_v009_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_252d_accel_v010_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_252d_accel_v011_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_252d_accel_v012_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_504d_accel_v013_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_504d_accel_v014_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_504d_accel_v015_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_21d_accel_v016_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_21d_accel_v017_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_21d_accel_v018_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_63d_accel_v019_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_63d_accel_v020_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_63d_accel_v021_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_126d_accel_v022_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_126d_accel_v023_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_126d_accel_v024_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_252d_accel_v025_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_252d_accel_v026_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_252d_accel_v027_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_504d_accel_v028_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_504d_accel_v029_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_504d_accel_v030_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_21d_accel_v031_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_21d_accel_v032_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_21d_accel_v033_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_63d_accel_v034_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_63d_accel_v035_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_63d_accel_v036_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_126d_accel_v037_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_126d_accel_v038_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_126d_accel_v039_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_252d_accel_v040_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_252d_accel_v041_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_252d_accel_v042_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_504d_accel_v043_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_504d_accel_v044_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_504d_accel_v045_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_21d_accel_v046_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_21d_accel_v047_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_21d_accel_v048_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_accel_v049_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_accel_v050_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_accel_v051_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_126d_accel_v052_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_126d_accel_v053_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_126d_accel_v054_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_accel_v055_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_accel_v056_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_accel_v057_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_accel_v058_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_accel_v059_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_accel_v060_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_21d_accel_v061_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_21d_accel_v062_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_21d_accel_v063_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_accel_v064_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_accel_v065_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_accel_v066_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_126d_accel_v067_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_126d_accel_v068_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_126d_accel_v069_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_accel_v070_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_accel_v071_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_accel_v072_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_accel_v073_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_accel_v074_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_accel_v075_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_21d_accel_v076_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_21d_accel_v077_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_21d_accel_v078_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_accel_v079_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_accel_v080_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_accel_v081_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_126d_accel_v082_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_126d_accel_v083_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_126d_accel_v084_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_accel_v085_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_accel_v086_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_accel_v087_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_accel_v088_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_accel_v089_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_accel_v090_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_21d_accel_v091_signal(sector_rank, closeadj):
    base = _std(sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_21d_accel_v092_signal(sector_rank, closeadj):
    base = _std(sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_21d_accel_v093_signal(sector_rank, closeadj):
    base = _std(sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_63d_accel_v094_signal(sector_rank, closeadj):
    base = _std(sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_63d_accel_v095_signal(sector_rank, closeadj):
    base = _std(sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_63d_accel_v096_signal(sector_rank, closeadj):
    base = _std(sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_126d_accel_v097_signal(sector_rank, closeadj):
    base = _std(sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_126d_accel_v098_signal(sector_rank, closeadj):
    base = _std(sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_126d_accel_v099_signal(sector_rank, closeadj):
    base = _std(sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_252d_accel_v100_signal(sector_rank, closeadj):
    base = _std(sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_252d_accel_v101_signal(sector_rank, closeadj):
    base = _std(sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_252d_accel_v102_signal(sector_rank, closeadj):
    base = _std(sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_504d_accel_v103_signal(sector_rank, closeadj):
    base = _std(sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_504d_accel_v104_signal(sector_rank, closeadj):
    base = _std(sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_504d_accel_v105_signal(sector_rank, closeadj):
    base = _std(sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_21d_accel_v106_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_21d_accel_v107_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_21d_accel_v108_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_63d_accel_v109_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_63d_accel_v110_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_63d_accel_v111_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_126d_accel_v112_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_126d_accel_v113_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_126d_accel_v114_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_252d_accel_v115_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_252d_accel_v116_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_252d_accel_v117_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_504d_accel_v118_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_504d_accel_v119_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_504d_accel_v120_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_21d_accel_v121_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_21d_accel_v122_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_21d_accel_v123_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_63d_accel_v124_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_63d_accel_v125_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_63d_accel_v126_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_126d_accel_v127_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_126d_accel_v128_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_126d_accel_v129_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_252d_accel_v130_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_252d_accel_v131_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_252d_accel_v132_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_504d_accel_v133_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_504d_accel_v134_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_504d_accel_v135_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_21d_accel_v136_signal(sector_rank):
    base = _z(sector_rank, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_21d_accel_v137_signal(sector_rank):
    base = _z(sector_rank, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_21d_accel_v138_signal(sector_rank):
    base = _z(sector_rank, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_accel_v139_signal(sector_rank):
    base = _z(sector_rank, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_accel_v140_signal(sector_rank):
    base = _z(sector_rank, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_accel_v141_signal(sector_rank):
    base = _z(sector_rank, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_accel_v142_signal(sector_rank):
    base = _z(sector_rank, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_accel_v143_signal(sector_rank):
    base = _z(sector_rank, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_accel_v144_signal(sector_rank):
    base = _z(sector_rank, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_accel_v145_signal(sector_rank):
    base = _z(sector_rank, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_accel_v146_signal(sector_rank):
    base = _z(sector_rank, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_accel_v147_signal(sector_rank):
    base = _z(sector_rank, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_accel_v148_signal(sector_rank):
    base = _z(sector_rank, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_accel_v149_signal(sector_rank):
    base = _z(sector_rank, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_accel_v150_signal(sector_rank):
    base = _z(sector_rank, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
