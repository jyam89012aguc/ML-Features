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


# 21d acceleration of top_share
def f096hcn_f096_holder_concentration_top_share_accel_21d_3d_v001_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top_share
def f096hcn_f096_holder_concentration_top_share_accel_63d_3d_v002_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top_share
def f096hcn_f096_holder_concentration_top_share_accel_126d_3d_v003_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top_share
def f096hcn_f096_holder_concentration_top_share_accel_252d_3d_v004_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of hhi
def f096hcn_f096_holder_concentration_hhi_accel_21d_3d_v005_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of hhi
def f096hcn_f096_holder_concentration_hhi_accel_63d_3d_v006_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of hhi
def f096hcn_f096_holder_concentration_hhi_accel_126d_3d_v007_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of hhi
def f096hcn_f096_holder_concentration_hhi_accel_252d_3d_v008_signal(holder_hhi, closeadj):
    base = holder_hhi
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_accel_21d_3d_v009_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_accel_63d_3d_v010_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_accel_126d_3d_v011_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_accel_252d_3d_v012_signal(new_holder_count, closeadj):
    base = new_holder_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_accel_21d_3d_v013_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_accel_63d_3d_v014_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_accel_126d_3d_v015_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_accel_252d_3d_v016_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_accel_21d_3d_v017_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_accel_63d_3d_v018_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_accel_126d_3d_v019_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_accel_252d_3d_v020_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top5_share
def f096hcn_f096_holder_concentration_top5_share_accel_21d_3d_v021_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top5_share
def f096hcn_f096_holder_concentration_top5_share_accel_63d_3d_v022_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top5_share
def f096hcn_f096_holder_concentration_top5_share_accel_126d_3d_v023_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top5_share
def f096hcn_f096_holder_concentration_top5_share_accel_252d_3d_v024_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_accel_21d_3d_v025_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_accel_63d_3d_v026_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_accel_126d_3d_v027_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_accel_252d_3d_v028_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_accel_21d_3d_v029_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_accel_63d_3d_v030_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_accel_126d_3d_v031_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_accel_252d_3d_v032_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_accel_21d_3d_v033_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_accel_63d_3d_v034_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_accel_126d_3d_v035_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_accel_252d_3d_v036_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_accel_21d_3d_v037_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_accel_63d_3d_v038_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_accel_126d_3d_v039_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_accel_252d_3d_v040_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_accel_21d_3d_v041_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_accel_63d_3d_v042_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_accel_126d_3d_v043_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_accel_252d_3d_v044_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_accel_21d_3d_v045_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_accel_63d_3d_v046_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_accel_126d_3d_v047_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_accel_252d_3d_v048_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_accel_21d_3d_v049_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_accel_63d_3d_v050_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_accel_126d_3d_v051_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_accel_252d_3d_v052_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_accel_21d_3d_v053_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_accel_63d_3d_v054_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_accel_126d_3d_v055_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_accel_252d_3d_v056_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_accel_21d_3d_v057_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_accel_63d_3d_v058_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_accel_126d_3d_v059_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_accel_252d_3d_v060_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_accel_21d_3d_v061_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_accel_63d_3d_v062_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_accel_126d_3d_v063_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_accel_252d_3d_v064_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_accel_21d_3d_v065_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_accel_63d_3d_v066_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_accel_126d_3d_v067_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_accel_252d_3d_v068_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_accel_21d_3d_v069_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_accel_63d_3d_v070_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_accel_126d_3d_v071_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_accel_252d_3d_v072_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top_share
def f096hcn_f096_holder_concentration_top_share_slopez_21d_z126_3d_v073_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top_share
def f096hcn_f096_holder_concentration_top_share_slopez_63d_z252_3d_v074_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top_share
def f096hcn_f096_holder_concentration_top_share_slopez_126d_z252_3d_v075_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top_share
def f096hcn_f096_holder_concentration_top_share_slopez_252d_z504_3d_v076_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of hhi
def f096hcn_f096_holder_concentration_hhi_slopez_21d_z126_3d_v077_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of hhi
def f096hcn_f096_holder_concentration_hhi_slopez_63d_z252_3d_v078_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of hhi
def f096hcn_f096_holder_concentration_hhi_slopez_126d_z252_3d_v079_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of hhi
def f096hcn_f096_holder_concentration_hhi_slopez_252d_z504_3d_v080_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slopez_21d_z126_3d_v081_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slopez_63d_z252_3d_v082_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slopez_126d_z252_3d_v083_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_slopez_252d_z504_3d_v084_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slopez_21d_z126_3d_v085_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slopez_63d_z252_3d_v086_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slopez_126d_z252_3d_v087_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_slopez_252d_z504_3d_v088_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slopez_21d_z126_3d_v089_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slopez_63d_z252_3d_v090_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slopez_126d_z252_3d_v091_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_slopez_252d_z504_3d_v092_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top5_share
def f096hcn_f096_holder_concentration_top5_share_slopez_21d_z126_3d_v093_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top5_share
def f096hcn_f096_holder_concentration_top5_share_slopez_63d_z252_3d_v094_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top5_share
def f096hcn_f096_holder_concentration_top5_share_slopez_126d_z252_3d_v095_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top5_share
def f096hcn_f096_holder_concentration_top5_share_slopez_252d_z504_3d_v096_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slopez_21d_z126_3d_v097_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slopez_63d_z252_3d_v098_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slopez_126d_z252_3d_v099_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_slopez_252d_z504_3d_v100_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slopez_21d_z126_3d_v101_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slopez_63d_z252_3d_v102_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slopez_126d_z252_3d_v103_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_slopez_252d_z504_3d_v104_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slopez_21d_z126_3d_v105_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slopez_63d_z252_3d_v106_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slopez_126d_z252_3d_v107_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_slopez_252d_z504_3d_v108_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slopez_21d_z126_3d_v109_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slopez_63d_z252_3d_v110_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slopez_126d_z252_3d_v111_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_slopez_252d_z504_3d_v112_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slopez_21d_z126_3d_v113_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slopez_63d_z252_3d_v114_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slopez_126d_z252_3d_v115_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_slopez_252d_z504_3d_v116_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slopez_21d_z126_3d_v117_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slopez_63d_z252_3d_v118_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slopez_126d_z252_3d_v119_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_slopez_252d_z504_3d_v120_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slopez_21d_z126_3d_v121_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slopez_63d_z252_3d_v122_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slopez_126d_z252_3d_v123_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_slopez_252d_z504_3d_v124_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slopez_21d_z126_3d_v125_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slopez_63d_z252_3d_v126_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slopez_126d_z252_3d_v127_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_slopez_252d_z504_3d_v128_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slopez_21d_z126_3d_v129_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slopez_63d_z252_3d_v130_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slopez_126d_z252_3d_v131_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_slopez_252d_z504_3d_v132_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slopez_21d_z126_3d_v133_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slopez_63d_z252_3d_v134_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slopez_126d_z252_3d_v135_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_slopez_252d_z504_3d_v136_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slopez_21d_z126_3d_v137_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slopez_63d_z252_3d_v138_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slopez_126d_z252_3d_v139_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_slopez_252d_z504_3d_v140_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slopez_21d_z126_3d_v141_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slopez_63d_z252_3d_v142_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slopez_126d_z252_3d_v143_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_slopez_252d_z504_3d_v144_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top_share
def f096hcn_f096_holder_concentration_top_share_jerk_21d_3d_v145_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top_share
def f096hcn_f096_holder_concentration_top_share_jerk_63d_3d_v146_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top_share
def f096hcn_f096_holder_concentration_top_share_jerk_126d_3d_v147_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of hhi
def f096hcn_f096_holder_concentration_hhi_jerk_21d_3d_v148_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of hhi
def f096hcn_f096_holder_concentration_hhi_jerk_63d_3d_v149_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of hhi
def f096hcn_f096_holder_concentration_hhi_jerk_126d_3d_v150_signal(holder_hhi, closeadj):
    base = holder_hhi
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_jerk_21d_3d_v151_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_jerk_63d_3d_v152_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of new_holder_cnt
def f096hcn_f096_holder_concentration_new_holder_cnt_jerk_126d_3d_v153_signal(new_holder_count, closeadj):
    base = new_holder_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_jerk_21d_3d_v154_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_jerk_63d_3d_v155_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of exited_holder_cnt
def f096hcn_f096_holder_concentration_exited_holder_cnt_jerk_126d_3d_v156_signal(exited_holder_count, closeadj):
    base = exited_holder_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_jerk_21d_3d_v157_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_jerk_63d_3d_v158_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_holder_chg
def f096hcn_f096_holder_concentration_net_holder_chg_jerk_126d_3d_v159_signal(new_holder_count, exited_holder_count, closeadj):
    base = new_holder_count - exited_holder_count
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top5_share
def f096hcn_f096_holder_concentration_top5_share_jerk_21d_3d_v160_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top5_share
def f096hcn_f096_holder_concentration_top5_share_jerk_63d_3d_v161_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top5_share
def f096hcn_f096_holder_concentration_top5_share_jerk_126d_3d_v162_signal(top5_holder_value, inst_total_value, closeadj):
    base = top5_holder_value / inst_total_value.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_jerk_21d_3d_v163_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_jerk_63d_3d_v164_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of concentration_trend
def f096hcn_f096_holder_concentration_concentration_trend_jerk_126d_3d_v165_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_jerk_21d_3d_v166_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_jerk_63d_3d_v167_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top5_value_qoq_delta
def f096hcn_f096_holder_concentration_top5_value_qoq_delta_jerk_126d_3d_v168_signal(top5_holder_value, closeadj):
    base = top5_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_jerk_21d_3d_v169_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_jerk_63d_3d_v170_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top5_value_qoq_pct
def f096hcn_f096_holder_concentration_top5_value_qoq_pct_jerk_126d_3d_v171_signal(top5_holder_value, closeadj):
    base = top5_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_jerk_21d_3d_v172_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_jerk_63d_3d_v173_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top_holder_qoq_delta
def f096hcn_f096_holder_concentration_top_holder_qoq_delta_jerk_126d_3d_v174_signal(top_holder_value, closeadj):
    base = top_holder_value.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_jerk_21d_3d_v175_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_jerk_63d_3d_v176_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top_holder_qoq_pct
def f096hcn_f096_holder_concentration_top_holder_qoq_pct_jerk_126d_3d_v177_signal(top_holder_value, closeadj):
    base = top_holder_value.pct_change(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_jerk_21d_3d_v178_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_jerk_63d_3d_v179_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of new_holder_qoq_chg
def f096hcn_f096_holder_concentration_new_holder_qoq_chg_jerk_126d_3d_v180_signal(new_holder_count, closeadj):
    base = new_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_jerk_21d_3d_v181_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_jerk_63d_3d_v182_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of exited_holder_qoq_chg
def f096hcn_f096_holder_concentration_exited_holder_qoq_chg_jerk_126d_3d_v183_signal(exited_holder_count, closeadj):
    base = exited_holder_count.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_jerk_21d_3d_v184_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_jerk_63d_3d_v185_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of net_holder_chg_qoq
def f096hcn_f096_holder_concentration_net_holder_chg_qoq_jerk_126d_3d_v186_signal(new_holder_count, exited_holder_count, closeadj):
    base = (new_holder_count - exited_holder_count).diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_jerk_21d_3d_v187_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_jerk_63d_3d_v188_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of holder_breadth_burst
def f096hcn_f096_holder_concentration_holder_breadth_burst_jerk_126d_3d_v189_signal(new_holder_count, closeadj):
    base = (new_holder_count > new_holder_count.rolling(252, min_periods=63).quantile(0.90)).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_jerk_21d_3d_v190_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_jerk_63d_3d_v191_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of hhi_qoq_delta
def f096hcn_f096_holder_concentration_hhi_qoq_delta_jerk_126d_3d_v192_signal(holder_hhi, closeadj):
    base = holder_hhi.diff(periods=63)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_jerk_21d_3d_v193_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_jerk_63d_3d_v194_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of hhi_rising_streak
def f096hcn_f096_holder_concentration_hhi_rising_streak_jerk_126d_3d_v195_signal(holder_hhi, closeadj):
    base = (holder_hhi.diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_jerk_21d_3d_v196_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_jerk_63d_3d_v197_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of top5_share_to_sector_med
def f096hcn_f096_holder_concentration_top5_share_to_sector_med_jerk_126d_3d_v198_signal(top5_holder_value, inst_total_value, top5_share_sector_med, closeadj):
    base = (top5_holder_value / inst_total_value.replace(0, np.nan).abs() - top5_share_sector_med) / top5_share_sector_med.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of top_share smoothed over 252d
def f096hcn_f096_holder_concentration_top_share_smoothaccel_63d_sm252_3d_v199_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of top_share smoothed over 504d
def f096hcn_f096_holder_concentration_top_share_smoothaccel_252d_sm504_3d_v200_signal(top_holder_value, inst_total_value, closeadj):
    base = _f096_topshare(top_holder_value, inst_total_value)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

