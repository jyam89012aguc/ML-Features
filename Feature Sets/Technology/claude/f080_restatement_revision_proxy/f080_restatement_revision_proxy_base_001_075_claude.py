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


# 21d mean of revision_lvl scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_lvl_mean_21d_base_v001_signal(revision_flag, closeadj):
    base = revision_flag
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revision_lvl scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_lvl_mean_63d_base_v002_signal(revision_flag, closeadj):
    base = revision_flag
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revision_lvl scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_lvl_mean_126d_base_v003_signal(revision_flag, closeadj):
    base = revision_flag
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revision_lvl scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_lvl_mean_252d_base_v004_signal(revision_flag, closeadj):
    base = revision_flag
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revision_lvl scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_lvl_mean_504d_base_v005_signal(revision_flag, closeadj):
    base = revision_flag
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revision_252d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_252d_mean_21d_base_v006_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revision_252d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_252d_mean_63d_base_v007_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revision_252d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_252d_mean_126d_base_v008_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revision_252d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_252d_mean_252d_base_v009_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revision_252d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_252d_mean_504d_base_v010_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revision_504d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_504d_mean_21d_base_v011_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revision_504d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_504d_mean_63d_base_v012_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revision_504d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_504d_mean_126d_base_v013_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revision_504d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_504d_mean_252d_base_v014_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revision_504d scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_504d_mean_504d_base_v015_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revision_streak scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_streak_mean_21d_base_v016_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revision_streak scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_streak_mean_63d_base_v017_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revision_streak scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_streak_mean_126d_base_v018_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revision_streak scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_streak_mean_252d_base_v019_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revision_streak scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_streak_mean_504d_base_v020_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_delta_abs scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_mean_21d_base_v021_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_delta_abs scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_mean_63d_base_v022_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_delta_abs scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_mean_126d_base_v023_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_delta_abs scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_mean_252d_base_v024_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_delta_abs scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_mean_504d_base_v025_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rev_delta_pct scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_mean_21d_base_v026_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_delta_pct scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_mean_63d_base_v027_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_delta_pct scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_mean_126d_base_v028_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_delta_pct scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_mean_252d_base_v029_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_delta_pct scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_mean_504d_base_v030_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of revision_freq scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_freq_mean_21d_base_v031_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of revision_freq scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_freq_mean_63d_base_v032_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of revision_freq scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_freq_mean_126d_base_v033_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of revision_freq scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_freq_mean_252d_base_v034_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of revision_freq scaled by closeadj
def f080rvr_f080_restatement_revision_proxy_revision_freq_mean_504d_base_v035_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_median_63d_base_v036_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_median_252d_base_v037_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_median_504d_base_v038_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_median_63d_base_v039_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_median_252d_base_v040_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_median_504d_base_v041_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_median_63d_base_v042_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_median_252d_base_v043_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_median_504d_base_v044_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_median_63d_base_v045_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_median_252d_base_v046_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_median_504d_base_v047_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_median_63d_base_v048_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_median_252d_base_v049_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_median_504d_base_v050_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_median_63d_base_v051_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_median_252d_base_v052_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_median_504d_base_v053_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_median_63d_base_v054_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_median_252d_base_v055_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_median_504d_base_v056_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_rmax_252d_base_v057_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_rmax_504d_base_v058_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_rmax_252d_base_v059_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_rmax_504d_base_v060_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_rmax_252d_base_v061_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_rmax_504d_base_v062_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_rmax_252d_base_v063_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of revision_streak
def f080rvr_f080_restatement_revision_proxy_revision_streak_rmax_504d_base_v064_signal(revision_flag, closeadj):
    base = revision_flag.rolling(63, min_periods=21).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_rmax_252d_base_v065_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_delta_abs
def f080rvr_f080_restatement_revision_proxy_rev_delta_abs_rmax_504d_base_v066_signal(revision_value_delta, closeadj):
    base = revision_value_delta.abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_rmax_252d_base_v067_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_delta_pct
def f080rvr_f080_restatement_revision_proxy_rev_delta_pct_rmax_504d_base_v068_signal(revision_value_delta, revenue, closeadj):
    base = revision_value_delta / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_rmax_252d_base_v069_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of revision_freq
def f080rvr_f080_restatement_revision_proxy_revision_freq_rmax_504d_base_v070_signal(revision_flag, closeadj):
    base = revision_flag.rolling(252, min_periods=63).mean()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_rmin_252d_base_v071_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of revision_lvl
def f080rvr_f080_restatement_revision_proxy_revision_lvl_rmin_504d_base_v072_signal(revision_flag, closeadj):
    base = revision_flag
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_rmin_252d_base_v073_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of revision_252d
def f080rvr_f080_restatement_revision_proxy_revision_252d_rmin_504d_base_v074_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of revision_504d
def f080rvr_f080_restatement_revision_proxy_revision_504d_rmin_252d_base_v075_signal(revision_flag, closeadj):
    base = _f080_rev_count(revision_flag, 504)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

