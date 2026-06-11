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


# 63d z-score of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_z_63d_base_v076_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_z_126d_base_v077_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_z_252d_base_v078_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_z_504d_base_v079_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_z_63d_base_v080_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_z_126d_base_v081_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_z_252d_base_v082_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_z_504d_base_v083_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_z_63d_base_v084_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_z_126d_base_v085_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_z_252d_base_v086_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_z_504d_base_v087_signal(director_buy_value, closeadj):
    base = director_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_z_63d_base_v088_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_z_126d_base_v089_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_z_252d_base_v090_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_z_504d_base_v091_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_z_63d_base_v092_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_z_126d_base_v093_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_z_252d_base_v094_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_z_504d_base_v095_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_z_63d_base_v096_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_z_126d_base_v097_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_z_252d_base_v098_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_z_504d_base_v099_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_z_63d_base_v100_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_z_126d_base_v101_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_z_252d_base_v102_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of insider_buy_breadth
def f093irc_f093_insider_role_clusters_insider_buy_breadth_z_504d_base_v103_signal(unique_insider_count, closeadj):
    base = (unique_insider_count > 3).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_z_63d_base_v104_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_z_126d_base_v105_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_z_252d_base_v106_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_cluster_30d_count
def f093irc_f093_insider_role_clusters_p_cluster_30d_count_z_504d_base_v107_signal(unique_p_insider_count, closeadj):
    base = unique_p_insider_count.rolling(30, min_periods=1).max()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_z_63d_base_v108_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_z_126d_base_v109_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_z_252d_base_v110_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_cluster_30d_flag
def f093irc_f093_insider_role_clusters_p_cluster_30d_flag_z_504d_base_v111_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_z_63d_base_v112_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_z_126d_base_v113_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_z_252d_base_v114_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_cluster_90d_flag
def f093irc_f093_insider_role_clusters_p_cluster_90d_flag_z_504d_base_v115_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(90, min_periods=1).max() >= 3).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_z_63d_base_v116_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_z_126d_base_v117_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_z_252d_base_v118_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of p_cluster_strong_flag
def f093irc_f093_insider_role_clusters_p_cluster_strong_flag_z_504d_base_v119_signal(unique_p_insider_count, closeadj):
    base = (unique_p_insider_count.rolling(30, min_periods=1).max() >= 5).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_z_63d_base_v120_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_z_126d_base_v121_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_z_252d_base_v122_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ceo_buy_value
def f093irc_f093_insider_role_clusters_ceo_buy_value_z_504d_base_v123_signal(ceo_buy_value, closeadj):
    base = ceo_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_z_63d_base_v124_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_z_126d_base_v125_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_z_252d_base_v126_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of cfo_buy_value
def f093irc_f093_insider_role_clusters_cfo_buy_value_z_504d_base_v127_signal(cfo_buy_value, closeadj):
    base = cfo_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_z_63d_base_v128_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_z_126d_base_v129_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_z_252d_base_v130_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ceo_cfo_buy_lvl
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_lvl_z_504d_base_v131_signal(ceo_buy_value, cfo_buy_value, closeadj):
    base = ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_z_63d_base_v132_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_z_126d_base_v133_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_z_252d_base_v134_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ceo_cfo_buy_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_buy_to_mcap_z_504d_base_v135_signal(ceo_buy_value, cfo_buy_value, marketcap, closeadj):
    base = (ceo_buy_value.fillna(0) + cfo_buy_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_z_63d_base_v136_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_z_126d_base_v137_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_z_252d_base_v138_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ceo_cfo_sell_to_mcap
def f093irc_f093_insider_role_clusters_ceo_cfo_sell_to_mcap_z_504d_base_v139_signal(ceo_sell_value, cfo_sell_value, marketcap, closeadj):
    base = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)) / marketcap.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_z_63d_base_v140_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_z_126d_base_v141_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_z_252d_base_v142_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of founder_buy_value
def f093irc_f093_insider_role_clusters_founder_buy_value_z_504d_base_v143_signal(founder_buy_value, closeadj):
    base = founder_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_z_63d_base_v144_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_z_126d_base_v145_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_z_252d_base_v146_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of founder_ownership_pct
def f093irc_f093_insider_role_clusters_founder_ownership_pct_z_504d_base_v147_signal(founder_owned_shares, sharesbas, closeadj):
    base = founder_owned_shares / sharesbas.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_z_63d_base_v148_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_z_126d_base_v149_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_z_252d_base_v150_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of founder_net_chg_30d
def f093irc_f093_insider_role_clusters_founder_net_chg_30d_z_504d_base_v151_signal(founder_buy_value, founder_sell_value, closeadj):
    base = (founder_buy_value.fillna(0) - founder_sell_value.fillna(0)).rolling(30, min_periods=1).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_z_63d_base_v152_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_z_126d_base_v153_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_z_252d_base_v154_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of officer_p_buy_value
def f093irc_f093_insider_role_clusters_officer_p_buy_value_z_504d_base_v155_signal(officer_p_buy_value, closeadj):
    base = officer_p_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_z_63d_base_v156_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_z_126d_base_v157_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_z_252d_base_v158_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of director_p_buy_value
def f093irc_f093_insider_role_clusters_director_p_buy_value_z_504d_base_v159_signal(director_p_buy_value, closeadj):
    base = director_p_buy_value
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_z_63d_base_v160_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_z_126d_base_v161_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_z_252d_base_v162_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of officer_p_share
def f093irc_f093_insider_role_clusters_officer_p_share_z_504d_base_v163_signal(officer_p_buy_value, director_p_buy_value, closeadj):
    base = officer_p_buy_value / (officer_p_buy_value + director_p_buy_value).replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_distmax_252d_base_v164_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of unique_insider_cnt
def f093irc_f093_insider_role_clusters_unique_insider_cnt_distmax_504d_base_v165_signal(unique_insider_count, closeadj):
    base = unique_insider_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_distmax_252d_base_v166_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of officer_buy_value
def f093irc_f093_insider_role_clusters_officer_buy_value_distmax_504d_base_v167_signal(officer_buy_value, closeadj):
    base = officer_buy_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_distmax_252d_base_v168_signal(director_buy_value, closeadj):
    base = director_buy_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of director_buy_value
def f093irc_f093_insider_role_clusters_director_buy_value_distmax_504d_base_v169_signal(director_buy_value, closeadj):
    base = director_buy_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_distmax_252d_base_v170_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ten_pct_owner_buy
def f093irc_f093_insider_role_clusters_ten_pct_owner_buy_distmax_504d_base_v171_signal(ten_pct_owner_buy_value, closeadj):
    base = ten_pct_owner_buy_value
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_distmax_252d_base_v172_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of cluster_score
def f093irc_f093_insider_role_clusters_cluster_score_distmax_504d_base_v173_signal(unique_insider_count, officer_buy_value, closeadj):
    base = unique_insider_count * officer_buy_value / officer_buy_value.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_distmax_252d_base_v174_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of officer_share_buy
def f093irc_f093_insider_role_clusters_officer_share_buy_distmax_504d_base_v175_signal(officer_buy_value, director_buy_value, closeadj):
    base = officer_buy_value / (officer_buy_value + director_buy_value).replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

