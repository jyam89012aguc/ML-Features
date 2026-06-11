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


# 63d z-score of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_z_63d_base_v076_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_z_126d_base_v077_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_z_252d_base_v078_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_z_504d_base_v079_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_z_63d_base_v080_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_z_126d_base_v081_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_z_252d_base_v082_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_z_504d_base_v083_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_z_63d_base_v084_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_z_126d_base_v085_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_z_252d_base_v086_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_z_504d_base_v087_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_z_63d_base_v088_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_z_126d_base_v089_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_z_252d_base_v090_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_z_504d_base_v091_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_z_63d_base_v092_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_z_126d_base_v093_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_z_252d_base_v094_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_z_504d_base_v095_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_z_63d_base_v096_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_z_126d_base_v097_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_z_252d_base_v098_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_z_504d_base_v099_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_z_63d_base_v100_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_z_126d_base_v101_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_z_252d_base_v102_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_z_504d_base_v103_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_z_63d_base_v104_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_z_126d_base_v105_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_z_252d_base_v106_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_z_504d_base_v107_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_z_63d_base_v108_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_z_126d_base_v109_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_z_252d_base_v110_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_z_504d_base_v111_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_z_63d_base_v112_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_z_126d_base_v113_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_z_252d_base_v114_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_z_504d_base_v115_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_z_63d_base_v116_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_z_126d_base_v117_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_z_252d_base_v118_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_add_postcar_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_21d_z_504d_base_v119_signal(abnormal_return_d, sp500_add_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_z_63d_base_v120_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_z_126d_base_v121_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_z_252d_base_v122_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_add_postcar_63d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_63d_z_504d_base_v123_signal(abnormal_return_d, sp500_add_post_window_63d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_63d, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_z_63d_base_v124_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_z_126d_base_v125_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_z_252d_base_v126_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_remove_car_5d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_5d_z_504d_base_v127_signal(abnormal_return_d, sp500_remove_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_5d, 5)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_z_63d_base_v128_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_z_126d_base_v129_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_z_252d_base_v130_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_remove_car_21d
def f100imr_f100_index_membership_and_relative_context_sp500_remove_car_21d_z_504d_base_v131_signal(abnormal_return_d, sp500_remove_post_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_remove_post_window_21d, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_z_63d_base_v132_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_z_126d_base_v133_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_z_252d_base_v134_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_days_since_addition
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_addition_z_504d_base_v135_signal(sp500_days_since_addition, closeadj):
    base = sp500_days_since_addition
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_z_63d_base_v136_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_z_126d_base_v137_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_z_252d_base_v138_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sp500_days_since_removal
def f100imr_f100_index_membership_and_relative_context_sp500_days_since_removal_z_504d_base_v139_signal(sp500_days_since_removal, closeadj):
    base = sp500_days_since_removal
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_z_63d_base_v140_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_z_126d_base_v141_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_z_252d_base_v142_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sector_rel_strength_63
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_63_z_504d_base_v143_signal(closeadj, sector_avg_return_63):
    base = closeadj.pct_change(periods=63) - sector_avg_return_63
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_z_63d_base_v144_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_z_126d_base_v145_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_z_252d_base_v146_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of sector_rel_strength_504
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_504_z_504d_base_v147_signal(closeadj, sector_avg_return_504):
    base = closeadj.pct_change(periods=504) - sector_avg_return_504
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_z_63d_base_v148_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_z_126d_base_v149_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_z_252d_base_v150_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_margin_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_fcf_margin_pctile_in_sector_z_504d_base_v151_signal(fcf_margin_sector_pctile, closeadj):
    base = fcf_margin_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_z_63d_base_v152_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_z_126d_base_v153_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_z_252d_base_v154_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_gm_pctile_in_sector_z_504d_base_v155_signal(gm_sector_pctile, closeadj):
    base = gm_sector_pctile
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_distmax_252d_base_v156_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of in_sp500
def f100imr_f100_index_membership_and_relative_context_in_sp500_distmax_504d_base_v157_signal(in_sp500_flag, closeadj):
    base = _f100_mem(in_sp500_flag)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_distmax_252d_base_v158_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sp500_addition_recent
def f100imr_f100_index_membership_and_relative_context_sp500_addition_recent_distmax_504d_base_v159_signal(sp500_days_since_addition, closeadj):
    base = (sp500_days_since_addition < 252).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_distmax_252d_base_v160_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sp500_removal_recent
def f100imr_f100_index_membership_and_relative_context_sp500_removal_recent_distmax_504d_base_v161_signal(sp500_days_since_removal, closeadj):
    base = (sp500_days_since_removal < 252).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_distmax_252d_base_v162_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sector_rel_strength_252
def f100imr_f100_index_membership_and_relative_context_sector_rel_strength_252_distmax_504d_base_v163_signal(closeadj, sector_avg_return_252):
    base = closeadj.pct_change(periods=252) - sector_avg_return_252
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_distmax_252d_base_v164_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of size_rank_in_sector
def f100imr_f100_index_membership_and_relative_context_size_rank_in_sector_distmax_504d_base_v165_signal(marketcap_sector_rank, closeadj):
    base = marketcap_sector_rank
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_distmax_252d_base_v166_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of growth_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_growth_pctile_in_sector_distmax_504d_base_v167_signal(revenue_growth_sector_pctile, closeadj):
    base = revenue_growth_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_distmax_252d_base_v168_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of multiple_pctile_in_sector
def f100imr_f100_index_membership_and_relative_context_multiple_pctile_in_sector_distmax_504d_base_v169_signal(evsales_sector_pctile, closeadj):
    base = evsales_sector_pctile
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_distmax_252d_base_v170_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sp500_add_predrift_21d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_21d_distmax_504d_base_v171_signal(abnormal_return_d, sp500_add_pre_window_21d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_21d, 21)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_distmax_252d_base_v172_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sp500_add_predrift_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_predrift_5d_distmax_504d_base_v173_signal(abnormal_return_d, sp500_add_pre_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_pre_window_5d, 5)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_distmax_252d_base_v174_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of sp500_add_postcar_5d
def f100imr_f100_index_membership_and_relative_context_sp500_add_postcar_5d_distmax_504d_base_v175_signal(abnormal_return_d, sp500_add_post_window_5d, closeadj):
    base = _f100_car_window(abnormal_return_d, sp500_add_post_window_5d, 5)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

