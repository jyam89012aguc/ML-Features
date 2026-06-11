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


# 21d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slope_21d_2d_v001_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slope_63d_2d_v002_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slope_126d_2d_v003_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slope_252d_2d_v004_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_slope_504d_2d_v005_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slope_21d_2d_v006_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slope_63d_2d_v007_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slope_126d_2d_v008_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slope_252d_2d_v009_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_slope_504d_2d_v010_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slope_21d_2d_v011_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slope_63d_2d_v012_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slope_126d_2d_v013_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slope_252d_2d_v014_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_slope_504d_2d_v015_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slope_21d_2d_v016_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slope_63d_2d_v017_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slope_126d_2d_v018_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slope_252d_2d_v019_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_slope_504d_2d_v020_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slope_21d_2d_v021_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slope_63d_2d_v022_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slope_126d_2d_v023_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slope_252d_2d_v024_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_slope_504d_2d_v025_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slope_21d_2d_v026_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slope_63d_2d_v027_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slope_126d_2d_v028_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slope_252d_2d_v029_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_slope_504d_2d_v030_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slope_21d_2d_v031_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slope_63d_2d_v032_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slope_126d_2d_v033_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slope_252d_2d_v034_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_slope_504d_2d_v035_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sm21_sl21_2d_v036_signal(revision_flag, closeadj):
    base = _mean(revision_flag, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sm63_sl21_2d_v037_signal(revision_flag, closeadj):
    base = _mean(revision_flag, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sm63_sl63_2d_v038_signal(revision_flag, closeadj):
    base = _mean(revision_flag, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sm252_sl63_2d_v039_signal(revision_flag, closeadj):
    base = _mean(revision_flag, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sm252_sl126_2d_v040_signal(revision_flag, closeadj):
    base = _mean(revision_flag, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sm21_sl21_2d_v041_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sm63_sl21_2d_v042_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sm63_sl63_2d_v043_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sm252_sl63_2d_v044_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sm252_sl126_2d_v045_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sm21_sl21_2d_v046_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 504), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sm63_sl21_2d_v047_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 504), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sm63_sl63_2d_v048_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 504), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sm252_sl63_2d_v049_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 504), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sm252_sl126_2d_v050_signal(revision_flag, closeadj):
    base = _mean(_f080_rev_count(revision_flag, 504), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sm21_sl21_2d_v051_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(63, min_periods=21).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sm63_sl21_2d_v052_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(63, min_periods=21).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sm63_sl63_2d_v053_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(63, min_periods=21).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sm252_sl63_2d_v054_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(63, min_periods=21).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sm252_sl126_2d_v055_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(63, min_periods=21).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sm21_sl21_2d_v056_signal(revision_value_delta, closeadj):
    base = _mean(revision_value_delta.abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sm63_sl21_2d_v057_signal(revision_value_delta, closeadj):
    base = _mean(revision_value_delta.abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sm63_sl63_2d_v058_signal(revision_value_delta, closeadj):
    base = _mean(revision_value_delta.abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sm252_sl63_2d_v059_signal(revision_value_delta, closeadj):
    base = _mean(revision_value_delta.abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sm252_sl126_2d_v060_signal(revision_value_delta, closeadj):
    base = _mean(revision_value_delta.abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sm21_sl21_2d_v061_signal(revision_value_delta, revenue, closeadj):
    base = _mean(revision_value_delta / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sm63_sl21_2d_v062_signal(revision_value_delta, revenue, closeadj):
    base = _mean(revision_value_delta / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sm63_sl63_2d_v063_signal(revision_value_delta, revenue, closeadj):
    base = _mean(revision_value_delta / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sm252_sl63_2d_v064_signal(revision_value_delta, revenue, closeadj):
    base = _mean(revision_value_delta / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sm252_sl126_2d_v065_signal(revision_value_delta, revenue, closeadj):
    base = _mean(revision_value_delta / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sm21_sl21_2d_v066_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(252, min_periods=63).mean(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sm63_sl21_2d_v067_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sm63_sl63_2d_v068_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(252, min_periods=63).mean(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sm252_sl63_2d_v069_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sm252_sl126_2d_v070_signal(revision_flag, closeadj):
    base = _mean(revision_flag.rolling(252, min_periods=63).mean(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_pctslope_21d_2d_v071_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_pctslope_63d_2d_v072_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_pctslope_252d_2d_v073_signal(revision_flag, closeadj):
    base = revision_flag
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_pctslope_21d_2d_v074_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_pctslope_63d_2d_v075_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_pctslope_252d_2d_v076_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_pctslope_21d_2d_v077_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_pctslope_63d_2d_v078_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_pctslope_252d_2d_v079_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_pctslope_21d_2d_v080_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_pctslope_63d_2d_v081_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_pctslope_252d_2d_v082_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_pctslope_21d_2d_v083_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_pctslope_63d_2d_v084_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_pctslope_252d_2d_v085_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_pctslope_21d_2d_v086_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_pctslope_63d_2d_v087_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_pctslope_252d_2d_v088_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_pctslope_21d_2d_v089_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_pctslope_63d_2d_v090_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_pctslope_252d_2d_v091_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sgnslope_21d_2d_v092_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sgnslope_63d_2d_v093_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_sgnslope_252d_2d_v094_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sgnslope_21d_2d_v095_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sgnslope_63d_2d_v096_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_sgnslope_252d_2d_v097_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sgnslope_21d_2d_v098_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sgnslope_63d_2d_v099_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_sgnslope_252d_2d_v100_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sgnslope_21d_2d_v101_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sgnslope_63d_2d_v102_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_sgnslope_252d_2d_v103_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sgnslope_21d_2d_v104_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sgnslope_63d_2d_v105_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_sgnslope_252d_2d_v106_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sgnslope_21d_2d_v107_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sgnslope_63d_2d_v108_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_sgnslope_252d_2d_v109_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sgnslope_21d_2d_v110_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sgnslope_63d_2d_v111_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_sgnslope_252d_2d_v112_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_logmagslope_21d_2d_v113_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_logmagslope_63d_2d_v114_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_logmagslope_252d_2d_v115_signal(revision_flag, closeadj):
    base = revision_flag
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_logmagslope_21d_2d_v116_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_logmagslope_63d_2d_v117_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_logmagslope_252d_2d_v118_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_logmagslope_21d_2d_v119_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_logmagslope_63d_2d_v120_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_logmagslope_252d_2d_v121_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_logmagslope_21d_2d_v122_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_logmagslope_63d_2d_v123_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_logmagslope_252d_2d_v124_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_logmagslope_21d_2d_v125_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_logmagslope_63d_2d_v126_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_logmagslope_252d_2d_v127_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_logmagslope_21d_2d_v128_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_logmagslope_63d_2d_v129_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_logmagslope_252d_2d_v130_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_logmagslope_21d_2d_v131_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_logmagslope_63d_2d_v132_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_logmagslope_252d_2d_v133_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|revision_lvl|
def f080rvr_f080_restatement_revision_proxy_revision_lvl_logslope_63d_2d_v134_signal(revision_flag, closeadj):
    base = np.log((revision_flag).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|revision_lvl|
def f080rvr_f080_restatement_revision_proxy_revision_lvl_logslope_252d_2d_v135_signal(revision_flag, closeadj):
    base = np.log((revision_flag).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|revision_252d|
def f080rvr_f080_restatement_revision_proxy_revision_252d_logslope_63d_2d_v136_signal(revision_flag, closeadj):
    base = np.log((_f080_rev_count(revision_flag, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|revision_252d|
def f080rvr_f080_restatement_revision_proxy_revision_252d_logslope_252d_2d_v137_signal(revision_flag, closeadj):
    base = np.log((_f080_rev_count(revision_flag, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|revision_504d|
def f080rvr_f080_restatement_revision_proxy_revision_504d_logslope_63d_2d_v138_signal(revision_flag, closeadj):
    base = np.log((_f080_rev_count(revision_flag, 504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|revision_504d|
def f080rvr_f080_restatement_revision_proxy_revision_504d_logslope_252d_2d_v139_signal(revision_flag, closeadj):
    base = np.log((_f080_rev_count(revision_flag, 504)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|revision_streak|
def f080rvr_f080_restatement_revision_proxy_revision_streak_logslope_63d_2d_v140_signal(revision_flag, closeadj):
    base = np.log((revision_flag.rolling(63, min_periods=21).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|revision_streak|
def f080rvr_f080_restatement_revision_proxy_revision_streak_logslope_252d_2d_v141_signal(revision_flag, closeadj):
    base = np.log((revision_flag.rolling(63, min_periods=21).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_delta_abs|
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_logslope_63d_2d_v142_signal(revision_value_delta, closeadj):
    base = np.log((revision_value_delta.abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_delta_abs|
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_logslope_252d_2d_v143_signal(revision_value_delta, closeadj):
    base = np.log((revision_value_delta.abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rev_delta_pct|
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_logslope_63d_2d_v144_signal(revision_value_delta, revenue, closeadj):
    base = np.log((revision_value_delta / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rev_delta_pct|
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_logslope_252d_2d_v145_signal(revision_value_delta, revenue, closeadj):
    base = np.log((revision_value_delta / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|revision_freq|
def f080rvr_f080_restatement_revision_proxy_revision_freq_logslope_63d_2d_v146_signal(revision_flag, closeadj):
    base = np.log((revision_flag.rolling(252, min_periods=63).mean()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|revision_freq|
def f080rvr_f080_restatement_revision_proxy_revision_freq_logslope_252d_2d_v147_signal(revision_flag, closeadj):
    base = np.log((revision_flag.rolling(252, min_periods=63).mean()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

