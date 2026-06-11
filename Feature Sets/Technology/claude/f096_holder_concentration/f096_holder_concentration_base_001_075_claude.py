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


# 21d mean of top_share scaled by closeadj
def f096hcn_f096_holder_concentration_top_share_mean_21d_base_v001_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top_share scaled by closeadj
def f096hcn_f096_holder_concentration_top_share_mean_63d_base_v002_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top_share scaled by closeadj
def f096hcn_f096_holder_concentration_top_share_mean_126d_base_v003_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top_share scaled by closeadj
def f096hcn_f096_holder_concentration_top_share_mean_252d_base_v004_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top_share scaled by closeadj
def f096hcn_f096_holder_concentration_top_share_mean_504d_base_v005_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of hhi scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_mean_21d_base_v006_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of hhi scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_mean_63d_base_v007_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of hhi scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_mean_126d_base_v008_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of hhi scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_mean_252d_base_v009_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of hhi scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_mean_504d_base_v010_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of new_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_cnt_mean_21d_base_v011_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of new_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_cnt_mean_63d_base_v012_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of new_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_cnt_mean_126d_base_v013_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of new_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_cnt_mean_252d_base_v014_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of new_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_cnt_mean_504d_base_v015_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of exited_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_cnt_mean_21d_base_v016_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of exited_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_cnt_mean_63d_base_v017_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of exited_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_cnt_mean_126d_base_v018_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of exited_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_cnt_mean_252d_base_v019_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of exited_holder_cnt scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_cnt_mean_504d_base_v020_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of net_holder_chg scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_mean_21d_base_v021_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_holder_chg scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_mean_63d_base_v022_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_holder_chg scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_mean_126d_base_v023_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_holder_chg scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_mean_252d_base_v024_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_holder_chg scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_mean_504d_base_v025_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top5_share scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_mean_21d_base_v026_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top5_share scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_mean_63d_base_v027_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top5_share scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_mean_126d_base_v028_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top5_share scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_mean_252d_base_v029_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top5_share scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_mean_504d_base_v030_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of concentration_trend scaled by closeadj
def f096hcn_f096_holder_concentration_concentration_trend_mean_21d_base_v031_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of concentration_trend scaled by closeadj
def f096hcn_f096_holder_concentration_concentration_trend_mean_63d_base_v032_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of concentration_trend scaled by closeadj
def f096hcn_f096_holder_concentration_concentration_trend_mean_126d_base_v033_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of concentration_trend scaled by closeadj
def f096hcn_f096_holder_concentration_concentration_trend_mean_252d_base_v034_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of concentration_trend scaled by closeadj
def f096hcn_f096_holder_concentration_concentration_trend_mean_504d_base_v035_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top5_value_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_mean_21d_base_v036_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top5_value_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_mean_63d_base_v037_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top5_value_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_mean_126d_base_v038_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top5_value_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_mean_252d_base_v039_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top5_value_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_mean_504d_base_v040_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top5_value_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_mean_21d_base_v041_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top5_value_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_mean_63d_base_v042_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top5_value_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_mean_126d_base_v043_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top5_value_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_mean_252d_base_v044_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top5_value_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_mean_504d_base_v045_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top_holder_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_mean_21d_base_v046_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top_holder_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_mean_63d_base_v047_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top_holder_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_mean_126d_base_v048_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top_holder_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_mean_252d_base_v049_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top_holder_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_mean_504d_base_v050_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top_holder_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_mean_21d_base_v051_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top_holder_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_mean_63d_base_v052_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top_holder_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_mean_126d_base_v053_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top_holder_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_mean_252d_base_v054_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top_holder_qoq_pct scaled by closeadj
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_mean_504d_base_v055_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of new_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_mean_21d_base_v056_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of new_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_mean_63d_base_v057_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of new_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_mean_126d_base_v058_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of new_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_mean_252d_base_v059_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of new_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_mean_504d_base_v060_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of exited_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_mean_21d_base_v061_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of exited_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_mean_63d_base_v062_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of exited_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_mean_126d_base_v063_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of exited_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_mean_252d_base_v064_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of exited_holder_qoq_chg scaled by closeadj
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_mean_504d_base_v065_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of net_holder_chg_qoq scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_mean_21d_base_v066_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of net_holder_chg_qoq scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_mean_63d_base_v067_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of net_holder_chg_qoq scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_mean_126d_base_v068_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of net_holder_chg_qoq scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_mean_252d_base_v069_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of net_holder_chg_qoq scaled by closeadj
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_mean_504d_base_v070_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of holder_breadth_burst scaled by closeadj
def f096hcn_f096_holder_concentration_holder_breadth_burst_mean_21d_base_v071_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of holder_breadth_burst scaled by closeadj
def f096hcn_f096_holder_concentration_holder_breadth_burst_mean_63d_base_v072_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of holder_breadth_burst scaled by closeadj
def f096hcn_f096_holder_concentration_holder_breadth_burst_mean_126d_base_v073_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of holder_breadth_burst scaled by closeadj
def f096hcn_f096_holder_concentration_holder_breadth_burst_mean_252d_base_v074_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of holder_breadth_burst scaled by closeadj
def f096hcn_f096_holder_concentration_holder_breadth_burst_mean_504d_base_v075_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of hhi_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_qoq_delta_mean_21d_base_v076_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of hhi_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_qoq_delta_mean_63d_base_v077_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of hhi_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_qoq_delta_mean_126d_base_v078_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of hhi_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_qoq_delta_mean_252d_base_v079_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of hhi_qoq_delta scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_qoq_delta_mean_504d_base_v080_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of hhi_rising_streak scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_rising_streak_mean_21d_base_v081_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of hhi_rising_streak scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_rising_streak_mean_63d_base_v082_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of hhi_rising_streak scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_rising_streak_mean_126d_base_v083_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of hhi_rising_streak scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_rising_streak_mean_252d_base_v084_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of hhi_rising_streak scaled by closeadj
def f096hcn_f096_holder_concentration_hhi_rising_streak_mean_504d_base_v085_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of top5_share_to_sector_med scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_mean_21d_base_v086_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of top5_share_to_sector_med scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_mean_63d_base_v087_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of top5_share_to_sector_med scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_mean_126d_base_v088_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of top5_share_to_sector_med scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_mean_252d_base_v089_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of top5_share_to_sector_med scaled by closeadj
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_mean_504d_base_v090_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of top_share
def f096hcn_f096_holder_concentration_top_share_median_63d_base_v091_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of top_share
def f096hcn_f096_holder_concentration_top_share_median_252d_base_v092_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of top_share
def f096hcn_f096_holder_concentration_top_share_median_504d_base_v093_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of hhi
def f096hcn_f096_holder_concentration_hhi_median_63d_base_v094_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of hhi
def f096hcn_f096_holder_concentration_hhi_median_252d_base_v095_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of hhi
def f096hcn_f096_holder_concentration_hhi_median_504d_base_v096_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_median_63d_base_v097_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_median_252d_base_v098_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_median_504d_base_v099_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_median_63d_base_v100_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

