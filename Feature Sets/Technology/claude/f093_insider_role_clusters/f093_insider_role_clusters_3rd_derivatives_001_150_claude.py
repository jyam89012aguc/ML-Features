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
def _f093_unique_count(unique_insider_count):
    return unique_insider_count


# 21d acceleration of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_accel_21d_3d_v001_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_accel_63d_3d_v002_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_accel_126d_3d_v003_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_accel_252d_3d_v004_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_accel_21d_3d_v005_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_accel_63d_3d_v006_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_accel_126d_3d_v007_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_accel_252d_3d_v008_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_accel_21d_3d_v009_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_accel_63d_3d_v010_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_accel_126d_3d_v011_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_accel_252d_3d_v012_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_accel_21d_3d_v013_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_accel_63d_3d_v014_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_accel_126d_3d_v015_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_accel_252d_3d_v016_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_accel_21d_3d_v017_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_accel_63d_3d_v018_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_accel_126d_3d_v019_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_accel_252d_3d_v020_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_accel_21d_3d_v021_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_accel_63d_3d_v022_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_accel_126d_3d_v023_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_accel_252d_3d_v024_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_accel_21d_3d_v025_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_accel_63d_3d_v026_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_accel_126d_3d_v027_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_accel_252d_3d_v028_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_accel_21d_3d_v029_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_accel_63d_3d_v030_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_accel_126d_3d_v031_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_accel_252d_3d_v032_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_accel_21d_3d_v033_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_accel_63d_3d_v034_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_accel_126d_3d_v035_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_accel_252d_3d_v036_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_accel_21d_3d_v037_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_accel_63d_3d_v038_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_accel_126d_3d_v039_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_accel_252d_3d_v040_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_accel_21d_3d_v041_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_accel_63d_3d_v042_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_accel_126d_3d_v043_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_accel_252d_3d_v044_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_accel_21d_3d_v045_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_accel_63d_3d_v046_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_accel_126d_3d_v047_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_accel_252d_3d_v048_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_accel_21d_3d_v049_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_accel_63d_3d_v050_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_accel_126d_3d_v051_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_accel_252d_3d_v052_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_accel_21d_3d_v053_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_accel_63d_3d_v054_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_accel_126d_3d_v055_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_accel_252d_3d_v056_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_accel_21d_3d_v057_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_accel_63d_3d_v058_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_accel_126d_3d_v059_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_accel_252d_3d_v060_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_accel_21d_3d_v061_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_accel_63d_3d_v062_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_accel_126d_3d_v063_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_accel_252d_3d_v064_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_accel_21d_3d_v065_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_accel_63d_3d_v066_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_accel_126d_3d_v067_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_accel_252d_3d_v068_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_accel_21d_3d_v069_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_accel_63d_3d_v070_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_accel_126d_3d_v071_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_accel_252d_3d_v072_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_accel_21d_3d_v073_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_accel_63d_3d_v074_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_accel_126d_3d_v075_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_accel_252d_3d_v076_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_accel_21d_3d_v077_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_accel_63d_3d_v078_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_accel_126d_3d_v079_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_accel_252d_3d_v080_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_accel_21d_3d_v081_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_accel_63d_3d_v082_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_accel_126d_3d_v083_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_accel_252d_3d_v084_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_accel_21d_3d_v085_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_accel_63d_3d_v086_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_accel_126d_3d_v087_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_accel_252d_3d_v088_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slopez_21d_z126_3d_v089_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slopez_63d_z252_3d_v090_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slopez_126d_z252_3d_v091_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slopez_252d_z504_3d_v092_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slopez_21d_z126_3d_v093_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slopez_63d_z252_3d_v094_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slopez_126d_z252_3d_v095_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slopez_252d_z504_3d_v096_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slopez_21d_z126_3d_v097_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slopez_63d_z252_3d_v098_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slopez_126d_z252_3d_v099_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slopez_252d_z504_3d_v100_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slopez_21d_z126_3d_v101_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slopez_63d_z252_3d_v102_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slopez_126d_z252_3d_v103_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slopez_252d_z504_3d_v104_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slopez_21d_z126_3d_v105_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slopez_63d_z252_3d_v106_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slopez_126d_z252_3d_v107_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slopez_252d_z504_3d_v108_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slopez_21d_z126_3d_v109_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slopez_63d_z252_3d_v110_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slopez_126d_z252_3d_v111_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slopez_252d_z504_3d_v112_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slopez_21d_z126_3d_v113_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slopez_63d_z252_3d_v114_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slopez_126d_z252_3d_v115_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slopez_252d_z504_3d_v116_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slopez_21d_z126_3d_v117_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slopez_63d_z252_3d_v118_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slopez_126d_z252_3d_v119_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slopez_252d_z504_3d_v120_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slopez_21d_z126_3d_v121_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slopez_63d_z252_3d_v122_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slopez_126d_z252_3d_v123_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slopez_252d_z504_3d_v124_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slopez_21d_z126_3d_v125_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slopez_63d_z252_3d_v126_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slopez_126d_z252_3d_v127_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slopez_252d_z504_3d_v128_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slopez_21d_z126_3d_v129_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slopez_63d_z252_3d_v130_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slopez_126d_z252_3d_v131_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slopez_252d_z504_3d_v132_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slopez_21d_z126_3d_v133_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slopez_63d_z252_3d_v134_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slopez_126d_z252_3d_v135_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slopez_252d_z504_3d_v136_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slopez_21d_z126_3d_v137_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slopez_63d_z252_3d_v138_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slopez_126d_z252_3d_v139_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slopez_252d_z504_3d_v140_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slopez_21d_z126_3d_v141_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slopez_63d_z252_3d_v142_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slopez_126d_z252_3d_v143_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slopez_252d_z504_3d_v144_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slopez_21d_z126_3d_v145_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slopez_63d_z252_3d_v146_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slopez_126d_z252_3d_v147_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slopez_252d_z504_3d_v148_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slopez_21d_z126_3d_v149_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slopez_63d_z252_3d_v150_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slopez_126d_z252_3d_v151_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slopez_252d_z504_3d_v152_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slopez_21d_z126_3d_v153_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slopez_63d_z252_3d_v154_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slopez_126d_z252_3d_v155_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slopez_252d_z504_3d_v156_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slopez_21d_z126_3d_v157_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slopez_63d_z252_3d_v158_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slopez_126d_z252_3d_v159_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slopez_252d_z504_3d_v160_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slopez_21d_z126_3d_v161_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slopez_63d_z252_3d_v162_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slopez_126d_z252_3d_v163_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slopez_252d_z504_3d_v164_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slopez_21d_z126_3d_v165_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slopez_63d_z252_3d_v166_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slopez_126d_z252_3d_v167_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slopez_252d_z504_3d_v168_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slopez_21d_z126_3d_v169_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slopez_63d_z252_3d_v170_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slopez_126d_z252_3d_v171_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slopez_252d_z504_3d_v172_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slopez_21d_z126_3d_v173_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slopez_63d_z252_3d_v174_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slopez_126d_z252_3d_v175_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slopez_252d_z504_3d_v176_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_jerk_21d_3d_v177_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_jerk_63d_3d_v178_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_jerk_126d_3d_v179_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_jerk_21d_3d_v180_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_jerk_63d_3d_v181_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_jerk_126d_3d_v182_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_jerk_21d_3d_v183_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_jerk_63d_3d_v184_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_jerk_126d_3d_v185_signal(director_buy_value, closeadj):
    base = director_buy_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_jerk_21d_3d_v186_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_jerk_63d_3d_v187_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_jerk_126d_3d_v188_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_jerk_21d_3d_v189_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_jerk_63d_3d_v190_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_jerk_126d_3d_v191_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_jerk_21d_3d_v192_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_jerk_63d_3d_v193_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_jerk_126d_3d_v194_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_jerk_21d_3d_v195_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_jerk_63d_3d_v196_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_jerk_126d_3d_v197_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_jerk_21d_3d_v198_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_jerk_63d_3d_v199_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_jerk_126d_3d_v200_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

