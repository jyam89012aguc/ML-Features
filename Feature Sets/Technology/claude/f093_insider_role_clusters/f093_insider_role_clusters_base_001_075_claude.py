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
def _f093_unique_count(unique_insider_count):
    return unique_insider_count


# 21d mean of unique_insider_cnt scaled by closeadj
def f093irc_f093_insider_role_clusters_unique_insider_cnt_mean_21d_base_v001_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of unique_insider_cnt scaled by closeadj
def f093irc_f093_insider_role_clusters_unique_insider_cnt_mean_63d_base_v002_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of unique_insider_cnt scaled by closeadj
def f093irc_f093_insider_role_clusters_unique_insider_cnt_mean_126d_base_v003_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of unique_insider_cnt scaled by closeadj
def f093irc_f093_insider_role_clusters_unique_insider_cnt_mean_252d_base_v004_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of unique_insider_cnt scaled by closeadj
def f093irc_f093_insider_role_clusters_unique_insider_cnt_mean_504d_base_v005_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of officer_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_buy_value_mean_21d_base_v006_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of officer_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_buy_value_mean_63d_base_v007_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of officer_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_buy_value_mean_126d_base_v008_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of officer_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_buy_value_mean_252d_base_v009_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of officer_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_buy_value_mean_504d_base_v010_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of director_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_director_buy_value_mean_21d_base_v011_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of director_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_director_buy_value_mean_63d_base_v012_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of director_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_director_buy_value_mean_126d_base_v013_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of director_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_director_buy_value_mean_252d_base_v014_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of director_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_director_buy_value_mean_504d_base_v015_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ten_pct_owner_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_mean_21d_base_v016_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ten_pct_owner_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_mean_63d_base_v017_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ten_pct_owner_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_mean_126d_base_v018_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ten_pct_owner_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_mean_252d_base_v019_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ten_pct_owner_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_mean_504d_base_v020_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of cluster_score scaled by closeadj
def f093irc_f093_insider_role_clusters_cluster_score_mean_21d_base_v021_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of cluster_score scaled by closeadj
def f093irc_f093_insider_role_clusters_cluster_score_mean_63d_base_v022_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of cluster_score scaled by closeadj
def f093irc_f093_insider_role_clusters_cluster_score_mean_126d_base_v023_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of cluster_score scaled by closeadj
def f093irc_f093_insider_role_clusters_cluster_score_mean_252d_base_v024_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of cluster_score scaled by closeadj
def f093irc_f093_insider_role_clusters_cluster_score_mean_504d_base_v025_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of officer_share_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_share_buy_mean_21d_base_v026_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of officer_share_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_share_buy_mean_63d_base_v027_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of officer_share_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_share_buy_mean_126d_base_v028_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of officer_share_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_share_buy_mean_252d_base_v029_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of officer_share_buy scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_share_buy_mean_504d_base_v030_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of insider_buy_breadth scaled by closeadj
def f093irc_f093_insider_role_clusters_insider_buy_breadth_mean_21d_base_v031_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of insider_buy_breadth scaled by closeadj
def f093irc_f093_insider_role_clusters_insider_buy_breadth_mean_63d_base_v032_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of insider_buy_breadth scaled by closeadj
def f093irc_f093_insider_role_clusters_insider_buy_breadth_mean_126d_base_v033_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of insider_buy_breadth scaled by closeadj
def f093irc_f093_insider_role_clusters_insider_buy_breadth_mean_252d_base_v034_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of insider_buy_breadth scaled by closeadj
def f093irc_f093_insider_role_clusters_insider_buy_breadth_mean_504d_base_v035_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_cluster_30d_count scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_mean_21d_base_v036_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_cluster_30d_count scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_mean_63d_base_v037_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_cluster_30d_count scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_mean_126d_base_v038_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_cluster_30d_count scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_mean_252d_base_v039_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_cluster_30d_count scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_mean_504d_base_v040_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_cluster_30d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_mean_21d_base_v041_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_cluster_30d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_mean_63d_base_v042_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_cluster_30d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_mean_126d_base_v043_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_cluster_30d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_mean_252d_base_v044_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_cluster_30d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_mean_504d_base_v045_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_cluster_90d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_mean_21d_base_v046_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_cluster_90d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_mean_63d_base_v047_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_cluster_90d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_mean_126d_base_v048_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_cluster_90d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_mean_252d_base_v049_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_cluster_90d_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_mean_504d_base_v050_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of p_cluster_strong_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_mean_21d_base_v051_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of p_cluster_strong_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_mean_63d_base_v052_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of p_cluster_strong_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_mean_126d_base_v053_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of p_cluster_strong_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_mean_252d_base_v054_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of p_cluster_strong_flag scaled by closeadj
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_mean_504d_base_v055_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ceo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_buy_value_mean_21d_base_v056_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ceo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_buy_value_mean_63d_base_v057_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ceo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_buy_value_mean_126d_base_v058_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ceo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_buy_value_mean_252d_base_v059_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ceo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_buy_value_mean_504d_base_v060_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of cfo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_cfo_buy_value_mean_21d_base_v061_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of cfo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_cfo_buy_value_mean_63d_base_v062_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of cfo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_cfo_buy_value_mean_126d_base_v063_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of cfo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_cfo_buy_value_mean_252d_base_v064_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of cfo_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_cfo_buy_value_mean_504d_base_v065_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ceo_cfo_buy_lvl scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_mean_21d_base_v066_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ceo_cfo_buy_lvl scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_mean_63d_base_v067_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ceo_cfo_buy_lvl scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_mean_126d_base_v068_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ceo_cfo_buy_lvl scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_mean_252d_base_v069_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ceo_cfo_buy_lvl scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_mean_504d_base_v070_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ceo_cfo_buy_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_mean_21d_base_v071_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ceo_cfo_buy_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_mean_63d_base_v072_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ceo_cfo_buy_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_mean_126d_base_v073_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ceo_cfo_buy_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_mean_252d_base_v074_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ceo_cfo_buy_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_mean_504d_base_v075_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ceo_cfo_sell_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_mean_21d_base_v076_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ceo_cfo_sell_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_mean_63d_base_v077_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ceo_cfo_sell_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_mean_126d_base_v078_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ceo_cfo_sell_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_mean_252d_base_v079_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ceo_cfo_sell_to_mcap scaled by closeadj
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_mean_504d_base_v080_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of founder_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_buy_value_mean_21d_base_v081_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of founder_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_buy_value_mean_63d_base_v082_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of founder_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_buy_value_mean_126d_base_v083_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of founder_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_buy_value_mean_252d_base_v084_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of founder_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_buy_value_mean_504d_base_v085_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of founder_ownership_pct scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_ownership_pct_mean_21d_base_v086_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of founder_ownership_pct scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_ownership_pct_mean_63d_base_v087_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of founder_ownership_pct scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_ownership_pct_mean_126d_base_v088_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of founder_ownership_pct scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_ownership_pct_mean_252d_base_v089_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of founder_ownership_pct scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_ownership_pct_mean_504d_base_v090_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of founder_net_chg_30d scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_mean_21d_base_v091_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of founder_net_chg_30d scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_mean_63d_base_v092_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of founder_net_chg_30d scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_mean_126d_base_v093_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of founder_net_chg_30d scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_mean_252d_base_v094_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of founder_net_chg_30d scaled by closeadj
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_mean_504d_base_v095_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of officer_p_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_p_buy_value_mean_21d_base_v096_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of officer_p_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_p_buy_value_mean_63d_base_v097_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of officer_p_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_p_buy_value_mean_126d_base_v098_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of officer_p_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_p_buy_value_mean_252d_base_v099_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of officer_p_buy_value scaled by closeadj
def f093irc_f093_insider_role_clusters_officer_p_buy_value_mean_504d_base_v100_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

