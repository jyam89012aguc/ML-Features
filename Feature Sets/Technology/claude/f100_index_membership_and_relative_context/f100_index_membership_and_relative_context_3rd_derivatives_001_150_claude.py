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


# 21d acceleration of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_accel_21d_3d_v001_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_accel_63d_3d_v002_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_accel_126d_3d_v003_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_accel_252d_3d_v004_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_accel_21d_3d_v005_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_accel_63d_3d_v006_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_accel_126d_3d_v007_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_accel_252d_3d_v008_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_accel_21d_3d_v009_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_accel_63d_3d_v010_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_accel_126d_3d_v011_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_accel_252d_3d_v012_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_accel_21d_3d_v013_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_accel_63d_3d_v014_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_accel_126d_3d_v015_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_accel_252d_3d_v016_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_accel_21d_3d_v017_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_accel_63d_3d_v018_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_accel_126d_3d_v019_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_accel_252d_3d_v020_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_accel_21d_3d_v021_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_accel_63d_3d_v022_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_accel_126d_3d_v023_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_accel_252d_3d_v024_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_accel_21d_3d_v025_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_accel_63d_3d_v026_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_accel_126d_3d_v027_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_accel_252d_3d_v028_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_accel_21d_3d_v029_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_accel_63d_3d_v030_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_accel_126d_3d_v031_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_accel_252d_3d_v032_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_accel_21d_3d_v033_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_accel_63d_3d_v034_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_accel_126d_3d_v035_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_accel_252d_3d_v036_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_accel_21d_3d_v037_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_accel_63d_3d_v038_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_accel_126d_3d_v039_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_accel_252d_3d_v040_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_accel_21d_3d_v041_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_accel_63d_3d_v042_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_accel_126d_3d_v043_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_accel_252d_3d_v044_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_accel_21d_3d_v045_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_accel_63d_3d_v046_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_accel_126d_3d_v047_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_accel_252d_3d_v048_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_accel_21d_3d_v049_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_accel_63d_3d_v050_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_accel_126d_3d_v051_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_accel_252d_3d_v052_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_accel_21d_3d_v053_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_accel_63d_3d_v054_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_accel_126d_3d_v055_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_accel_252d_3d_v056_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_accel_21d_3d_v057_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_accel_63d_3d_v058_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_accel_126d_3d_v059_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_accel_252d_3d_v060_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_accel_21d_3d_v061_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_accel_63d_3d_v062_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_accel_126d_3d_v063_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_accel_252d_3d_v064_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_accel_21d_3d_v065_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_accel_63d_3d_v066_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_accel_126d_3d_v067_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_accel_252d_3d_v068_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_accel_21d_3d_v069_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_accel_63d_3d_v070_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_accel_126d_3d_v071_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_accel_252d_3d_v072_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_accel_21d_3d_v073_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_accel_63d_3d_v074_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_accel_126d_3d_v075_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_accel_252d_3d_v076_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_accel_21d_3d_v077_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_accel_63d_3d_v078_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_accel_126d_3d_v079_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_accel_252d_3d_v080_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slopez_21d_z126_3d_v081_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slopez_63d_z252_3d_v082_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slopez_126d_z252_3d_v083_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_slopez_252d_z504_3d_v084_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slopez_21d_z126_3d_v085_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slopez_63d_z252_3d_v086_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slopez_126d_z252_3d_v087_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_slopez_252d_z504_3d_v088_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slopez_21d_z126_3d_v089_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slopez_63d_z252_3d_v090_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slopez_126d_z252_3d_v091_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_slopez_252d_z504_3d_v092_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slopez_21d_z126_3d_v093_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slopez_63d_z252_3d_v094_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slopez_126d_z252_3d_v095_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_slopez_252d_z504_3d_v096_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slopez_21d_z126_3d_v097_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slopez_63d_z252_3d_v098_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slopez_126d_z252_3d_v099_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_slopez_252d_z504_3d_v100_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slopez_21d_z126_3d_v101_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slopez_63d_z252_3d_v102_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slopez_126d_z252_3d_v103_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_slopez_252d_z504_3d_v104_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slopez_21d_z126_3d_v105_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slopez_63d_z252_3d_v106_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slopez_126d_z252_3d_v107_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_slopez_252d_z504_3d_v108_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slopez_21d_z126_3d_v109_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slopez_63d_z252_3d_v110_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slopez_126d_z252_3d_v111_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_slopez_252d_z504_3d_v112_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slopez_21d_z126_3d_v113_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slopez_63d_z252_3d_v114_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slopez_126d_z252_3d_v115_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_slopez_252d_z504_3d_v116_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slopez_21d_z126_3d_v117_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slopez_63d_z252_3d_v118_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slopez_126d_z252_3d_v119_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_slopez_252d_z504_3d_v120_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slopez_21d_z126_3d_v121_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slopez_63d_z252_3d_v122_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slopez_126d_z252_3d_v123_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_slopez_252d_z504_3d_v124_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slopez_21d_z126_3d_v125_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slopez_63d_z252_3d_v126_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slopez_126d_z252_3d_v127_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_slopez_252d_z504_3d_v128_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slopez_21d_z126_3d_v129_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slopez_63d_z252_3d_v130_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slopez_126d_z252_3d_v131_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_slopez_252d_z504_3d_v132_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slopez_21d_z126_3d_v133_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slopez_63d_z252_3d_v134_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slopez_126d_z252_3d_v135_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_slopez_252d_z504_3d_v136_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slopez_21d_z126_3d_v137_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slopez_63d_z252_3d_v138_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slopez_126d_z252_3d_v139_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_slopez_252d_z504_3d_v140_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slopez_21d_z126_3d_v141_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slopez_63d_z252_3d_v142_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slopez_126d_z252_3d_v143_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_slopez_252d_z504_3d_v144_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slopez_21d_z126_3d_v145_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slopez_63d_z252_3d_v146_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slopez_126d_z252_3d_v147_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_slopez_252d_z504_3d_v148_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slopez_21d_z126_3d_v149_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slopez_63d_z252_3d_v150_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slopez_126d_z252_3d_v151_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_slopez_252d_z504_3d_v152_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slopez_21d_z126_3d_v153_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slopez_63d_z252_3d_v154_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slopez_126d_z252_3d_v155_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_slopez_252d_z504_3d_v156_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slopez_21d_z126_3d_v157_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slopez_63d_z252_3d_v158_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slopez_126d_z252_3d_v159_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_slopez_252d_z504_3d_v160_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_jerk_21d_3d_v161_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_jerk_63d_3d_v162_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_jerk_126d_3d_v163_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_jerk_21d_3d_v164_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_jerk_63d_3d_v165_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_jerk_126d_3d_v166_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_jerk_21d_3d_v167_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_jerk_63d_3d_v168_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_jerk_126d_3d_v169_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_jerk_21d_3d_v170_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_jerk_63d_3d_v171_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_jerk_126d_3d_v172_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_jerk_21d_3d_v173_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_jerk_63d_3d_v174_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_jerk_126d_3d_v175_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_jerk_21d_3d_v176_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_jerk_63d_3d_v177_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_jerk_126d_3d_v178_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_jerk_21d_3d_v179_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_jerk_63d_3d_v180_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_jerk_126d_3d_v181_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_jerk_21d_3d_v182_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_jerk_63d_3d_v183_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_jerk_126d_3d_v184_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_jerk_21d_3d_v185_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_jerk_63d_3d_v186_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_jerk_126d_3d_v187_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_jerk_21d_3d_v188_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_jerk_63d_3d_v189_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_jerk_126d_3d_v190_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_jerk_21d_3d_v191_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_jerk_63d_3d_v192_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_jerk_126d_3d_v193_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_jerk_21d_3d_v194_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_jerk_63d_3d_v195_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_jerk_126d_3d_v196_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_jerk_21d_3d_v197_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_jerk_63d_3d_v198_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_jerk_126d_3d_v199_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_jerk_21d_3d_v200_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

