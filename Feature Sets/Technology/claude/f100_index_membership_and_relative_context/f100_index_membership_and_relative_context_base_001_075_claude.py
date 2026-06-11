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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f100_mem(in_sp500):
    return in_sp500.astype(float)


def _f100_car_window(abnormal_return_d, window_flag, w):
    return (abnormal_return_d * window_flag).rolling(w, min_periods=1).sum()


# 21d mean of in_sp500 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_in_sp500_mean_21d_base_v001_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of in_sp500 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_in_sp500_mean_63d_base_v002_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of in_sp500 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_in_sp500_mean_126d_base_v003_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of in_sp500 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_in_sp500_mean_252d_base_v004_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of in_sp500 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_in_sp500_mean_504d_base_v005_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_addition_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_mean_21d_base_v006_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_addition_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_mean_63d_base_v007_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_addition_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_mean_126d_base_v008_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_addition_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_mean_252d_base_v009_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_addition_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_mean_504d_base_v010_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_removal_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_mean_21d_base_v011_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_removal_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_mean_63d_base_v012_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_removal_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_mean_126d_base_v013_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_removal_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_mean_252d_base_v014_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_removal_recent scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_mean_504d_base_v015_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sector_rel_strength_252 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_mean_21d_base_v016_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sector_rel_strength_252 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_mean_63d_base_v017_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sector_rel_strength_252 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_mean_126d_base_v018_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sector_rel_strength_252 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_mean_252d_base_v019_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sector_rel_strength_252 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_mean_504d_base_v020_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of size_rank_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_mean_21d_base_v021_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of size_rank_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_mean_63d_base_v022_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of size_rank_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_mean_126d_base_v023_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of size_rank_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_mean_252d_base_v024_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of size_rank_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_mean_504d_base_v025_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of growth_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_mean_21d_base_v026_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of growth_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_mean_63d_base_v027_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of growth_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_mean_126d_base_v028_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of growth_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_mean_252d_base_v029_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of growth_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_mean_504d_base_v030_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of multiple_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_mean_21d_base_v031_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of multiple_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_mean_63d_base_v032_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of multiple_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_mean_126d_base_v033_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of multiple_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_mean_252d_base_v034_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of multiple_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_mean_504d_base_v035_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_add_predrift_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_mean_21d_base_v036_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_add_predrift_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_mean_63d_base_v037_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_add_predrift_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_mean_126d_base_v038_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_add_predrift_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_mean_252d_base_v039_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_add_predrift_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_mean_504d_base_v040_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_add_predrift_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_mean_21d_base_v041_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_add_predrift_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_mean_63d_base_v042_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_add_predrift_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_mean_126d_base_v043_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_add_predrift_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_mean_252d_base_v044_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_add_predrift_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_mean_504d_base_v045_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_add_postcar_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_mean_21d_base_v046_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_add_postcar_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_mean_63d_base_v047_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_add_postcar_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_mean_126d_base_v048_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_add_postcar_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_mean_252d_base_v049_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_add_postcar_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_mean_504d_base_v050_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_add_postcar_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_mean_21d_base_v051_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_add_postcar_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_mean_63d_base_v052_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_add_postcar_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_mean_126d_base_v053_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_add_postcar_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_mean_252d_base_v054_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_add_postcar_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_mean_504d_base_v055_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_add_postcar_63d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_mean_21d_base_v056_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_add_postcar_63d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_mean_63d_base_v057_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_add_postcar_63d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_mean_126d_base_v058_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_add_postcar_63d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_mean_252d_base_v059_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_add_postcar_63d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_mean_504d_base_v060_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_remove_car_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_mean_21d_base_v061_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_remove_car_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_mean_63d_base_v062_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_remove_car_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_mean_126d_base_v063_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_remove_car_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_mean_252d_base_v064_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_remove_car_5d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_mean_504d_base_v065_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_remove_car_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_mean_21d_base_v066_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_remove_car_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_mean_63d_base_v067_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_remove_car_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_mean_126d_base_v068_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_remove_car_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_mean_252d_base_v069_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_remove_car_21d scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_mean_504d_base_v070_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_days_since_addition scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_mean_21d_base_v071_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_days_since_addition scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_mean_63d_base_v072_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_days_since_addition scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_mean_126d_base_v073_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_days_since_addition scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_mean_252d_base_v074_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_days_since_addition scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_mean_504d_base_v075_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sp500_days_since_removal scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_mean_21d_base_v076_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sp500_days_since_removal scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_mean_63d_base_v077_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sp500_days_since_removal scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_mean_126d_base_v078_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sp500_days_since_removal scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_mean_252d_base_v079_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sp500_days_since_removal scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_mean_504d_base_v080_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sector_rel_strength_63 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_mean_21d_base_v081_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sector_rel_strength_63 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_mean_63d_base_v082_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sector_rel_strength_63 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_mean_126d_base_v083_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sector_rel_strength_63 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_mean_252d_base_v084_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sector_rel_strength_63 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_mean_504d_base_v085_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of sector_rel_strength_504 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_mean_21d_base_v086_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of sector_rel_strength_504 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_mean_63d_base_v087_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of sector_rel_strength_504 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_mean_126d_base_v088_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of sector_rel_strength_504 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_mean_252d_base_v089_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of sector_rel_strength_504 scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_mean_504d_base_v090_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_margin_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_mean_21d_base_v091_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_margin_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_mean_63d_base_v092_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_margin_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_mean_126d_base_v093_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_margin_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_mean_252d_base_v094_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_margin_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_mean_504d_base_v095_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_mean_21d_base_v096_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_mean_63d_base_v097_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_mean_126d_base_v098_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_mean_252d_base_v099_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_pctile_in_sector scaled by closeadj
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_mean_504d_base_v100_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

