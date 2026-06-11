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


# 21d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slope_21d_2d_v001_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slope_63d_2d_v002_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slope_126d_2d_v003_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slope_252d_2d_v004_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_slope_504d_2d_v005_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slope_21d_2d_v006_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slope_63d_2d_v007_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slope_126d_2d_v008_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slope_252d_2d_v009_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_slope_504d_2d_v010_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slope_21d_2d_v011_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slope_63d_2d_v012_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slope_126d_2d_v013_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slope_252d_2d_v014_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_slope_504d_2d_v015_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slope_21d_2d_v016_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slope_63d_2d_v017_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slope_126d_2d_v018_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slope_252d_2d_v019_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_slope_504d_2d_v020_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slope_21d_2d_v021_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slope_63d_2d_v022_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slope_126d_2d_v023_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slope_252d_2d_v024_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_slope_504d_2d_v025_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slope_21d_2d_v026_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slope_63d_2d_v027_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slope_126d_2d_v028_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slope_252d_2d_v029_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_slope_504d_2d_v030_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slope_21d_2d_v031_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slope_63d_2d_v032_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slope_126d_2d_v033_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slope_252d_2d_v034_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_slope_504d_2d_v035_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slope_21d_2d_v036_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slope_63d_2d_v037_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slope_126d_2d_v038_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slope_252d_2d_v039_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_slope_504d_2d_v040_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slope_21d_2d_v041_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slope_63d_2d_v042_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slope_126d_2d_v043_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slope_252d_2d_v044_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_slope_504d_2d_v045_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slope_21d_2d_v046_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slope_63d_2d_v047_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slope_126d_2d_v048_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slope_252d_2d_v049_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_slope_504d_2d_v050_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slope_21d_2d_v051_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slope_63d_2d_v052_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slope_126d_2d_v053_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slope_252d_2d_v054_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_slope_504d_2d_v055_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slope_21d_2d_v056_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slope_63d_2d_v057_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slope_126d_2d_v058_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slope_252d_2d_v059_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_slope_504d_2d_v060_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slope_21d_2d_v061_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slope_63d_2d_v062_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slope_126d_2d_v063_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slope_252d_2d_v064_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_slope_504d_2d_v065_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slope_21d_2d_v066_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slope_63d_2d_v067_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slope_126d_2d_v068_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slope_252d_2d_v069_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_slope_504d_2d_v070_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slope_21d_2d_v071_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slope_63d_2d_v072_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slope_126d_2d_v073_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slope_252d_2d_v074_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_slope_504d_2d_v075_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slope_21d_2d_v076_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slope_63d_2d_v077_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slope_126d_2d_v078_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slope_252d_2d_v079_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_slope_504d_2d_v080_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slope_21d_2d_v081_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slope_63d_2d_v082_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slope_126d_2d_v083_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slope_252d_2d_v084_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_slope_504d_2d_v085_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slope_21d_2d_v086_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slope_63d_2d_v087_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slope_126d_2d_v088_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slope_252d_2d_v089_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_slope_504d_2d_v090_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slope_21d_2d_v091_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slope_63d_2d_v092_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slope_126d_2d_v093_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slope_252d_2d_v094_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_slope_504d_2d_v095_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slope_21d_2d_v096_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slope_63d_2d_v097_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slope_126d_2d_v098_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slope_252d_2d_v099_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_slope_504d_2d_v100_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slope_21d_2d_v101_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slope_63d_2d_v102_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slope_126d_2d_v103_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slope_252d_2d_v104_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_slope_504d_2d_v105_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slope_21d_2d_v106_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slope_63d_2d_v107_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slope_126d_2d_v108_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slope_252d_2d_v109_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_slope_504d_2d_v110_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_sm21_sl21_2d_v111_signal(unique_insider_count, closeadj):
    base = _mean(unique_insider_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_sm63_sl21_2d_v112_signal(unique_insider_count, closeadj):
    base = _mean(unique_insider_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_sm63_sl63_2d_v113_signal(unique_insider_count, closeadj):
    base = _mean(unique_insider_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_sm252_sl63_2d_v114_signal(unique_insider_count, closeadj):
    base = _mean(unique_insider_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_sm252_sl126_2d_v115_signal(unique_insider_count, closeadj):
    base = _mean(unique_insider_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_sm21_sl21_2d_v116_signal(officer_buy_value, closeadj):
    base = _mean(officer_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_sm63_sl21_2d_v117_signal(officer_buy_value, closeadj):
    base = _mean(officer_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_sm63_sl63_2d_v118_signal(officer_buy_value, closeadj):
    base = _mean(officer_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_sm252_sl63_2d_v119_signal(officer_buy_value, closeadj):
    base = _mean(officer_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_sm252_sl126_2d_v120_signal(officer_buy_value, closeadj):
    base = _mean(officer_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_sm21_sl21_2d_v121_signal(director_buy_value, closeadj):
    base = _mean(director_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_sm63_sl21_2d_v122_signal(director_buy_value, closeadj):
    base = _mean(director_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_sm63_sl63_2d_v123_signal(director_buy_value, closeadj):
    base = _mean(director_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_sm252_sl63_2d_v124_signal(director_buy_value, closeadj):
    base = _mean(director_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_sm252_sl126_2d_v125_signal(director_buy_value, closeadj):
    base = _mean(director_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_sm21_sl21_2d_v126_signal(ten_pct_owner_buy_value, closeadj):
    base = _mean(ten_pct_owner_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_sm63_sl21_2d_v127_signal(ten_pct_owner_buy_value, closeadj):
    base = _mean(ten_pct_owner_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_sm63_sl63_2d_v128_signal(ten_pct_owner_buy_value, closeadj):
    base = _mean(ten_pct_owner_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_sm252_sl63_2d_v129_signal(ten_pct_owner_buy_value, closeadj):
    base = _mean(ten_pct_owner_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_sm252_sl126_2d_v130_signal(ten_pct_owner_buy_value, closeadj):
    base = _mean(ten_pct_owner_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_sm21_sl21_2d_v131_signal(unique_insider_count, officer_buy_value, closeadj):
    base = _mean(unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_sm63_sl21_2d_v132_signal(unique_insider_count, officer_buy_value, closeadj):
    base = _mean(unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_sm63_sl63_2d_v133_signal(unique_insider_count, officer_buy_value, closeadj):
    base = _mean(unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_sm252_sl63_2d_v134_signal(unique_insider_count, officer_buy_value, closeadj):
    base = _mean(unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_sm252_sl126_2d_v135_signal(unique_insider_count, officer_buy_value, closeadj):
    base = _mean(unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_sm21_sl21_2d_v136_signal(officer_buy_value, director_buy_value, closeadj):
    base = _mean(officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_sm63_sl21_2d_v137_signal(officer_buy_value, director_buy_value, closeadj):
    base = _mean(officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_sm63_sl63_2d_v138_signal(officer_buy_value, director_buy_value, closeadj):
    base = _mean(officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_sm252_sl63_2d_v139_signal(officer_buy_value, director_buy_value, closeadj):
    base = _mean(officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_sm252_sl126_2d_v140_signal(officer_buy_value, director_buy_value, closeadj):
    base = _mean(officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_sm21_sl21_2d_v141_signal(unique_insider_count, closeadj):
    base = _mean((unique_insider_count > 3).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_sm63_sl21_2d_v142_signal(unique_insider_count, closeadj):
    base = _mean((unique_insider_count > 3).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_sm63_sl63_2d_v143_signal(unique_insider_count, closeadj):
    base = _mean((unique_insider_count > 3).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_sm252_sl63_2d_v144_signal(unique_insider_count, closeadj):
    base = _mean((unique_insider_count > 3).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_sm252_sl126_2d_v145_signal(unique_insider_count, closeadj):
    base = _mean((unique_insider_count > 3).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_sm21_sl21_2d_v146_signal(unique_p_insider_count, closeadj):
    base = _mean(unique_p_insider_count.rolling(30, min_periods=1).max(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_sm63_sl21_2d_v147_signal(unique_p_insider_count, closeadj):
    base = _mean(unique_p_insider_count.rolling(30, min_periods=1).max(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_sm63_sl63_2d_v148_signal(unique_p_insider_count, closeadj):
    base = _mean(unique_p_insider_count.rolling(30, min_periods=1).max(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_sm252_sl63_2d_v149_signal(unique_p_insider_count, closeadj):
    base = _mean(unique_p_insider_count.rolling(30, min_periods=1).max(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_sm252_sl126_2d_v150_signal(unique_p_insider_count, closeadj):
    base = _mean(unique_p_insider_count.rolling(30, min_periods=1).max(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_sm21_sl21_2d_v151_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_sm63_sl21_2d_v152_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_sm63_sl63_2d_v153_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_sm252_sl63_2d_v154_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_sm252_sl126_2d_v155_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_sm21_sl21_2d_v156_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_sm63_sl21_2d_v157_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_sm63_sl63_2d_v158_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_sm252_sl63_2d_v159_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_sm252_sl126_2d_v160_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_sm21_sl21_2d_v161_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_sm63_sl21_2d_v162_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_sm63_sl63_2d_v163_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_sm252_sl63_2d_v164_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_sm252_sl126_2d_v165_signal(unique_p_insider_count, closeadj):
    base = _mean((unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_sm21_sl21_2d_v166_signal(ceo_buy_value, closeadj):
    base = _mean(ceo_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_sm63_sl21_2d_v167_signal(ceo_buy_value, closeadj):
    base = _mean(ceo_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_sm63_sl63_2d_v168_signal(ceo_buy_value, closeadj):
    base = _mean(ceo_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_sm252_sl63_2d_v169_signal(ceo_buy_value, closeadj):
    base = _mean(ceo_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_sm252_sl126_2d_v170_signal(ceo_buy_value, closeadj):
    base = _mean(ceo_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_sm21_sl21_2d_v171_signal(cfo_buy_value, closeadj):
    base = _mean(cfo_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_sm63_sl21_2d_v172_signal(cfo_buy_value, closeadj):
    base = _mean(cfo_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_sm63_sl63_2d_v173_signal(cfo_buy_value, closeadj):
    base = _mean(cfo_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_sm252_sl63_2d_v174_signal(cfo_buy_value, closeadj):
    base = _mean(cfo_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_sm252_sl126_2d_v175_signal(cfo_buy_value, closeadj):
    base = _mean(cfo_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_sm21_sl21_2d_v176_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = _mean(ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_sm63_sl21_2d_v177_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = _mean(ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_sm63_sl63_2d_v178_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = _mean(ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_sm252_sl63_2d_v179_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = _mean(ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_sm252_sl126_2d_v180_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = _mean(ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_sm21_sl21_2d_v181_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = _mean((ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_sm63_sl21_2d_v182_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = _mean((ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_sm63_sl63_2d_v183_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = _mean((ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_sm252_sl63_2d_v184_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = _mean((ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_sm252_sl126_2d_v185_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = _mean((ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_sm21_sl21_2d_v186_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = _mean((ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_sm63_sl21_2d_v187_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = _mean((ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_sm63_sl63_2d_v188_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = _mean((ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_sm252_sl63_2d_v189_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = _mean((ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_sm252_sl126_2d_v190_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = _mean((ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_sm21_sl21_2d_v191_signal(founder_buy_value, closeadj):
    base = _mean(founder_buy_value, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_sm63_sl21_2d_v192_signal(founder_buy_value, closeadj):
    base = _mean(founder_buy_value, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_sm63_sl63_2d_v193_signal(founder_buy_value, closeadj):
    base = _mean(founder_buy_value, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_sm252_sl63_2d_v194_signal(founder_buy_value, closeadj):
    base = _mean(founder_buy_value, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_sm252_sl126_2d_v195_signal(founder_buy_value, closeadj):
    base = _mean(founder_buy_value, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_sm21_sl21_2d_v196_signal(founder_owned_shares, sharesbas, closeadj):
    base = _mean(founder_owned_shares / sharesbas.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_sm63_sl21_2d_v197_signal(founder_owned_shares, sharesbas, closeadj):
    base = _mean(founder_owned_shares / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_sm63_sl63_2d_v198_signal(founder_owned_shares, sharesbas, closeadj):
    base = _mean(founder_owned_shares / sharesbas.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_sm252_sl63_2d_v199_signal(founder_owned_shares, sharesbas, closeadj):
    base = _mean(founder_owned_shares / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_sm252_sl126_2d_v200_signal(founder_owned_shares, sharesbas, closeadj):
    base = _mean(founder_owned_shares / sharesbas.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

