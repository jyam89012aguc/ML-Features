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
def _f017_qchg(rnd):
    return rnd.diff(periods=63)


def _f017_ychg(rnd):
    return rnd.diff(periods=252)


# 21d mean of rnd_qchg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_qchg_mean_21d_base_v001_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_qchg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_qchg_mean_63d_base_v002_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_qchg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_qchg_mean_126d_base_v003_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_qchg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_qchg_mean_252d_base_v004_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_qchg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_qchg_mean_504d_base_v005_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_ychg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_ychg_mean_21d_base_v006_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_ychg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_ychg_mean_63d_base_v007_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_ychg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_ychg_mean_126d_base_v008_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_ychg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_ychg_mean_252d_base_v009_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_ychg scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_ychg_mean_504d_base_v010_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_pct_q scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_q_mean_21d_base_v011_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_pct_q scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_q_mean_63d_base_v012_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_pct_q scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_q_mean_126d_base_v013_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_pct_q scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_q_mean_252d_base_v014_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_pct_q scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_q_mean_504d_base_v015_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_pct_y scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_y_mean_21d_base_v016_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_pct_y scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_y_mean_63d_base_v017_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_pct_y scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_y_mean_126d_base_v018_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_pct_y scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_y_mean_252d_base_v019_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_pct_y scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_pct_y_mean_504d_base_v020_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_growth_to_rev_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_mean_21d_base_v021_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_growth_to_rev_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_mean_63d_base_v022_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_growth_to_rev_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_mean_126d_base_v023_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_growth_to_rev_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_mean_252d_base_v024_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_growth_to_rev_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_mean_504d_base_v025_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_to_prior scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_to_prior_mean_21d_base_v026_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_to_prior scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_to_prior_mean_63d_base_v027_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_to_prior scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_to_prior_mean_126d_base_v028_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_to_prior scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_to_prior_mean_252d_base_v029_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_to_prior scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_to_prior_mean_504d_base_v030_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_log_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_log_growth_mean_21d_base_v031_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_log_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_log_growth_mean_63d_base_v032_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_log_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_log_growth_mean_126d_base_v033_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_log_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_log_growth_mean_252d_base_v034_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_log_growth scaled by closeadj
def f017rdg_f017_rnd_growth_rnd_log_growth_mean_504d_base_v035_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_median_63d_base_v036_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_median_252d_base_v037_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_median_504d_base_v038_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_median_63d_base_v039_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_median_252d_base_v040_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_median_504d_base_v041_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_median_63d_base_v042_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_median_252d_base_v043_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_median_504d_base_v044_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_median_63d_base_v045_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_median_252d_base_v046_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_median_504d_base_v047_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_median_63d_base_v048_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_median_252d_base_v049_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_median_504d_base_v050_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_median_63d_base_v051_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_median_252d_base_v052_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_median_504d_base_v053_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_median_63d_base_v054_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_median_252d_base_v055_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_median_504d_base_v056_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_rmax_252d_base_v057_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_rmax_504d_base_v058_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_rmax_252d_base_v059_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_rmax_504d_base_v060_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_rmax_252d_base_v061_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_rmax_504d_base_v062_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_rmax_252d_base_v063_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_pct_y
def f017rdg_f017_rnd_growth_rnd_pct_y_rmax_504d_base_v064_signal(rnd, closeadj):
    base = rnd.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_rmax_252d_base_v065_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_growth_to_rev_growth
def f017rdg_f017_rnd_growth_rnd_growth_to_rev_growth_rmax_504d_base_v066_signal(rnd, revenue, closeadj):
    base = rnd.pct_change(periods=252) - revenue.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_rmax_252d_base_v067_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_to_prior
def f017rdg_f017_rnd_growth_rnd_to_prior_rmax_504d_base_v068_signal(rnd, closeadj):
    base = rnd / rnd.shift(252).replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_rmax_252d_base_v069_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_log_growth
def f017rdg_f017_rnd_growth_rnd_log_growth_rmax_504d_base_v070_signal(rnd, closeadj):
    base = np.log(rnd.abs().replace(0, np.nan)) - np.log(rnd.shift(252).abs().replace(0, np.nan))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_rmin_252d_base_v071_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rnd_qchg
def f017rdg_f017_rnd_growth_rnd_qchg_rmin_504d_base_v072_signal(rnd, closeadj):
    base = _f017_qchg(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_rmin_252d_base_v073_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rnd_ychg
def f017rdg_f017_rnd_growth_rnd_ychg_rmin_504d_base_v074_signal(rnd, closeadj):
    base = _f017_ychg(rnd)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rnd_pct_q
def f017rdg_f017_rnd_growth_rnd_pct_q_rmin_252d_base_v075_signal(rnd, closeadj):
    base = rnd.pct_change(periods=63)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

