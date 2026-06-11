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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f100_mem(in_sp500):
    return in_sp500.astype(float)


def _f100_car_window(abnormal_return_d, window_flag, w):
    return (abnormal_return_d * window_flag).rolling(w, min_periods=1).sum()


# 21d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slope_21d_2d_v001_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slope_63d_2d_v002_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slope_126d_2d_v003_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slope_252d_2d_v004_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slope_504d_2d_v005_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slope_21d_2d_v006_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slope_63d_2d_v007_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slope_126d_2d_v008_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slope_252d_2d_v009_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slope_504d_2d_v010_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slope_21d_2d_v011_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slope_63d_2d_v012_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slope_126d_2d_v013_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slope_252d_2d_v014_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slope_504d_2d_v015_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slope_21d_2d_v016_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slope_63d_2d_v017_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slope_126d_2d_v018_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slope_252d_2d_v019_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slope_504d_2d_v020_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slope_21d_2d_v021_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slope_63d_2d_v022_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slope_126d_2d_v023_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slope_252d_2d_v024_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slope_504d_2d_v025_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slope_21d_2d_v026_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slope_63d_2d_v027_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slope_126d_2d_v028_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slope_252d_2d_v029_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slope_504d_2d_v030_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slope_21d_2d_v031_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slope_63d_2d_v032_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slope_126d_2d_v033_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slope_252d_2d_v034_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slope_504d_2d_v035_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slope_21d_2d_v036_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slope_63d_2d_v037_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slope_126d_2d_v038_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slope_252d_2d_v039_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slope_504d_2d_v040_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slope_21d_2d_v041_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slope_63d_2d_v042_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slope_126d_2d_v043_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slope_252d_2d_v044_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slope_504d_2d_v045_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slope_21d_2d_v046_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slope_63d_2d_v047_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slope_126d_2d_v048_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slope_252d_2d_v049_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slope_504d_2d_v050_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slope_21d_2d_v051_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slope_63d_2d_v052_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slope_126d_2d_v053_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slope_252d_2d_v054_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slope_504d_2d_v055_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slope_21d_2d_v056_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slope_63d_2d_v057_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slope_126d_2d_v058_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slope_252d_2d_v059_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slope_504d_2d_v060_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slope_21d_2d_v061_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slope_63d_2d_v062_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slope_126d_2d_v063_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slope_252d_2d_v064_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slope_504d_2d_v065_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slope_21d_2d_v066_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slope_63d_2d_v067_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slope_126d_2d_v068_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slope_252d_2d_v069_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slope_504d_2d_v070_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slope_21d_2d_v071_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slope_63d_2d_v072_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slope_126d_2d_v073_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slope_252d_2d_v074_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slope_504d_2d_v075_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slope_21d_2d_v076_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slope_63d_2d_v077_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slope_126d_2d_v078_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slope_252d_2d_v079_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slope_504d_2d_v080_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slope_21d_2d_v081_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slope_63d_2d_v082_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slope_126d_2d_v083_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slope_252d_2d_v084_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slope_504d_2d_v085_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slope_21d_2d_v086_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slope_63d_2d_v087_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slope_126d_2d_v088_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slope_252d_2d_v089_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slope_504d_2d_v090_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slope_21d_2d_v091_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slope_63d_2d_v092_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slope_126d_2d_v093_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slope_252d_2d_v094_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slope_504d_2d_v095_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slope_21d_2d_v096_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slope_63d_2d_v097_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slope_126d_2d_v098_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slope_252d_2d_v099_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slope_504d_2d_v100_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_sm21_sl21_2d_v101_signal(in_sp500_flag, closeadj):
    base = _mean(_f100_mem(in_sp500_flag), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_sm63_sl21_2d_v102_signal(in_sp500_flag, closeadj):
    base = _mean(_f100_mem(in_sp500_flag), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_sm63_sl63_2d_v103_signal(in_sp500_flag, closeadj):
    base = _mean(_f100_mem(in_sp500_flag), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_sm252_sl63_2d_v104_signal(in_sp500_flag, closeadj):
    base = _mean(_f100_mem(in_sp500_flag), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_sm252_sl126_2d_v105_signal(in_sp500_flag, closeadj):
    base = _mean(_f100_mem(in_sp500_flag), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_sm21_sl21_2d_v106_signal(sp500_days_since_addition, closeadj):
    base = _mean((sp500_days_since_addition < 252).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_sm63_sl21_2d_v107_signal(sp500_days_since_addition, closeadj):
    base = _mean((sp500_days_since_addition < 252).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_sm63_sl63_2d_v108_signal(sp500_days_since_addition, closeadj):
    base = _mean((sp500_days_since_addition < 252).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_sm252_sl63_2d_v109_signal(sp500_days_since_addition, closeadj):
    base = _mean((sp500_days_since_addition < 252).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_sm252_sl126_2d_v110_signal(sp500_days_since_addition, closeadj):
    base = _mean((sp500_days_since_addition < 252).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_sm21_sl21_2d_v111_signal(sp500_days_since_removal, closeadj):
    base = _mean((sp500_days_since_removal < 252).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_sm63_sl21_2d_v112_signal(sp500_days_since_removal, closeadj):
    base = _mean((sp500_days_since_removal < 252).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_sm63_sl63_2d_v113_signal(sp500_days_since_removal, closeadj):
    base = _mean((sp500_days_since_removal < 252).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_sm252_sl63_2d_v114_signal(sp500_days_since_removal, closeadj):
    base = _mean((sp500_days_since_removal < 252).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_sm252_sl126_2d_v115_signal(sp500_days_since_removal, closeadj):
    base = _mean((sp500_days_since_removal < 252).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_sm21_sl21_2d_v116_signal(closeadj, sector_avg_return_252):
    base = _mean(closeadj.pct_change(periods=252) - sector_avg_return_252, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_sm63_sl21_2d_v117_signal(closeadj, sector_avg_return_252):
    base = _mean(closeadj.pct_change(periods=252) - sector_avg_return_252, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_sm63_sl63_2d_v118_signal(closeadj, sector_avg_return_252):
    base = _mean(closeadj.pct_change(periods=252) - sector_avg_return_252, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_sm252_sl63_2d_v119_signal(closeadj, sector_avg_return_252):
    base = _mean(closeadj.pct_change(periods=252) - sector_avg_return_252, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_sm252_sl126_2d_v120_signal(closeadj, sector_avg_return_252):
    base = _mean(closeadj.pct_change(periods=252) - sector_avg_return_252, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_sm21_sl21_2d_v121_signal(marketcap_sector_rank, closeadj):
    base = _mean(marketcap_sector_rank, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_sm63_sl21_2d_v122_signal(marketcap_sector_rank, closeadj):
    base = _mean(marketcap_sector_rank, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_sm63_sl63_2d_v123_signal(marketcap_sector_rank, closeadj):
    base = _mean(marketcap_sector_rank, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_sm252_sl63_2d_v124_signal(marketcap_sector_rank, closeadj):
    base = _mean(marketcap_sector_rank, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_sm252_sl126_2d_v125_signal(marketcap_sector_rank, closeadj):
    base = _mean(marketcap_sector_rank, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_sm21_sl21_2d_v126_signal(revenue_growth_sector_pctile, closeadj):
    base = _mean(revenue_growth_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_sm63_sl21_2d_v127_signal(revenue_growth_sector_pctile, closeadj):
    base = _mean(revenue_growth_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_sm63_sl63_2d_v128_signal(revenue_growth_sector_pctile, closeadj):
    base = _mean(revenue_growth_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_sm252_sl63_2d_v129_signal(revenue_growth_sector_pctile, closeadj):
    base = _mean(revenue_growth_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_sm252_sl126_2d_v130_signal(revenue_growth_sector_pctile, closeadj):
    base = _mean(revenue_growth_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_sm21_sl21_2d_v131_signal(evsales_sector_pctile, closeadj):
    base = _mean(evsales_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_sm63_sl21_2d_v132_signal(evsales_sector_pctile, closeadj):
    base = _mean(evsales_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_sm63_sl63_2d_v133_signal(evsales_sector_pctile, closeadj):
    base = _mean(evsales_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_sm252_sl63_2d_v134_signal(evsales_sector_pctile, closeadj):
    base = _mean(evsales_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_sm252_sl126_2d_v135_signal(evsales_sector_pctile, closeadj):
    base = _mean(evsales_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_sm21_sl21_2d_v136_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_sm63_sl21_2d_v137_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_sm63_sl63_2d_v138_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_sm252_sl63_2d_v139_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_sm252_sl126_2d_v140_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_sm21_sl21_2d_v141_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_sm63_sl21_2d_v142_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_sm63_sl63_2d_v143_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_sm252_sl63_2d_v144_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_sm252_sl126_2d_v145_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_sm21_sl21_2d_v146_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_sm63_sl21_2d_v147_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_sm63_sl63_2d_v148_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_sm252_sl63_2d_v149_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_sm252_sl126_2d_v150_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_sm21_sl21_2d_v151_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_sm63_sl21_2d_v152_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_sm63_sl63_2d_v153_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_sm252_sl63_2d_v154_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_sm252_sl126_2d_v155_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_sm21_sl21_2d_v156_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_sm63_sl21_2d_v157_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_sm63_sl63_2d_v158_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_sm252_sl63_2d_v159_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_sm252_sl126_2d_v160_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_sm21_sl21_2d_v161_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_sm63_sl21_2d_v162_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_sm63_sl63_2d_v163_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_sm252_sl63_2d_v164_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_sm252_sl126_2d_v165_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_sm21_sl21_2d_v166_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_sm63_sl21_2d_v167_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_sm63_sl63_2d_v168_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_sm252_sl63_2d_v169_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_sm252_sl126_2d_v170_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _mean(_f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_sm21_sl21_2d_v171_signal(sp500_days_since_addition, closeadj):
    base = _mean(sp500_days_since_addition, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_sm63_sl21_2d_v172_signal(sp500_days_since_addition, closeadj):
    base = _mean(sp500_days_since_addition, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_sm63_sl63_2d_v173_signal(sp500_days_since_addition, closeadj):
    base = _mean(sp500_days_since_addition, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_sm252_sl63_2d_v174_signal(sp500_days_since_addition, closeadj):
    base = _mean(sp500_days_since_addition, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_sm252_sl126_2d_v175_signal(sp500_days_since_addition, closeadj):
    base = _mean(sp500_days_since_addition, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_sm21_sl21_2d_v176_signal(sp500_days_since_removal, closeadj):
    base = _mean(sp500_days_since_removal, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_sm63_sl21_2d_v177_signal(sp500_days_since_removal, closeadj):
    base = _mean(sp500_days_since_removal, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_sm63_sl63_2d_v178_signal(sp500_days_since_removal, closeadj):
    base = _mean(sp500_days_since_removal, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_sm252_sl63_2d_v179_signal(sp500_days_since_removal, closeadj):
    base = _mean(sp500_days_since_removal, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_sm252_sl126_2d_v180_signal(sp500_days_since_removal, closeadj):
    base = _mean(sp500_days_since_removal, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_sm21_sl21_2d_v181_signal(closeadj, sector_avg_return_63):
    base = _mean(closeadj.pct_change(periods=63) - sector_avg_return_63, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_sm63_sl21_2d_v182_signal(closeadj, sector_avg_return_63):
    base = _mean(closeadj.pct_change(periods=63) - sector_avg_return_63, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_sm63_sl63_2d_v183_signal(closeadj, sector_avg_return_63):
    base = _mean(closeadj.pct_change(periods=63) - sector_avg_return_63, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_sm252_sl63_2d_v184_signal(closeadj, sector_avg_return_63):
    base = _mean(closeadj.pct_change(periods=63) - sector_avg_return_63, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_sm252_sl126_2d_v185_signal(closeadj, sector_avg_return_63):
    base = _mean(closeadj.pct_change(periods=63) - sector_avg_return_63, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_sm21_sl21_2d_v186_signal(closeadj, sector_avg_return_504):
    base = _mean(closeadj.pct_change(periods=504) - sector_avg_return_504, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_sm63_sl21_2d_v187_signal(closeadj, sector_avg_return_504):
    base = _mean(closeadj.pct_change(periods=504) - sector_avg_return_504, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_sm63_sl63_2d_v188_signal(closeadj, sector_avg_return_504):
    base = _mean(closeadj.pct_change(periods=504) - sector_avg_return_504, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_sm252_sl63_2d_v189_signal(closeadj, sector_avg_return_504):
    base = _mean(closeadj.pct_change(periods=504) - sector_avg_return_504, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_sm252_sl126_2d_v190_signal(closeadj, sector_avg_return_504):
    base = _mean(closeadj.pct_change(periods=504) - sector_avg_return_504, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_sm21_sl21_2d_v191_signal(fcf_margin_sector_pctile, closeadj):
    base = _mean(fcf_margin_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_sm63_sl21_2d_v192_signal(fcf_margin_sector_pctile, closeadj):
    base = _mean(fcf_margin_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_sm63_sl63_2d_v193_signal(fcf_margin_sector_pctile, closeadj):
    base = _mean(fcf_margin_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_sm252_sl63_2d_v194_signal(fcf_margin_sector_pctile, closeadj):
    base = _mean(fcf_margin_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_sm252_sl126_2d_v195_signal(fcf_margin_sector_pctile, closeadj):
    base = _mean(fcf_margin_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_sm21_sl21_2d_v196_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_sm63_sl21_2d_v197_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_sm63_sl63_2d_v198_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_sm252_sl63_2d_v199_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_sm252_sl126_2d_v200_signal(gm_sector_pctile, closeadj):
    base = _mean(gm_sector_pctile, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

