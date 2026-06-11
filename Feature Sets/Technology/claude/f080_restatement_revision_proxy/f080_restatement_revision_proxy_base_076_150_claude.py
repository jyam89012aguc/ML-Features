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
def _f080_rev_count(revision_flag, w):
    return revision_flag.rolling(w, min_periods=max(1, w//2)).sum()


# 63d z-score of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_z_63d_base_v076_signal(revision_flag, closeadj):
    base = revision_flag
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_z_126d_base_v077_signal(revision_flag, closeadj):
    base = revision_flag
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_z_252d_base_v078_signal(revision_flag, closeadj):
    base = revision_flag
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_z_504d_base_v079_signal(revision_flag, closeadj):
    base = revision_flag
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_z_63d_base_v080_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_z_126d_base_v081_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_z_252d_base_v082_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_z_504d_base_v083_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_z_63d_base_v084_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_z_126d_base_v085_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_z_252d_base_v086_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_z_504d_base_v087_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_z_63d_base_v088_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_z_126d_base_v089_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_z_252d_base_v090_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_z_504d_base_v091_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_z_63d_base_v092_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_z_126d_base_v093_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_z_252d_base_v094_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_z_504d_base_v095_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_z_63d_base_v096_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_z_126d_base_v097_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_z_252d_base_v098_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_z_504d_base_v099_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_z_63d_base_v100_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_z_126d_base_v101_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_z_252d_base_v102_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_z_504d_base_v103_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_distmax_252d_base_v104_signal(revision_flag, closeadj):
    base = revision_flag
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_distmax_504d_base_v105_signal(revision_flag, closeadj):
    base = revision_flag
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_distmax_252d_base_v106_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_distmax_504d_base_v107_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_distmax_252d_base_v108_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_distmax_504d_base_v109_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_distmax_252d_base_v110_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_distmax_504d_base_v111_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_distmax_252d_base_v112_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_distmax_504d_base_v113_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_distmax_252d_base_v114_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_distmax_504d_base_v115_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_distmax_252d_base_v116_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_distmax_504d_base_v117_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_distmed_126d_base_v118_signal(revision_flag, closeadj):
    base = revision_flag
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_distmed_252d_base_v119_signal(revision_flag, closeadj):
    base = revision_flag
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_distmed_504d_base_v120_signal(revision_flag, closeadj):
    base = revision_flag
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_distmed_126d_base_v121_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_distmed_252d_base_v122_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_distmed_504d_base_v123_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_distmed_126d_base_v124_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_distmed_252d_base_v125_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_distmed_504d_base_v126_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_distmed_126d_base_v127_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_distmed_252d_base_v128_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_distmed_504d_base_v129_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_distmed_126d_base_v130_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_distmed_252d_base_v131_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_distmed_504d_base_v132_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_distmed_126d_base_v133_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_distmed_252d_base_v134_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_distmed_504d_base_v135_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_distmed_126d_base_v136_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_distmed_252d_base_v137_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_distmed_504d_base_v138_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_chg_63d_base_v139_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_chg_252d_base_v140_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_chg_63d_base_v141_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_chg_252d_base_v142_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_chg_63d_base_v143_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_chg_252d_base_v144_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_chg_63d_base_v145_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_chg_252d_base_v146_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_chg_63d_base_v147_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_chg_252d_base_v148_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_chg_63d_base_v149_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_chg_252d_base_v150_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

