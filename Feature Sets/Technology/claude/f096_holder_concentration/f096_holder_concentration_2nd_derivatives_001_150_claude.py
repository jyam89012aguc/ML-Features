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
def _f096_topshare(top_holder_value, inst_total_value):
    return top_holder_value / inst_total_value.replace(0, np.nan).abs()


# 21d slope of top_share
def f096hcn_f096_holder_concentration_top_share_slope_21d_2d_v001_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top_share
def f096hcn_f096_holder_concentration_top_share_slope_63d_2d_v002_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top_share
def f096hcn_f096_holder_concentration_top_share_slope_126d_2d_v003_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top_share
def f096hcn_f096_holder_concentration_top_share_slope_252d_2d_v004_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top_share
def f096hcn_f096_holder_concentration_top_share_slope_504d_2d_v005_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of hhi
def f096hcn_f096_holder_concentration_hhi_slope_21d_2d_v006_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of hhi
def f096hcn_f096_holder_concentration_hhi_slope_63d_2d_v007_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of hhi
def f096hcn_f096_holder_concentration_hhi_slope_126d_2d_v008_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of hhi
def f096hcn_f096_holder_concentration_hhi_slope_252d_2d_v009_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of hhi
def f096hcn_f096_holder_concentration_hhi_slope_504d_2d_v010_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slope_21d_2d_v011_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slope_63d_2d_v012_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slope_126d_2d_v013_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slope_252d_2d_v014_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slope_504d_2d_v015_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slope_21d_2d_v016_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slope_63d_2d_v017_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slope_126d_2d_v018_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slope_252d_2d_v019_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slope_504d_2d_v020_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slope_21d_2d_v021_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slope_63d_2d_v022_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slope_126d_2d_v023_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slope_252d_2d_v024_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slope_504d_2d_v025_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_slope_21d_2d_v026_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_slope_63d_2d_v027_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_slope_126d_2d_v028_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_slope_252d_2d_v029_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_slope_504d_2d_v030_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slope_21d_2d_v031_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slope_63d_2d_v032_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slope_126d_2d_v033_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slope_252d_2d_v034_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slope_504d_2d_v035_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slope_21d_2d_v036_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slope_63d_2d_v037_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slope_126d_2d_v038_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slope_252d_2d_v039_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slope_504d_2d_v040_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slope_21d_2d_v041_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slope_63d_2d_v042_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slope_126d_2d_v043_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slope_252d_2d_v044_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slope_504d_2d_v045_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slope_21d_2d_v046_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slope_63d_2d_v047_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slope_126d_2d_v048_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slope_252d_2d_v049_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slope_504d_2d_v050_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slope_21d_2d_v051_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slope_63d_2d_v052_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slope_126d_2d_v053_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slope_252d_2d_v054_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slope_504d_2d_v055_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slope_21d_2d_v056_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slope_63d_2d_v057_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slope_126d_2d_v058_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slope_252d_2d_v059_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slope_504d_2d_v060_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slope_21d_2d_v061_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slope_63d_2d_v062_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slope_126d_2d_v063_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slope_252d_2d_v064_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slope_504d_2d_v065_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slope_21d_2d_v066_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slope_63d_2d_v067_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slope_126d_2d_v068_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slope_252d_2d_v069_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slope_504d_2d_v070_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slope_21d_2d_v071_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slope_63d_2d_v072_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slope_126d_2d_v073_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slope_252d_2d_v074_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slope_504d_2d_v075_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slope_21d_2d_v076_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slope_63d_2d_v077_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slope_126d_2d_v078_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slope_252d_2d_v079_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slope_504d_2d_v080_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slope_21d_2d_v081_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slope_63d_2d_v082_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slope_126d_2d_v083_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slope_252d_2d_v084_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slope_504d_2d_v085_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slope_21d_2d_v086_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slope_63d_2d_v087_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slope_126d_2d_v088_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slope_252d_2d_v089_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slope_504d_2d_v090_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top_share
def f096hcn_f096_holder_concentration_top_share_sm21_sl21_2d_v091_signal(top_holder_value, inst_total_value, closeadj):
    base = _mean(_f096_topshare(top_holder_value, inst_total_value), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top_share
def f096hcn_f096_holder_concentration_top_share_sm63_sl21_2d_v092_signal(top_holder_value, inst_total_value, closeadj):
    base = _mean(_f096_topshare(top_holder_value, inst_total_value), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top_share
def f096hcn_f096_holder_concentration_top_share_sm63_sl63_2d_v093_signal(top_holder_value, inst_total_value, closeadj):
    base = _mean(_f096_topshare(top_holder_value, inst_total_value), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top_share
def f096hcn_f096_holder_concentration_top_share_sm252_sl63_2d_v094_signal(top_holder_value, inst_total_value, closeadj):
    base = _mean(_f096_topshare(top_holder_value, inst_total_value), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top_share
def f096hcn_f096_holder_concentration_top_share_sm252_sl126_2d_v095_signal(top_holder_value, inst_total_value, closeadj):
    base = _mean(_f096_topshare(top_holder_value, inst_total_value), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of hhi
def f096hcn_f096_holder_concentration_hhi_sm21_sl21_2d_v096_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of hhi
def f096hcn_f096_holder_concentration_hhi_sm63_sl21_2d_v097_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of hhi
def f096hcn_f096_holder_concentration_hhi_sm63_sl63_2d_v098_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of hhi
def f096hcn_f096_holder_concentration_hhi_sm252_sl63_2d_v099_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of hhi
def f096hcn_f096_holder_concentration_hhi_sm252_sl126_2d_v100_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_sm21_sl21_2d_v101_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_sm63_sl21_2d_v102_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_sm63_sl63_2d_v103_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_sm252_sl63_2d_v104_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_sm252_sl126_2d_v105_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_sm21_sl21_2d_v106_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_sm63_sl21_2d_v107_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_sm63_sl63_2d_v108_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_sm252_sl63_2d_v109_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_sm252_sl126_2d_v110_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_sm21_sl21_2d_v111_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean(new_holder_count - exited_holder_count, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_sm63_sl21_2d_v112_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean(new_holder_count - exited_holder_count, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_sm63_sl63_2d_v113_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean(new_holder_count - exited_holder_count, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_sm252_sl63_2d_v114_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean(new_holder_count - exited_holder_count, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_sm252_sl126_2d_v115_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean(new_holder_count - exited_holder_count, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_sm21_sl21_2d_v116_signal(top5_holder_value, inst_total_value, closeadj):
    base = _mean(top5_holder_value / inst_total_value.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_sm63_sl21_2d_v117_signal(top5_holder_value, inst_total_value, closeadj):
    base = _mean(top5_holder_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_sm63_sl63_2d_v118_signal(top5_holder_value, inst_total_value, closeadj):
    base = _mean(top5_holder_value / inst_total_value.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_sm252_sl63_2d_v119_signal(top5_holder_value, inst_total_value, closeadj):
    base = _mean(top5_holder_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_sm252_sl126_2d_v120_signal(top5_holder_value, inst_total_value, closeadj):
    base = _mean(top5_holder_value / inst_total_value.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_sm21_sl21_2d_v121_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_sm63_sl21_2d_v122_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_sm63_sl63_2d_v123_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_sm252_sl63_2d_v124_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_sm252_sl126_2d_v125_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_sm21_sl21_2d_v126_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_sm63_sl21_2d_v127_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_sm63_sl63_2d_v128_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_sm252_sl63_2d_v129_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_sm252_sl126_2d_v130_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_sm21_sl21_2d_v131_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_sm63_sl21_2d_v132_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_sm63_sl63_2d_v133_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_sm252_sl63_2d_v134_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_sm252_sl126_2d_v135_signal(top5_holder_value, closeadj):
    base = _mean(top5_holder_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_sm21_sl21_2d_v136_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_sm63_sl21_2d_v137_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_sm63_sl63_2d_v138_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_sm252_sl63_2d_v139_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_sm252_sl126_2d_v140_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_sm21_sl21_2d_v141_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.pct_change(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_sm63_sl21_2d_v142_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_sm63_sl63_2d_v143_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.pct_change(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_sm252_sl63_2d_v144_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_sm252_sl126_2d_v145_signal(top_holder_value, closeadj):
    base = _mean(top_holder_value.pct_change(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_sm21_sl21_2d_v146_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_sm63_sl21_2d_v147_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_sm63_sl63_2d_v148_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_sm252_sl63_2d_v149_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_sm252_sl126_2d_v150_signal(new_holder_count, closeadj):
    base = _mean(new_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_sm21_sl21_2d_v151_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_sm63_sl21_2d_v152_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_sm63_sl63_2d_v153_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_sm252_sl63_2d_v154_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_sm252_sl126_2d_v155_signal(exited_holder_count, closeadj):
    base = _mean(exited_holder_count.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_sm21_sl21_2d_v156_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean((new_holder_count - exited_holder_count).diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_sm63_sl21_2d_v157_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean((new_holder_count - exited_holder_count).diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_sm63_sl63_2d_v158_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean((new_holder_count - exited_holder_count).diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_sm252_sl63_2d_v159_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean((new_holder_count - exited_holder_count).diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_sm252_sl126_2d_v160_signal(new_holder_count, exited_holder_count, closeadj):
    base = _mean((new_holder_count - exited_holder_count).diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_sm21_sl21_2d_v161_signal(new_holder_count, closeadj):
    base = _mean((new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_sm63_sl21_2d_v162_signal(new_holder_count, closeadj):
    base = _mean((new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_sm63_sl63_2d_v163_signal(new_holder_count, closeadj):
    base = _mean((new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_sm252_sl63_2d_v164_signal(new_holder_count, closeadj):
    base = _mean((new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_sm252_sl126_2d_v165_signal(new_holder_count, closeadj):
    base = _mean((new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_sm21_sl21_2d_v166_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=63), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_sm63_sl21_2d_v167_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=63), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_sm63_sl63_2d_v168_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=63), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_sm252_sl63_2d_v169_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=63), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_sm252_sl126_2d_v170_signal(holder_hhi, closeadj):
    base = _mean(holder_hhi.diff(periods=63), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_sm21_sl21_2d_v171_signal(holder_hhi, closeadj):
    base = _mean((holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_sm63_sl21_2d_v172_signal(holder_hhi, closeadj):
    base = _mean((holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_sm63_sl63_2d_v173_signal(holder_hhi, closeadj):
    base = _mean((holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_sm252_sl63_2d_v174_signal(holder_hhi, closeadj):
    base = _mean((holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_sm252_sl126_2d_v175_signal(holder_hhi, closeadj):
    base = _mean((holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_sm21_sl21_2d_v176_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = _mean((top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_sm63_sl21_2d_v177_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = _mean((top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_sm63_sl63_2d_v178_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = _mean((top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_sm252_sl63_2d_v179_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = _mean((top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_sm252_sl126_2d_v180_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = _mean((top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of top_share
def f096hcn_f096_holder_concentration_top_share_pctslope_21d_2d_v181_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of top_share
def f096hcn_f096_holder_concentration_top_share_pctslope_63d_2d_v182_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of top_share
def f096hcn_f096_holder_concentration_top_share_pctslope_252d_2d_v183_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of hhi
def f096hcn_f096_holder_concentration_hhi_pctslope_21d_2d_v184_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of hhi
def f096hcn_f096_holder_concentration_hhi_pctslope_63d_2d_v185_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of hhi
def f096hcn_f096_holder_concentration_hhi_pctslope_252d_2d_v186_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_pctslope_21d_2d_v187_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_pctslope_63d_2d_v188_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_pctslope_252d_2d_v189_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_pctslope_21d_2d_v190_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_pctslope_63d_2d_v191_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_pctslope_252d_2d_v192_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_pctslope_21d_2d_v193_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_pctslope_63d_2d_v194_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_pctslope_252d_2d_v195_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_pctslope_21d_2d_v196_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_pctslope_63d_2d_v197_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of top5_share
def f096hcn_f096_holder_concentration_top5_share_pctslope_252d_2d_v198_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_pctslope_21d_2d_v199_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_pctslope_63d_2d_v200_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

