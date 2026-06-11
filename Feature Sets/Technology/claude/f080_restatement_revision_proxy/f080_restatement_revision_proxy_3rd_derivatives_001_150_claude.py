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
def _f080_rev_count(revision_flag, w):
    return revision_flag.rolling(w, min_periods=max(1, w//2)).sum()


# 21d acceleration of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_accel_21d_3d_v001_signal(revision_flag, closeadj):
    base = revision_flag
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_accel_63d_3d_v002_signal(revision_flag, closeadj):
    base = revision_flag
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_accel_126d_3d_v003_signal(revision_flag, closeadj):
    base = revision_flag
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_accel_252d_3d_v004_signal(revision_flag, closeadj):
    base = revision_flag
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_accel_21d_3d_v005_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_accel_63d_3d_v006_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_accel_126d_3d_v007_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_accel_252d_3d_v008_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_accel_21d_3d_v009_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_accel_63d_3d_v010_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_accel_126d_3d_v011_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_accel_252d_3d_v012_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_accel_21d_3d_v013_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_accel_63d_3d_v014_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_accel_126d_3d_v015_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_accel_252d_3d_v016_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_accel_21d_3d_v017_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_accel_63d_3d_v018_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_accel_126d_3d_v019_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_accel_252d_3d_v020_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_accel_21d_3d_v021_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_accel_63d_3d_v022_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_accel_126d_3d_v023_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_accel_252d_3d_v024_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_accel_21d_3d_v025_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_accel_63d_3d_v026_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_accel_126d_3d_v027_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_accel_252d_3d_v028_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slopez_21d_z126_3d_v029_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slopez_63d_z252_3d_v030_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slopez_126d_z252_3d_v031_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slopez_252d_z504_3d_v032_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slopez_21d_z126_3d_v033_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slopez_63d_z252_3d_v034_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slopez_126d_z252_3d_v035_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slopez_252d_z504_3d_v036_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slopez_21d_z126_3d_v037_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slopez_63d_z252_3d_v038_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slopez_126d_z252_3d_v039_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slopez_252d_z504_3d_v040_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slopez_21d_z126_3d_v041_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slopez_63d_z252_3d_v042_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slopez_126d_z252_3d_v043_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slopez_252d_z504_3d_v044_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slopez_21d_z126_3d_v045_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slopez_63d_z252_3d_v046_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slopez_126d_z252_3d_v047_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slopez_252d_z504_3d_v048_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slopez_21d_z126_3d_v049_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slopez_63d_z252_3d_v050_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slopez_126d_z252_3d_v051_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slopez_252d_z504_3d_v052_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slopez_21d_z126_3d_v053_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slopez_63d_z252_3d_v054_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slopez_126d_z252_3d_v055_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slopez_252d_z504_3d_v056_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_jerk_21d_3d_v057_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_jerk_63d_3d_v058_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_jerk_126d_3d_v059_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_jerk_21d_3d_v060_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_jerk_63d_3d_v061_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_jerk_126d_3d_v062_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_jerk_21d_3d_v063_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_jerk_63d_3d_v064_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_jerk_126d_3d_v065_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_jerk_21d_3d_v066_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_jerk_63d_3d_v067_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_jerk_126d_3d_v068_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_jerk_21d_3d_v069_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_jerk_63d_3d_v070_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_jerk_126d_3d_v071_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_jerk_21d_3d_v072_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_jerk_63d_3d_v073_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_jerk_126d_3d_v074_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_jerk_21d_3d_v075_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_jerk_63d_3d_v076_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_jerk_126d_3d_v077_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of revision_lvl smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_revision_lvl_smoothaccel_63d_sm252_3d_v078_signal(revision_flag, closeadj):
    base = revision_flag
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of revision_lvl smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_revision_lvl_smoothaccel_252d_sm504_3d_v079_signal(revision_flag, closeadj):
    base = revision_flag
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of revision_252d smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_smoothaccel_63d_sm252_3d_v080_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of revision_252d smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_revision_252d_smoothaccel_252d_sm504_3d_v081_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of revision_504d smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_revision_504d_smoothaccel_63d_sm252_3d_v082_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of revision_504d smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_smoothaccel_252d_sm504_3d_v083_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of revision_streak smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_revision_streak_smoothaccel_63d_sm252_3d_v084_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of revision_streak smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_revision_streak_smoothaccel_252d_sm504_3d_v085_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_delta_abs smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_smoothaccel_63d_sm252_3d_v086_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_delta_abs smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_smoothaccel_252d_sm504_3d_v087_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_delta_pct smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_smoothaccel_63d_sm252_3d_v088_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_delta_pct smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_smoothaccel_252d_sm504_3d_v089_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of revision_freq smoothed over 252d
def f080rvr_f080_restatement_revision_proxy_revision_freq_smoothaccel_63d_sm252_3d_v090_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of revision_freq smoothed over 504d
def f080rvr_f080_restatement_revision_proxy_revision_freq_smoothaccel_252d_sm504_3d_v091_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_accelz_21d_z252_3d_v092_signal(revision_flag, closeadj):
    base = revision_flag
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_accelz_63d_z504_3d_v093_signal(revision_flag, closeadj):
    base = revision_flag
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_accelz_21d_z252_3d_v094_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_accelz_63d_z504_3d_v095_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_accelz_21d_z252_3d_v096_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_accelz_63d_z504_3d_v097_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_accelz_21d_z252_3d_v098_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_accelz_63d_z504_3d_v099_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_accelz_21d_z252_3d_v100_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_accelz_63d_z504_3d_v101_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_accelz_21d_z252_3d_v102_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_accelz_63d_z504_3d_v103_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_accelz_21d_z252_3d_v104_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_accelz_63d_z504_3d_v105_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in revision_lvl (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_lvl_signflip_63d_3d_v106_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in revision_lvl (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_lvl_signflip_252d_3d_v107_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in revision_252d (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_252d_signflip_63d_3d_v108_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in revision_252d (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_252d_signflip_252d_3d_v109_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in revision_504d (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_504d_signflip_63d_3d_v110_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in revision_504d (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_504d_signflip_252d_3d_v111_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in revision_streak (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_streak_signflip_63d_3d_v112_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in revision_streak (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_streak_signflip_252d_3d_v113_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_delta_abs (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_signflip_63d_3d_v114_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_delta_abs (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_signflip_252d_3d_v115_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_delta_pct (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_signflip_63d_3d_v116_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_delta_pct (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_signflip_252d_3d_v117_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in revision_freq (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_freq_signflip_63d_3d_v118_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in revision_freq (raw count, no price scaling)
def f080rvr_f080_restatement_revision_proxy_revision_freq_signflip_252d_3d_v119_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_lvl normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_revision_lvl_rngaccel_63d_r252_3d_v120_signal(revision_flag, closeadj):
    base = revision_flag
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_lvl normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_revision_lvl_rngaccel_252d_r504_3d_v121_signal(revision_flag, closeadj):
    base = revision_flag
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_252d normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_revision_252d_rngaccel_63d_r252_3d_v122_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_252d normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_revision_252d_rngaccel_252d_r504_3d_v123_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_504d normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_revision_504d_rngaccel_63d_r252_3d_v124_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_504d normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_revision_504d_rngaccel_252d_r504_3d_v125_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_streak normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_revision_streak_rngaccel_63d_r252_3d_v126_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_streak normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_revision_streak_rngaccel_252d_r504_3d_v127_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_delta_abs normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_rngaccel_63d_r252_3d_v128_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_delta_abs normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_rngaccel_252d_r504_3d_v129_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_delta_pct normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_rngaccel_63d_r252_3d_v130_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_delta_pct normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_rngaccel_252d_r504_3d_v131_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of revision_freq normalized by 252d range
def f080rvr_f080_restatement_revision_proxy_revision_freq_rngaccel_63d_r252_3d_v132_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of revision_freq normalized by 504d range
def f080rvr_f080_restatement_revision_proxy_revision_freq_rngaccel_252d_r504_3d_v133_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_cumslope_21d_3d_v134_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_cumslope_63d_3d_v135_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_cumslope_252d_3d_v136_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_cumslope_21d_3d_v137_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_cumslope_63d_3d_v138_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_cumslope_252d_3d_v139_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_cumslope_21d_3d_v140_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_cumslope_63d_3d_v141_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_cumslope_252d_3d_v142_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_cumslope_21d_3d_v143_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_cumslope_63d_3d_v144_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_cumslope_252d_3d_v145_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_cumslope_21d_3d_v146_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_cumslope_63d_3d_v147_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_cumslope_252d_3d_v148_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_cumslope_21d_3d_v149_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_cumslope_63d_3d_v150_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

