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
def _f096_topshare(top_holder_value, inst_total_value):
    return top_holder_value / inst_total_value.replace(0, np.nan).abs()


# 63d z-score of top_share
def f096hcn_f096_holder_concentration_top_share_z_63d_base_v076_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top_share
def f096hcn_f096_holder_concentration_top_share_z_126d_base_v077_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top_share
def f096hcn_f096_holder_concentration_top_share_z_252d_base_v078_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top_share
def f096hcn_f096_holder_concentration_top_share_z_504d_base_v079_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of hhi
def f096hcn_f096_holder_concentration_hhi_z_63d_base_v080_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of hhi
def f096hcn_f096_holder_concentration_hhi_z_126d_base_v081_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of hhi
def f096hcn_f096_holder_concentration_hhi_z_252d_base_v082_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of hhi
def f096hcn_f096_holder_concentration_hhi_z_504d_base_v083_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_z_63d_base_v084_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_z_126d_base_v085_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_z_252d_base_v086_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_z_504d_base_v087_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_z_63d_base_v088_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_z_126d_base_v089_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_z_252d_base_v090_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_z_504d_base_v091_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_z_63d_base_v092_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_z_126d_base_v093_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_z_252d_base_v094_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_z_504d_base_v095_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top5_share
def f096hcn_f096_holder_concentration_top5_share_z_63d_base_v096_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top5_share
def f096hcn_f096_holder_concentration_top5_share_z_126d_base_v097_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top5_share
def f096hcn_f096_holder_concentration_top5_share_z_252d_base_v098_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top5_share
def f096hcn_f096_holder_concentration_top5_share_z_504d_base_v099_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_z_63d_base_v100_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_z_126d_base_v101_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_z_252d_base_v102_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_z_504d_base_v103_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_z_63d_base_v104_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_z_126d_base_v105_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_z_252d_base_v106_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_z_504d_base_v107_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_z_63d_base_v108_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_z_126d_base_v109_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_z_252d_base_v110_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_z_504d_base_v111_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_z_63d_base_v112_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_z_126d_base_v113_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_z_252d_base_v114_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_z_504d_base_v115_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_z_63d_base_v116_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_z_126d_base_v117_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_z_252d_base_v118_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_z_504d_base_v119_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_z_63d_base_v120_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_z_126d_base_v121_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_z_252d_base_v122_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_z_504d_base_v123_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_z_63d_base_v124_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_z_126d_base_v125_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_z_252d_base_v126_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_z_504d_base_v127_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_z_63d_base_v128_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_z_126d_base_v129_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_z_252d_base_v130_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_z_504d_base_v131_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_z_63d_base_v132_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_z_126d_base_v133_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_z_252d_base_v134_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_z_504d_base_v135_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_z_63d_base_v136_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_z_126d_base_v137_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_z_252d_base_v138_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_z_504d_base_v139_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_z_63d_base_v140_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_z_126d_base_v141_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_z_252d_base_v142_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_z_504d_base_v143_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_z_63d_base_v144_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_z_126d_base_v145_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_z_252d_base_v146_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_z_504d_base_v147_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of top_share
def f096hcn_f096_holder_concentration_top_share_distmax_252d_base_v148_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of top_share
def f096hcn_f096_holder_concentration_top_share_distmax_504d_base_v149_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of hhi
def f096hcn_f096_holder_concentration_hhi_distmax_252d_base_v150_signal(holder_hhi, closeadj):
    base = holder_hhi
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of hhi
def f096hcn_f096_holder_concentration_hhi_distmax_504d_base_v151_signal(holder_hhi, closeadj):
    base = holder_hhi
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_distmax_252d_base_v152_signal(new_holder_count, closeadj):
    base = new_holder_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_distmax_504d_base_v153_signal(new_holder_count, closeadj):
    base = new_holder_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_distmax_252d_base_v154_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_distmax_504d_base_v155_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_distmax_252d_base_v156_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_distmax_504d_base_v157_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of top5_share
def f096hcn_f096_holder_concentration_top5_share_distmax_252d_base_v158_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of top5_share
def f096hcn_f096_holder_concentration_top5_share_distmax_504d_base_v159_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_distmax_252d_base_v160_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_distmax_504d_base_v161_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_distmax_252d_base_v162_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_distmax_504d_base_v163_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_distmax_252d_base_v164_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_distmax_504d_base_v165_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_distmax_252d_base_v166_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_distmax_504d_base_v167_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_distmax_252d_base_v168_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_distmax_504d_base_v169_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_distmax_252d_base_v170_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_distmax_504d_base_v171_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_distmax_252d_base_v172_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_distmax_504d_base_v173_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_distmax_252d_base_v174_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_distmax_504d_base_v175_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

