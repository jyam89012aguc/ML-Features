"""Family f082 - Sector and industry biotech filter (Security Master and Universe) | Sharadar tables: TICKERS | fields: sector, industry, sicsector, sicindustry, famasector, famaindustry | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_21d_slope_v001_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_21d_slope_v002_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_21d_slope_v003_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_63d_slope_v004_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_63d_slope_v005_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_63d_slope_v006_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_126d_slope_v007_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_126d_slope_v008_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_126d_slope_v009_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_252d_slope_v010_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_252d_slope_v011_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_252d_slope_v012_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_504d_slope_v013_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_504d_slope_v014_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sector_rank
def sibf_f082_sector_industry_biotech_filter_raw_504d_slope_v015_signal(sector_rank, closeadj):
    base = _mean(sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_21d_slope_v016_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_21d_slope_v017_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_21d_slope_v018_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_63d_slope_v019_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_63d_slope_v020_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_63d_slope_v021_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_126d_slope_v022_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_126d_slope_v023_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_126d_slope_v024_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_252d_slope_v025_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_252d_slope_v026_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_252d_slope_v027_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_504d_slope_v028_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_504d_slope_v029_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sector_rank
def sibf_f082_sector_industry_biotech_filter_log_504d_slope_v030_signal(sector_rank, closeadj):
    base = _mean(_sector_industry_biotech_filter_log(sector_rank), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_21d_slope_v031_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_21d_slope_v032_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_21d_slope_v033_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_63d_slope_v034_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_63d_slope_v035_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_63d_slope_v036_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_126d_slope_v037_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_126d_slope_v038_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_126d_slope_v039_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_252d_slope_v040_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_252d_slope_v041_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_252d_slope_v042_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_504d_slope_v043_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_504d_slope_v044_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sector_rank
def sibf_f082_sector_industry_biotech_filter_pershare_504d_slope_v045_signal(sector_rank, sharesbas, closeadj):
    base = _mean(_sector_industry_biotech_filter_per_share(sector_rank, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_21d_slope_v046_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_21d_slope_v047_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_21d_slope_v048_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_slope_v049_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_slope_v050_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_63d_slope_v051_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_126d_slope_v052_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_126d_slope_v053_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_126d_slope_v054_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_slope_v055_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_slope_v056_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_252d_slope_v057_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_slope_v058_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_slope_v059_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sector_rank
def sibf_f082_sector_industry_biotech_filter_per_assets_504d_slope_v060_signal(sector_rank, assets):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_21d_slope_v061_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_21d_slope_v062_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_21d_slope_v063_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_slope_v064_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_slope_v065_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_63d_slope_v066_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_126d_slope_v067_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_126d_slope_v068_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_126d_slope_v069_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_slope_v070_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_slope_v071_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_252d_slope_v072_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_slope_v073_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_slope_v074_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sector_rank
def sibf_f082_sector_industry_biotech_filter_per_marketcap_504d_slope_v075_signal(sector_rank, marketcap):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_21d_slope_v076_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_21d_slope_v077_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_21d_slope_v078_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_slope_v079_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_slope_v080_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_63d_slope_v081_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_126d_slope_v082_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_126d_slope_v083_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_126d_slope_v084_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_slope_v085_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_slope_v086_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_252d_slope_v087_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_slope_v088_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_slope_v089_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity sector_rank
def sibf_f082_sector_industry_biotech_filter_per_equity_504d_slope_v090_signal(sector_rank, equity):
    base = _mean(_sector_industry_biotech_filter_scaled(sector_rank, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_21d_slope_v091_signal(sector_rank, closeadj):
    base = _std(sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_21d_slope_v092_signal(sector_rank, closeadj):
    base = _std(sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_21d_slope_v093_signal(sector_rank, closeadj):
    base = _std(sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_63d_slope_v094_signal(sector_rank, closeadj):
    base = _std(sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_63d_slope_v095_signal(sector_rank, closeadj):
    base = _std(sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_63d_slope_v096_signal(sector_rank, closeadj):
    base = _std(sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_126d_slope_v097_signal(sector_rank, closeadj):
    base = _std(sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_126d_slope_v098_signal(sector_rank, closeadj):
    base = _std(sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_126d_slope_v099_signal(sector_rank, closeadj):
    base = _std(sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_252d_slope_v100_signal(sector_rank, closeadj):
    base = _std(sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_252d_slope_v101_signal(sector_rank, closeadj):
    base = _std(sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_252d_slope_v102_signal(sector_rank, closeadj):
    base = _std(sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_504d_slope_v103_signal(sector_rank, closeadj):
    base = _std(sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_504d_slope_v104_signal(sector_rank, closeadj):
    base = _std(sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sector_rank
def sibf_f082_sector_industry_biotech_filter_std_504d_slope_v105_signal(sector_rank, closeadj):
    base = _std(sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_21d_slope_v106_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_21d_slope_v107_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_21d_slope_v108_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_63d_slope_v109_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_63d_slope_v110_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_63d_slope_v111_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_126d_slope_v112_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_126d_slope_v113_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_126d_slope_v114_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_252d_slope_v115_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_252d_slope_v116_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_252d_slope_v117_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_504d_slope_v118_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_504d_slope_v119_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sector_rank
def sibf_f082_sector_industry_biotech_filter_ewm_504d_slope_v120_signal(sector_rank, closeadj):
    base = sector_rank.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_21d_slope_v121_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_21d_slope_v122_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_21d_slope_v123_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_63d_slope_v124_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_63d_slope_v125_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_63d_slope_v126_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_126d_slope_v127_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_126d_slope_v128_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_126d_slope_v129_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_252d_slope_v130_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_252d_slope_v131_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_252d_slope_v132_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_504d_slope_v133_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_504d_slope_v134_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sector_rank
def sibf_f082_sector_industry_biotech_filter_sq_504d_slope_v135_signal(sector_rank, closeadj):
    base = _mean(sector_rank * sector_rank, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_21d_slope_v136_signal(sector_rank):
    base = _z(sector_rank, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_21d_slope_v137_signal(sector_rank):
    base = _z(sector_rank, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_21d_slope_v138_signal(sector_rank):
    base = _z(sector_rank, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_slope_v139_signal(sector_rank):
    base = _z(sector_rank, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_slope_v140_signal(sector_rank):
    base = _z(sector_rank, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_63d_slope_v141_signal(sector_rank):
    base = _z(sector_rank, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_slope_v142_signal(sector_rank):
    base = _z(sector_rank, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_slope_v143_signal(sector_rank):
    base = _z(sector_rank, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_126d_slope_v144_signal(sector_rank):
    base = _z(sector_rank, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_slope_v145_signal(sector_rank):
    base = _z(sector_rank, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_slope_v146_signal(sector_rank):
    base = _z(sector_rank, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_252d_slope_v147_signal(sector_rank):
    base = _z(sector_rank, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_slope_v148_signal(sector_rank):
    base = _z(sector_rank, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_slope_v149_signal(sector_rank):
    base = _z(sector_rank, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sector_rank
def sibf_f082_sector_industry_biotech_filter_z_504d_slope_v150_signal(sector_rank):
    base = _z(sector_rank, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
